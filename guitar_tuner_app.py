import customtkinter as ctk
from tkinter import messagebox
import threading
import time
from typing import Optional

from models import TuningRepository, TuningPreset, CustomTuning, InstrumentRepository, Instrument
from audio import AudioStreamManager, FFTFrequencyDetector, AudioProcessor
from analysis import TuningAnalyzer, TuningStatus
from gui import (
    TuningMeterWidget, TuningSelector, StringSelector,
    FrequencyDisplay, ControlButtons, CustomTuningDialog, InstrumentSelector
)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class GuitarTunerApp:
    def __init__(self):
        self.instrument_repository = InstrumentRepository()
        self.current_instrument = self.instrument_repository.get_default_instrument()

        self.tuning_repository = TuningRepository()
        self.current_tuning = list(self.current_instrument.get_tuning_presets().values())[0]
        self.current_string = self.current_tuning.get_string_names()[0]

        self.stream_manager = AudioStreamManager(chunk_size=4096, sample_rate=44100)
        self.frequency_detector = FFTFrequencyDetector(
            sample_rate=self.stream_manager.sample_rate,
            chunk_size=self.stream_manager.chunk_size,
            min_frequency=self.current_instrument.min_frequency,
            max_frequency=self.current_instrument.max_frequency
        )
        self.audio_processor = AudioProcessor(
            stream_manager=self.stream_manager,
            frequency_detector=self.frequency_detector
        )

        self.tuning_analyzer = TuningAnalyzer(in_tune_threshold=3.0, close_threshold=15.0)

        self.audio_thread = None
        self.is_running = False

        self.root = ctk.CTk()
        self._setup_gui()

    def _setup_gui(self):
        self.root.title("🎸 Guitar Tuner Pro")
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', lambda e: self.root.attributes('-fullscreen', False))
        self.root.bind('<F11>', lambda e: self.root.attributes('-fullscreen', True))
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

        header_frame = ctk.CTkFrame(self.root, fg_color="#1e1e1e", corner_radius=15)
        header_frame.pack(pady=20, padx=20, fill="x")

        title_label = ctk.CTkLabel(
            header_frame,
            text="🎸 Guitar Tuner Pro",
            font=("Segoe UI", 42, "bold"),
            text_color="#00ff88"
        )
        title_label.pack(pady=20)

        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Professional Instrument Tuning",
            font=("Segoe UI", 14),
            text_color="#888888"
        )
        subtitle_label.pack(pady=(0, 15))

        settings_frame = ctk.CTkFrame(self.root, fg_color="#1e1e1e", corner_radius=15)
        settings_frame.pack(pady=10, padx=20, fill="x")

        instrument_display_names = [
            inst.full_display_name for inst in self.instrument_repository.get_all_instruments().values()
        ]
        self.instrument_selector = InstrumentSelector(
            settings_frame,
            instrument_display_names,
            self._on_instrument_change
        )
        self.instrument_selector.pack(pady=15, padx=15)

        self.tuning_selector = TuningSelector(
            settings_frame,
            self.current_instrument.get_tuning_preset_names(),
            self._on_tuning_change,
            self._on_custom_tuning_click
        )
        self.tuning_selector.pack(pady=15, padx=15)

        self.string_selector = StringSelector(
            settings_frame,
            self.current_tuning.get_string_names(),
            self._on_string_change
        )
        self.string_selector.pack(pady=15, padx=15)

        display_frame = ctk.CTkFrame(self.root, fg_color="#1e1e1e", corner_radius=15)
        display_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.frequency_display = FrequencyDisplay(display_frame)
        self.frequency_display.pack(pady=15)
        self.frequency_display.update_target(self.current_tuning.get_frequency(self.current_string))

        self.tuning_meter = TuningMeterWidget(display_frame)
        self.tuning_meter.pack(pady=15, expand=True)

        control_frame = ctk.CTkFrame(self.root, fg_color="#1e1e1e", corner_radius=15)
        control_frame.pack(pady=10, padx=20, fill="x")

        self.control_buttons = ControlButtons(control_frame, self._on_start, self._on_stop)
        self.control_buttons.pack(pady=20)
    
    def _on_instrument_change(self, instrument_display_name: str):
        for inst in self.instrument_repository.get_all_instruments().values():
            if inst.full_display_name == instrument_display_name:
                self.current_instrument = inst

                self.frequency_detector = FFTFrequencyDetector(
                    sample_rate=self.stream_manager.sample_rate,
                    chunk_size=self.stream_manager.chunk_size,
                    min_frequency=inst.min_frequency,
                    max_frequency=inst.max_frequency
                )
                self.audio_processor.frequency_detector = self.frequency_detector

                tuning_names = inst.get_tuning_preset_names()
                self.tuning_selector.combo.configure(values=tuning_names)
                if tuning_names:
                    self.tuning_selector.set_tuning(tuning_names[0])
                    self.current_tuning = inst.get_preset(tuning_names[0])
                    self._update_string_selector()
                break

    def _on_tuning_change(self, tuning_name: str):
        preset = self.current_instrument.get_preset(tuning_name)
        if preset:
            self.current_tuning = preset
            self._update_string_selector()

    def _on_string_change(self, string_name: str):
        self.current_string = string_name
        target_freq = self.current_tuning.get_frequency(self.current_string)
        self.frequency_display.update_target(target_freq)
    
    def _on_custom_tuning_click(self):
        dialog = CustomTuningDialog(self.root, self.current_tuning.strings, self._apply_custom_tuning)
        dialog.show()
    
    def _apply_custom_tuning(self, custom_tuning: CustomTuning):
        self.current_tuning = custom_tuning
        self.tuning_selector.set_tuning("Custom Tuning")
        self._update_string_selector()
    
    def _update_string_selector(self):
        string_names = self.current_tuning.get_string_names()

        self.string_selector.update_strings(string_names)
        self.current_string = string_names[0]
        self.string_selector.set_string(self.current_string)

        target_freq = self.current_tuning.get_frequency(self.current_string)

        self.frequency_display.update_target(target_freq)
    
    def _on_start(self):
        if not self.audio_processor.start_processing():
            messagebox.showerror("Error", "Could not start audio input")
            self.control_buttons.enable_start()
            return
        
        self.is_running = True
        self.audio_thread = threading.Thread(target=self._audio_processing_loop)
        self.audio_thread.daemon = True
        self.audio_thread.start()
    
    def _on_stop(self):
        self.is_running = False
        self.audio_processor.stop_processing()
        
        self.frequency_display.update_frequency(None)
        self.tuning_meter.draw_meter(0)
    
    def _audio_processing_loop(self):
        while self.is_running:
            try:
                frequency = self.audio_processor.process_audio_frame()
                
                if frequency:
                    target_freq = self.current_tuning.get_frequency(self.current_string)
                    result = self.tuning_analyzer.analyze(frequency, target_freq)
                    
                    self.root.after(0, self._update_display, result)
            
            except Exception as e:
                print(f"Audio processing error: {e}")
            
            time.sleep(0.05)
    
    def _update_display(self, result):
        self.frequency_display.update_frequency(result.detected_frequency)
        self.tuning_meter.draw_meter(result.deviation)
    
    def _on_closing(self):
        self.is_running = False
        self.audio_processor.cleanup()
        self.root.destroy()
    
    def run(self):
        self.root.mainloop()


def main():
    app = GuitarTunerApp()
    app.run()


if __name__ == "__main__":
    main()
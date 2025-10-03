import customtkinter as ctk
from tkinter import messagebox
from typing import Optional

from models import TuningRepository, TuningPreset, CustomTuning, InstrumentRepository, Instrument, TunerState, NoteFrequencyConverter
from audio import AudioStreamManager, FFTFrequencyDetector, AudioProcessor, AudioThreadManager
from analysis import TuningAnalyzer, TuningStatus
from gui import (TuningMeterWidget, TuningSelector, StringSelector, FrequencyDisplay, ControlButtons, CustomTuningDialog, InstrumentSelector, SplashScreenManager)
from config import AudioConstants, TuningConstants, UIConstants, GUITAR_JOKES

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class GuitarTunerApp:
    def __init__(self, instrument_repository: InstrumentRepository, audio_processor: AudioProcessor, tuning_analyzer: TuningAnalyzer, note_converter: NoteFrequencyConverter):
        self.instrument_repository = instrument_repository
        self.audio_processor = audio_processor
        self.tuning_analyzer = tuning_analyzer
        self.note_converter = note_converter

        default_instrument = self.instrument_repository.get_default_instrument()
        default_tuning = list(default_instrument.get_tuning_presets().values())[0]
        self.state = TunerState(default_instrument, default_tuning)

        self.audio_thread_manager = AudioThreadManager(audio_processor=audio_processor, tuning_analyzer=tuning_analyzer, on_result_callback=self._on_tuning_result, get_target_frequency=lambda: self.state.get_current_frequency())

        self.root = ctk.CTk()
        self._setup_gui()

    def _setup_gui(self):
        self._setup_window()
        self._setup_header()
        self._setup_settings_panel()
        self._setup_display_panel()
        self._setup_control_panel()

    def _setup_window(self):
        self.root.title(UIConstants.WINDOW_TITLE)
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', lambda e: self.root.attributes('-fullscreen', False))
        self.root.bind('<F11>', lambda e: self.root.attributes('-fullscreen', True))
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _setup_header(self):
        header_frame = ctk.CTkFrame(self.root, fg_color="#1e1e1e", corner_radius=15)
        header_frame.pack(pady=20, padx=20, fill="x")

        title_label = ctk.CTkLabel(header_frame, text=UIConstants.WINDOW_TITLE, font=("Segoe UI", 42, "bold"), text_color="#00ff88")
        title_label.pack(pady=20)

        subtitle_label = ctk.CTkLabel(header_frame, text=UIConstants.WINDOW_SUBTITLE, font=("Segoe UI", 14), text_color="#888888")
        subtitle_label.pack(pady=(0, 15))

    def _setup_settings_panel(self):
        settings_frame = ctk.CTkFrame(self.root, fg_color="#1e1e1e", corner_radius=15)
        settings_frame.pack(pady=10, padx=20, fill="x")

        instrument_display_names = [
            inst.full_display_name
            for inst in self.instrument_repository.get_all_instruments().values()
        ]

        self.instrument_selector = InstrumentSelector(settings_frame, instrument_display_names, self._on_instrument_change)

        self.instrument_selector.pack(pady=15, padx=15)

        self.tuning_selector = TuningSelector(settings_frame, self.state.instrument.get_tuning_preset_names(), self._on_tuning_change, self._on_custom_tuning_click)

        self.tuning_selector.pack(pady=15, padx=15)

        self.string_selector = StringSelector(settings_frame, self.state.get_string_names(), self._on_string_change)
        self.string_selector.pack(pady=15, padx=15)

    def _setup_display_panel(self):
        display_frame = ctk.CTkFrame(self.root, fg_color="#1e1e1e", corner_radius=15)
        display_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.frequency_display = FrequencyDisplay(display_frame)
        self.frequency_display.pack(pady=15)
        self.frequency_display.update_target(self.state.get_current_frequency())

        self.tuning_meter = TuningMeterWidget(display_frame, width=UIConstants.TUNING_METER_WIDTH, height=UIConstants.TUNING_METER_HEIGHT)

        self.tuning_meter.pack(pady=15, expand=True)

    def _setup_control_panel(self):
        control_frame = ctk.CTkFrame(self.root, fg_color="#1e1e1e", corner_radius=15)
        control_frame.pack(pady=10, padx=20, fill="x")

        self.control_buttons = ControlButtons(control_frame, self._on_start, self._on_stop)
        self.control_buttons.pack(pady=20)
    
    def _on_instrument_change(self, instrument_display_name: str):
        for inst in self.instrument_repository.get_all_instruments().values():
            if inst.full_display_name == instrument_display_name:
                self.state.instrument = inst

                self.audio_processor.frequency_detector.set_frequency_range(inst.min_frequency, inst.max_frequency)

                tuning_names = inst.get_tuning_preset_names()
                self.tuning_selector.update_tunings(tuning_names)
                self.state.tuning = inst.get_preset(tuning_names[0])
                self._update_string_selector()
                break

    def _on_tuning_change(self, tuning_name: str):
        preset = self.state.instrument.get_preset(tuning_name)

        if preset:
            self.state.tuning = preset
            self._update_string_selector()

    def _on_string_change(self, string_name: str):
        self.state.current_string = string_name
        target_freq = self.state.get_current_frequency()
        self.frequency_display.update_target(target_freq)

    def _on_custom_tuning_click(self):
        dialog = CustomTuningDialog(self.root, self.state.tuning.strings, self._apply_custom_tuning, self.note_converter)
        dialog.show()

    def _apply_custom_tuning(self, custom_tuning: CustomTuning):
        self.state.tuning = custom_tuning
        self.tuning_selector.set_tuning("Custom Tuning")
        self._update_string_selector()

    def _update_string_selector(self):
        string_names = self.state.get_string_names()

        self.string_selector.update_strings(string_names)
        self.state.current_string = string_names[0]
        self.string_selector.set_string(self.state.current_string)

        target_freq = self.state.get_current_frequency()

        self.frequency_display.update_target(target_freq)
    
    def _on_start(self):
        if not self.audio_thread_manager.start():
            messagebox.showerror("Error", "Could not start audio input")
            self.control_buttons.enable_start()
            return

    def _on_stop(self):
        self.audio_thread_manager.stop()
        self.frequency_display.update_frequency(None)
        self.tuning_meter.draw_meter(0)

    def _on_tuning_result(self, result):
        self.root.after(0, self._update_display, result)

    def _update_display(self, result):
        self.frequency_display.update_frequency(result.detected_frequency)
        self.tuning_meter.draw_meter(result.deviation)
    
    def _on_closing(self):
        self.audio_thread_manager.stop()
        self.audio_processor.cleanup()
        self.root.destroy()
    
    def run(self):
        self.root.mainloop()


def main():
    import random

    splash = SplashScreenManager()
    splash.show()

    try:
        splash.update(0.1, random.choice(GUITAR_JOKES))
        instrument_repository = InstrumentRepository()
        default_instrument = instrument_repository.get_default_instrument()

        splash.update(0.3, random.choice(GUITAR_JOKES))
        stream_manager = AudioStreamManager(chunk_size=AudioConstants.CHUNK_SIZE, sample_rate=AudioConstants.SAMPLE_RATE)

        splash.update(0.5, random.choice(GUITAR_JOKES))
        frequency_detector = FFTFrequencyDetector(sample_rate=stream_manager.sample_rate, chunk_size=stream_manager.chunk_size, min_frequency=default_instrument.min_frequency, max_frequency=default_instrument.max_frequency)

        splash.update(0.6, random.choice(GUITAR_JOKES))
        audio_processor = AudioProcessor(stream_manager=stream_manager, frequency_detector=frequency_detector)

        splash.update(0.7, random.choice(GUITAR_JOKES))
        tuning_analyzer = TuningAnalyzer(in_tune_threshold=TuningConstants.IN_TUNE_THRESHOLD, close_threshold=TuningConstants.CLOSE_THRESHOLD)

        splash.update(0.8, random.choice(GUITAR_JOKES))
        note_converter = NoteFrequencyConverter()

        splash.update(0.9, random.choice(GUITAR_JOKES))
        app = GuitarTunerApp(instrument_repository=instrument_repository, audio_processor=audio_processor, tuning_analyzer=tuning_analyzer, note_converter=note_converter)

        splash.update(1.0, "Nothing is true, everything is permitted... to be in tune! 🗡️")
        splash.close()

        app.run()

    except Exception as exception:
        splash.close()
        raise exception


if __name__ == "__main__":
    main()
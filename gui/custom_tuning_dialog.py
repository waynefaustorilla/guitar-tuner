import customtkinter as ctk
from tkinter import messagebox
from typing import Dict, Callable

from models import CustomTuning, NoteFrequencyConverter, StringNameFormatter


class CustomTuningDialog:
    def __init__(self, parent, current_strings: Dict[str, float], on_apply: Callable[[CustomTuning], None], converter: NoteFrequencyConverter):
        self.parent = parent
        self.current_strings = current_strings.copy()
        self.on_apply = on_apply
        self.window = None
        self.converter = converter
        self.string_note_selectors = {}
    
    def show(self):
        self.window = ctk.CTkToplevel(self.parent)
        self.window.title("🎵 Custom Tuning")
        self.window.geometry("550x650")
        self.window.transient(self.parent)
        self.window.grab_set()

        self._create_widgets()
    
    def _create_widgets(self):
        ctk.CTkLabel(self.window, text="🎵 Custom Tuning Editor", font=("Segoe UI", 24, "bold"), text_color="#00ff88").pack(pady=20)
        ctk.CTkLabel(self.window, text="Select note and octave for each string:", font=("Segoe UI", 14)).pack(pady=10)

        self._create_string_selectors()
        self._create_buttons()

    def _create_string_selectors(self):
        selectors_frame = ctk.CTkScrollableFrame(self.window, fg_color="transparent")
        selectors_frame.pack(pady=10, padx=20, fill="both", expand=True)

        notes = self.converter.STANDARD_NOTES
        octaves = [str(i) for i in self.converter.OCTAVE_RANGE]

        for string_name, freq in self.current_strings.items():
            note, octave, _ = self.converter.frequency_to_note(freq)

            string_frame = ctk.CTkFrame(selectors_frame, fg_color="#2b2b2b")
            string_frame.pack(pady=10, padx=10, fill="x")

            label_frame = ctk.CTkFrame(string_frame, fg_color="transparent")
            label_frame.pack(side="left", padx=15, pady=15)

            ctk.CTkLabel(label_frame, text=f"String: {string_name}", font=("Segoe UI", 13, "bold"), anchor="w").pack()

            freq_label = ctk.CTkLabel(label_frame, text=f"({freq:.2f} Hz)", font=("Segoe UI", 11), text_color="#888888")
            freq_label.pack()

            selector_frame = ctk.CTkFrame(string_frame, fg_color="transparent")
            selector_frame.pack(side="right", padx=15, pady=15)

            ctk.CTkLabel(selector_frame, text="Note:", font=("Segoe UI", 12)).pack(side="left", padx=5)

            note_combo = ctk.CTkComboBox(selector_frame, values=notes, state="readonly", font=("Segoe UI", 12), width=80, command=lambda choice, sn=string_name, lbl=freq_label: self._update_frequency_display(sn, lbl))
            note_combo.set(note)
            note_combo.pack(side="left", padx=5)

            ctk.CTkLabel(selector_frame, text="Octave:", font=("Segoe UI", 12)).pack(side="left", padx=5)

            octave_combo = ctk.CTkComboBox(selector_frame, values=octaves, state="readonly", font=("Segoe UI", 12), width=70, command=lambda choice, sn=string_name, lbl=freq_label: self._update_frequency_display(sn, lbl))
            octave_combo.set(str(octave))
            octave_combo.pack(side="left", padx=5)

            self.string_note_selectors[string_name] = (note_combo, octave_combo, freq_label)
    
    def _create_buttons(self):
        button_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        button_frame.pack(pady=20)

        apply_btn = ctk.CTkButton(button_frame, text="✓ Apply", command=self._apply_custom_tuning, font=("Segoe UI", 14, "bold"), fg_color="#00aa66", hover_color="#008855", width=150)
        apply_btn.pack(side="left", padx=10)

        reset_btn = ctk.CTkButton(button_frame, text="↻ Reset to Standard", command=self._reset_to_standard, font=("Segoe UI", 14, "bold"), fg_color="#2b5278", hover_color="#1e3a5f", width=180)
        reset_btn.pack(side="left", padx=10)

        cancel_btn = ctk.CTkButton(button_frame, text="✕ Cancel", command=self.window.destroy, font=("Segoe UI", 14, "bold"), fg_color="#cc3333", hover_color="#aa2222", width=150)
        cancel_btn.pack(side="left", padx=10)
    
    def _update_frequency_display(self, string_name: str, freq_label: ctk.CTkLabel):
        note_combo, octave_combo, _ = self.string_note_selectors[string_name]
        note = note_combo.get()
        octave = int(octave_combo.get())

        try:
            freq = self.converter.note_to_frequency(note, octave)
            freq_label.configure(text=f"({freq:.2f} Hz)")

        except ValueError:
            freq_label.configure(text="(Invalid)")

    def _apply_custom_tuning(self):
        try:
            string_order = list(self.string_note_selectors.keys())
            note_octave_pairs = []

            for string_name in string_order:
                note_combo, octave_combo, _ = self.string_note_selectors[string_name]
                note = note_combo.get()
                octave = int(octave_combo.get())
                note_octave_pairs.append((note, octave))

            string_names = StringNameFormatter.create_unique_string_names(note_octave_pairs)

            new_strings = {}
            for i, internal_name in enumerate(string_names.keys()):
                note, octave = note_octave_pairs[i]
                freq = self.converter.note_to_frequency(note, octave)
                new_strings[internal_name] = freq

            custom_tuning = CustomTuning(new_strings)

            self.on_apply(custom_tuning)
            self.window.destroy()

        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
    
    def _reset_to_standard(self):
        standard_tuning = {
            'E (Low)': 82.41,
            'A': 110.00,
            'D': 146.83,
            'G': 196.00,
            'B': 246.94,
            'E (High)': 329.63
        }

        for string_name, (note_combo, octave_combo, freq_label) in self.string_note_selectors.items():
            if string_name in standard_tuning:
                freq = standard_tuning[string_name]
                note, octave, _ = self.converter.frequency_to_note(freq)
                note_combo.set(note)
                octave_combo.set(str(octave))
                freq_label.configure(text=f"({freq:.2f} Hz)")
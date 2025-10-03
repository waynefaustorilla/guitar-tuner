import customtkinter as ctk
from typing import Callable


class TuningSelector:
    def __init__(self, parent, tuning_names: list, on_tuning_change: Callable[[str], None], on_custom_click: Callable[[], None]):
        self.frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.on_tuning_change = on_tuning_change
        self.on_custom_click = on_custom_click

        label_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        label_frame.pack(fill="x")

        ctk.CTkLabel(label_frame, text="🎵", font=("Segoe UI", 20)).pack(side="left", padx=(0, 10))

        ctk.CTkLabel(label_frame, text="Tuning Configuration", font=("Segoe UI", 16, "bold"), text_color="#00ff88").pack(side="left")

        select_frame = ctk.CTkFrame(self.frame, fg_color="#2b2b2b", corner_radius=10)
        select_frame.pack(pady=10, fill="x")

        self.combo = ctk.CTkComboBox(select_frame, values=tuning_names, command=self._on_selection_changed, width=350, height=40, font=("Segoe UI", 15, "bold"), dropdown_font=("Segoe UI", 14), state="readonly", fg_color="#3d3d3d", button_color="#00ff88", button_hover_color="#00cc66", border_color="#00ff88", border_width=2)
        self.combo.set(tuning_names[0])
        self.combo.pack(side="left", padx=15, pady=15)

        custom_btn = ctk.CTkButton(select_frame, text="✏️ Custom", command=self.on_custom_click, width=120, height=40, font=("Segoe UI", 14, "bold"), fg_color="#5a2d5a", hover_color="#4a1d4a", corner_radius=10)
        custom_btn.pack(side="left", padx=15, pady=15)

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def _on_selection_changed(self, choice: str):
        self.on_tuning_change(choice)

    def set_tuning(self, tuning_name: str):
        self.combo.set(tuning_name)

    def get_current_tuning(self) -> str:
        return self.combo.get()

    def update_tunings(self, tuning_names: list):
        self.combo.configure(values=tuning_names)
        if tuning_names:
            self.set_tuning(tuning_names[0])
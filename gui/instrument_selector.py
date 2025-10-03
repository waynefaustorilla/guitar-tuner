import customtkinter as ctk
from typing import Callable, List


class InstrumentSelector:
    def __init__(self, parent, instrument_display_names: List[str], on_instrument_change: Callable[[str], None]):
        self.frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.on_instrument_change = on_instrument_change
        self.current_selection = instrument_display_names[0] if instrument_display_names else ""

        label_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        label_frame.pack(fill="x")

        ctk.CTkLabel(label_frame, text="🎸", font=("Segoe UI", 24)).pack(side="left", padx=(0, 10))

        ctk.CTkLabel(label_frame, text="Select Instrument", font=("Segoe UI", 16, "bold"), text_color="#00ff88").pack(side="left")

        button_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        button_frame.pack(pady=10, fill="x")

        self.buttons = {}

        colors = {
            "🎸 Acoustic Guitar": "#2d5a3d",
            "🎸 Electric Guitar": "#5a2d3d",
            "🎸 Bass Guitar": "#2d3d5a",
            "🎵 Ukulele": "#5a4d2d"
        }

        for i, name in enumerate(instrument_display_names):
            color = colors.get(name, "#2b5278")
            hover = self._darken_color(color)

            btn = ctk.CTkButton(button_frame, text=name, command=lambda n=name: self._on_button_click(n), font=("Segoe UI", 14, "bold"), fg_color=color, hover_color=hover, height=45, corner_radius=10)
            btn.pack(side="left", padx=5, expand=True, fill="x")
            self.buttons[name] = btn

        if instrument_display_names:
            self._highlight_button(instrument_display_names[0])

    def _darken_color(self, hex_color):
        hex_color = hex_color.lstrip('#')

        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        r, g, b = int(r * 0.7), int(g * 0.7), int(b * 0.7)

        return f'#{r:02x}{g:02x}{b:02x}'

    def _highlight_button(self, name):
        for btn_name, btn in self.buttons.items():
            if btn_name == name:
                btn.configure(border_width=3, border_color="#00ff88")

            else:
                btn.configure(border_width=0)

    def _on_button_click(self, name):
        self.current_selection = name
        self._highlight_button(name)
        self.on_instrument_change(name)

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def _on_selection_changed(self, choice: str):
        self.on_instrument_change(choice)

    def update_instruments(self, instrument_display_names: List[str]):
        pass

    def set_instrument(self, display_name: str):
        self.current_selection = display_name
        self._highlight_button(display_name)

    def get_current_instrument(self) -> str:
        return self.current_selection
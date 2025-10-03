import customtkinter as ctk
from typing import Callable

from models import StringNameFormatter


class StringSelector:
    def __init__(self, parent, string_names: list, on_string_change: Callable[[str], None]):
        self.frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.on_string_change = on_string_change
        self.string_names = string_names
        self.current_selection = string_names[0] if string_names else ""

        label_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        label_frame.pack(fill="x")

        ctk.CTkLabel(label_frame, text="🎼", font=("Segoe UI", 20)).pack(side="left", padx=(0, 10))

        ctk.CTkLabel(label_frame, text="String Selection", font=("Segoe UI", 16, "bold"), text_color="#00ff88").pack(side="left")

        self.button_container = ctk.CTkFrame(self.frame, fg_color="#2b2b2b", corner_radius=10)
        self.button_container.pack(pady=10, fill="x")

        self.buttons = {}
        self._create_string_buttons(string_names)

    def _get_display_name(self, internal_name):
        return StringNameFormatter.get_display_name(internal_name)

    def _create_string_buttons(self, string_names):
        for btn in self.buttons.values():
            btn.destroy()

        self.buttons.clear()

        colors = ["#3d2d5a", "#2d5a3d", "#5a3d2d", "#2d3d5a", "#5a2d3d", "#3d5a2d"]

        for i, name in enumerate(string_names):
            color = colors[i % len(colors)]
            hover = self._darken_color(color)
            display_name = self._get_display_name(name)

            btn = ctk.CTkButton(self.button_container, text=display_name, command=lambda n=name: self._on_button_click(n), font=("Segoe UI", 14, "bold"), fg_color=color, hover_color=hover, height=45, corner_radius=10)

            btn.pack(side="left", padx=5, pady=10, expand=True, fill="x")
            self.buttons[name] = btn

        if string_names:
            self._highlight_button(string_names[0])

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
        self.on_string_change(name)

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def _on_selection_changed(self, choice: str):
        self.on_string_change(choice)

    def update_strings(self, string_names: list):
        self.string_names = string_names
        self._create_string_buttons(string_names)

    def set_string(self, string_name: str):
        self.current_selection = string_name
        self._highlight_button(string_name)

    def get_current_string(self) -> str:
        return self.current_selection
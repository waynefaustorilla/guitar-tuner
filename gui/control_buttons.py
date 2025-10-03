import customtkinter as ctk
from typing import Callable


class ControlButtons:
    def __init__(self, parent, on_start: Callable[[], None], on_stop: Callable[[], None]):
        self.frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.on_start = on_start
        self.on_stop = on_stop

        self.start_button = ctk.CTkButton(self.frame, text="▶ Start Listening", command=self._handle_start, font=("Segoe UI", 16, "bold"), fg_color="#00aa66", hover_color="#008855", width=200, height=50)
        self.start_button.pack(side="left", padx=15)

        self.stop_button = ctk.CTkButton(self.frame, text="■ Stop", command=self._handle_stop, font=("Segoe UI", 16, "bold"), fg_color="#cc3333", hover_color="#aa2222", width=200, height=50, state="disabled")
        self.stop_button.pack(side="left", padx=15)

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def _handle_start(self):
        self.on_start()
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")

    def _handle_stop(self):
        self.on_stop()
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")

    def enable_start(self):
        self.start_button.configure(state="normal")

    def disable_start(self):
        self.start_button.configure(state="disabled")
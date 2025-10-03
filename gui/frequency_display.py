import customtkinter as ctk
from typing import Optional


class FrequencyDisplay:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent, fg_color="transparent")

        info_frame = ctk.CTkFrame(self.frame, fg_color="#2b2b2b", corner_radius=10)
        info_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(info_frame, text="Current Frequency", font=("Segoe UI", 12), text_color="#888888").pack(pady=(10, 0))
        self.freq_label = ctk.CTkLabel(info_frame, text="-- Hz", font=("Segoe UI", 56, "bold"), text_color="#888888")
        self.freq_label.pack(pady=5)

        separator = ctk.CTkFrame(info_frame, height=2, fg_color="#444444")
        separator.pack(fill="x", padx=40, pady=10)

        ctk.CTkLabel(info_frame, text="Target Frequency", font=("Segoe UI", 12), text_color="#888888").pack()
        self.target_label = ctk.CTkLabel(info_frame, text="-- Hz", font=("Segoe UI", 20, "bold"), text_color="#00ff88")
        self.target_label.pack(pady=(0, 15))

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def update_frequency(self, frequency: Optional[float]):
        if frequency is None:
            self.freq_label.configure(text="-- Hz", text_color="#888888")
        else:
            self.freq_label.configure(text=f"{frequency:.2f} Hz", text_color="#00ff88")

    def update_target(self, target_frequency: float):
        self.target_label.configure(text=f"{target_frequency:.2f} Hz")
import customtkinter as ctk


class StatusDisplay:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent, fg_color="#2b2b2b", corner_radius=15)
        self.icon_label = ctk.CTkLabel(self.frame, text="🎵", font=("Segoe UI", 32))
        self.icon_label.pack(pady=(15, 5))
        self.label = ctk.CTkLabel(self.frame, text="Click 'Start' to begin tuning", font=("Segoe UI", 20, "bold"), text_color="#888888")
        self.label.pack(pady=(5, 15))

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def update_status(self, message: str, color: str = '#888888'):
        self.label.configure(text=message, text_color=color)

        if "IN TUNE" in message:
            self.icon_label.configure(text="✅")

        elif "HIGH" in message or "LOW" in message:
            self.icon_label.configure(text="⚠️")

        elif "Stopped" in message:
            self.icon_label.configure(text="⏸️")

        elif "Listening" in message:
            self.icon_label.configure(text="🎤")

        else:
            self.icon_label.configure(text="🎵")
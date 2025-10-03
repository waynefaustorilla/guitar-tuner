import customtkinter as ctk
import tkinter as tk
from typing import Optional


class SplashScreen:
    def __init__(self, parent=None):
        self.parent = parent
        self.window: Optional[tk.Toplevel] = None
        self.progress_bar: Optional[ctk.CTkProgressBar] = None
        self.status_label: Optional[ctk.CTkLabel] = None
        self.progress_value = 0.0

    def show(self):
        """Display the splash screen"""
        # Create a simple Tkinter window for splash
        self.window = tk.Tk() if self.parent is None else tk.Toplevel(self.parent)
        self.window.title("")
        self.window.overrideredirect(True)  # Remove window decorations
        self.window.configure(bg="#1a1a1a")
        
        # Set window size and center it
        window_width = 700
        window_height = 300
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Main frame
        main_frame = tk.Frame(
            self.window,
            bg="#1a1a1a",
            highlightbackground="#00ff88",
            highlightthickness=2
        )
        main_frame.pack(fill="both", expand=True, padx=2, pady=2)

        # Logo/Icon
        icon_label = tk.Label(
            main_frame,
            text="🎸",
            font=("Segoe UI", 50),
            bg="#1a1a1a",
            fg="#00ff88"
        )
        icon_label.pack(pady=(20, 5))

        # App title
        title_label = tk.Label(
            main_frame,
            text="Guitar Tuner Pro",
            font=("Segoe UI", 28, "bold"),
            bg="#1a1a1a",
            fg="#00ff88"
        )
        title_label.pack(pady=(0, 3))

        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Professional Instrument Tuning",
            font=("Segoe UI", 11),
            bg="#1a1a1a",
            fg="#888888"
        )
        subtitle_label.pack(pady=(0, 15))

        # Progress bar frame
        progress_frame = tk.Frame(main_frame, bg="#2b2b2b", height=8, width=550)
        progress_frame.pack(pady=(0, 8))
        progress_frame.pack_propagate(False)

        self.progress_bar = tk.Canvas(
            progress_frame,
            bg="#2b2b2b",
            height=8,
            width=550,
            highlightthickness=0
        )
        self.progress_bar.pack(fill="both", expand=True)

        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Initializing...",
            font=("Segoe UI", 10),
            bg="#1a1a1a",
            fg="#888888"
        )
        self.status_label.pack(pady=(0, 8))

        # Version/Credits
        credits_label = tk.Label(
            main_frame,
            text="Powered by Espresso Assassino (Orlie Wayne Faustorilla) ☕ | v1.0",
            font=("Segoe UI", 9),
            bg="#1a1a1a",
            fg="#666666"
        )
        credits_label.pack(pady=(0, 8))
        
        self.window.update()
    
    def update_progress(self, value: float, status: str = ""):
        """Update progress bar and status text

        Args:
            value: Progress value between 0.0 and 1.0
            status: Status message to display
        """
        if self.progress_bar and self.window:
            self.progress_value = min(1.0, max(0.0, value))

            # Draw progress bar
            self.progress_bar.delete("all")
            bar_width = int(550 * self.progress_value)
            self.progress_bar.create_rectangle(
                0, 0, bar_width, 10,
                fill="#00ff88",
                outline=""
            )

            if status and self.status_label:
                self.status_label.configure(text=status)

            self.window.update()
    
    def close(self):
        """Close the splash screen"""
        if self.window:
            self.window.destroy()
            self.window = None


class SplashScreenManager:
    """Manager for showing splash screen during initialization"""
    
    def __init__(self):
        self.splash: Optional[SplashScreen] = None
        self.is_showing = False
    
    def show(self):
        """Show splash screen in main thread"""
        self.splash = SplashScreen()
        self.splash.show()
        self.is_showing = True
    
    def update(self, progress: float, status: str):
        """Update splash screen progress"""
        if self.splash and self.is_showing:
            self.splash.update_progress(progress, status)
    
    def close(self):
        """Close splash screen"""
        if self.splash and self.is_showing:
            self.splash.close()
            self.is_showing = False
            self.splash = None
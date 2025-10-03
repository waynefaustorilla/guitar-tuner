import customtkinter as ctk
import tkinter as tk
import math


class TuningMeterWidget:
    def __init__(self, parent, width: int = 600, height: int = 350):
        self.frame = ctk.CTkFrame(parent, fg_color="#1e1e1e", corner_radius=15)
        self.canvas = tk.Canvas(self.frame, width=width, height=height, bg='#1e1e1e', highlightthickness=0)
        self.canvas.pack(padx=20, pady=20)
        self.width = width
        self.height = height
        self.current_deviation = 0
        self.animation_step = 0
        self.draw_meter()

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def draw_meter(self, deviation: float = 0):
        self.current_deviation = deviation
        self.canvas.delete("all")

        center_x = self.width // 2
        center_y = self.height - 80
        radius = 180

        start_angle = 180
        end_angle = 0

        for angle_deg in range(start_angle, end_angle - 1, -2):
            angle_rad = math.radians(angle_deg)
            x1 = center_x + (radius - 15) * math.cos(angle_rad)
            y1 = center_y - (radius - 15) * math.sin(angle_rad)
            x2 = center_x + radius * math.cos(angle_rad)
            y2 = center_y - radius * math.sin(angle_rad)

            normalized_pos = (angle_deg - 180) / 180

            if abs(normalized_pos) < 0.15:
                color = '#00ff88'
                width = 4

            elif abs(normalized_pos) < 0.4:
                color = '#88ff44'
                width = 3

            elif abs(normalized_pos) < 0.6:
                color = '#ffaa00'
                width = 3

            else:
                color = '#ff3333'
                width = 3

            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)

        for i in range(-5, 6):
            angle_deg = 180 - (i * 18)
            angle_rad = math.radians(angle_deg)
            x1 = center_x + (radius - 20) * math.cos(angle_rad)
            y1 = center_y - (radius - 20) * math.sin(angle_rad)
            x2 = center_x + (radius + 5) * math.cos(angle_rad)
            y2 = center_y - (radius + 5) * math.sin(angle_rad)

            self.canvas.create_line(x1, y1, x2, y2, fill='#ffffff', width=2)

            if i != 0:
                label_x = center_x + (radius + 35) * math.cos(angle_rad)
                label_y = center_y - (radius + 35) * math.sin(angle_rad)
                self.canvas.create_text(label_x, label_y, text=f"{i*10}", fill='#888888', font=('Segoe UI', 12, 'bold'))

        self.canvas.create_text(center_x, 25, text="PERFECT", fill='#00ff88', font=('Segoe UI', 18, 'bold'))

        clamped_deviation = max(-50, min(50, deviation))
        needle_angle_deg = 180 - (clamped_deviation / 50 * 90)
        needle_angle_rad = math.radians(needle_angle_deg)

        if abs(deviation) < 3:
            needle_color = '#00ff88'
            glow_color = '#00ff88'
            glow_radius = 15

        elif abs(deviation) < 10:
            needle_color = '#ffaa00'
            glow_color = '#ffaa00'
            glow_radius = 12

        else:
            needle_color = '#ff3333'
            glow_color = '#ff3333'
            glow_radius = 10

        for i in range(3, 0, -1):
            glow_r = glow_radius * (i / 3)
            self.canvas.create_oval(center_x - glow_r, center_y - glow_r, center_x + glow_r, center_y + glow_r, fill='', outline=glow_color, width=2)

        needle_length = radius - 10
        needle_x = center_x + needle_length * math.cos(needle_angle_rad)
        needle_y = center_y - needle_length * math.sin(needle_angle_rad)

        base_offset = 8
        base_angle1 = needle_angle_rad + math.pi / 2
        base_angle2 = needle_angle_rad - math.pi / 2
        base_x1 = center_x + base_offset * math.cos(base_angle1)
        base_y1 = center_y - base_offset * math.sin(base_angle1)
        base_x2 = center_x + base_offset * math.cos(base_angle2)
        base_y2 = center_y - base_offset * math.sin(base_angle2)

        self.canvas.create_polygon(needle_x, needle_y, base_x1, base_y1, base_x2, base_y2, fill=needle_color, outline='#ffffff', width=2)

        self.canvas.create_oval(center_x - 10, center_y - 10, center_x + 10, center_y + 10, fill=needle_color, outline='#ffffff', width=3)

        if abs(deviation) > 0.5:
            sign = "+" if deviation > 0 else ""
            status_text = f"{sign}{deviation:.1f} Hz"

            if abs(deviation) < 3:
                status_msg = "IN TUNE!"
                msg_color = '#00ff88'

            elif abs(deviation) < 10:
                status_msg = "CLOSE"
                msg_color = '#ffaa00'

            else:
                status_msg = "TUNE " + ("UP ↑" if deviation > 0 else "DOWN ↓")
                msg_color = '#ff3333'

            self.canvas.create_text(center_x, center_y + 40, text=status_msg, fill=msg_color, font=('Segoe UI', 22, 'bold'))
            self.canvas.create_text(center_x, center_y + 70, text=status_text, fill=needle_color, font=('Segoe UI', 18, 'bold'))
        else:
            self.canvas.create_text(center_x, center_y + 40, text="READY", fill='#888888', font=('Segoe UI', 22, 'bold'))
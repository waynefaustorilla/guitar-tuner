import customtkinter as ctk
import tkinter as tk
import math
from config import UIConstants


class TuningMeterWidget:
    # Color thresholds
    IN_TUNE_THRESHOLD = 0.15
    CLOSE_THRESHOLD = 0.4
    MODERATE_THRESHOLD = 0.6

    # Colors
    COLOR_IN_TUNE = '#00ff88'
    COLOR_CLOSE = '#88ff44'
    COLOR_MODERATE = '#ffaa00'
    COLOR_OUT_OF_TUNE = '#ff3333'
    COLOR_MARKER = '#ffffff'

    # Dimensions
    RADIUS_OFFSET = 15
    MARKER_INNER_OFFSET = 20
    MARKER_OUTER_OFFSET = 5
    LABEL_OFFSET = 35

    def __init__(self, parent, width: int = 600, height: int = 350):
        self.frame = ctk.CTkFrame(parent, fg_color="#1e1e1e", corner_radius=15)
        self.canvas = tk.Canvas(self.frame, width=width, height=height, bg='#1e1e1e', highlightthickness=0)
        self.canvas.pack(padx=20, pady=20)
        self.width = width
        self.height = height
        self.current_deviation = 0
        self.animation_step = 0
        self.center_x = self.width // 2
        self.center_y = self.height - UIConstants.TUNING_METER_CENTER_Y_OFFSET
        self.radius = UIConstants.TUNING_METER_RADIUS
        self.draw_meter()

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def draw_meter(self, deviation: float = 0):
        self.current_deviation = deviation
        self.canvas.delete("all")

        self._draw_arc_segments()
        self._draw_scale_markers()
        self._draw_needle()
        self._draw_status_text()

    def _get_color_and_width(self, normalized_pos: float) -> tuple:
        abs_pos = abs(normalized_pos)

        if abs_pos < self.IN_TUNE_THRESHOLD:
            return self.COLOR_IN_TUNE, 4
        elif abs_pos < self.CLOSE_THRESHOLD:
            return self.COLOR_CLOSE, 3
        elif abs_pos < self.MODERATE_THRESHOLD:
            return self.COLOR_MODERATE, 3
        else:
            return self.COLOR_OUT_OF_TUNE, 3

    def _draw_arc_segments(self):
        start_angle = 180
        end_angle = 0

        for angle_deg in range(start_angle, end_angle - 1, -2):
            angle_rad = math.radians(angle_deg)
            x1 = self.center_x + (self.radius - self.RADIUS_OFFSET) * math.cos(angle_rad)
            y1 = self.center_y - (self.radius - self.RADIUS_OFFSET) * math.sin(angle_rad)
            x2 = self.center_x + self.radius * math.cos(angle_rad)
            y2 = self.center_y - self.radius * math.sin(angle_rad)

            normalized_pos = (angle_deg - 180) / 180
            color, width = self._get_color_and_width(normalized_pos)

            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)

    def _draw_scale_markers(self):
        for i in range(-5, 6):
            angle_deg = 180 - (i * 18)
            angle_rad = math.radians(angle_deg)
            x1 = self.center_x + (self.radius - self.MARKER_INNER_OFFSET) * math.cos(angle_rad)
            y1 = self.center_y - (self.radius - self.MARKER_INNER_OFFSET) * math.sin(angle_rad)
            x2 = self.center_x + (self.radius + self.MARKER_OUTER_OFFSET) * math.cos(angle_rad)
            y2 = self.center_y - (self.radius + self.MARKER_OUTER_OFFSET) * math.sin(angle_rad)

            self.canvas.create_line(x1, y1, x2, y2, fill=self.COLOR_MARKER, width=2)

            if i != 0:
                label_x = self.center_x + (self.radius + self.LABEL_OFFSET) * math.cos(angle_rad)
                label_y = self.center_y - (self.radius + self.LABEL_OFFSET) * math.sin(angle_rad)
                self.canvas.create_text(
                    label_x, label_y,
                    text=f"{i*10}",
                    fill='#888888',
                    font=('Segoe UI', 12, 'bold')
                )

        self.canvas.create_text(
            self.center_x, 25,
            text="PERFECT",
            fill=self.COLOR_IN_TUNE,
            font=('Segoe UI', 18, 'bold')
        )

    def _get_needle_color_and_glow(self, deviation: float) -> tuple:
        abs_dev = abs(deviation)

        if abs_dev < 3:
            return self.COLOR_IN_TUNE, self.COLOR_IN_TUNE, 15
        elif abs_dev < 10:
            return self.COLOR_MODERATE, self.COLOR_MODERATE, 12
        else:
            return self.COLOR_OUT_OF_TUNE, self.COLOR_OUT_OF_TUNE, 10

    def _draw_needle(self):
        clamped_deviation = max(-50, min(50, self.current_deviation))
        needle_angle_deg = 180 - (clamped_deviation / 50 * 90)
        needle_angle_rad = math.radians(needle_angle_deg)

        needle_color, glow_color, glow_radius = self._get_needle_color_and_glow(self.current_deviation)

        # Draw glow effect
        for i in range(3, 0, -1):
            glow_r = glow_radius * (i / 3)
            self.canvas.create_oval(
                self.center_x - glow_r,
                self.center_y - glow_r,
                self.center_x + glow_r,
                self.center_y + glow_r,
                fill='',
                outline=glow_color,
                width=2
            )

        # Draw needle
        needle_length = self.radius - 10
        needle_x = self.center_x + needle_length * math.cos(needle_angle_rad)
        needle_y = self.center_y - needle_length * math.sin(needle_angle_rad)

        base_offset = 8
        base_angle1 = needle_angle_rad + math.pi / 2
        base_angle2 = needle_angle_rad - math.pi / 2
        base_x1 = self.center_x + base_offset * math.cos(base_angle1)
        base_y1 = self.center_y - base_offset * math.sin(base_angle1)
        base_x2 = self.center_x + base_offset * math.cos(base_angle2)
        base_y2 = self.center_y - base_offset * math.sin(base_angle2)

        self.canvas.create_polygon(
            needle_x, needle_y,
            base_x1, base_y1,
            base_x2, base_y2,
            fill=needle_color,
            outline=self.COLOR_MARKER,
            width=2
        )

        # Draw center circle
        self.canvas.create_oval(
            self.center_x - 10,
            self.center_y - 10,
            self.center_x + 10,
            self.center_y + 10,
            fill=needle_color,
            outline=self.COLOR_MARKER,
            width=3
        )

    def _get_status_message_and_color(self, deviation: float) -> tuple:
        abs_dev = abs(deviation)

        if abs_dev < 3:
            return "IN TUNE!", self.COLOR_IN_TUNE
        elif abs_dev < 10:
            return "CLOSE", self.COLOR_MODERATE
        else:
            direction = "UP ↑" if deviation > 0 else "DOWN ↓"
            return f"TUNE {direction}", self.COLOR_OUT_OF_TUNE

    def _draw_status_text(self):
        if abs(self.current_deviation) > 0.5:
            sign = "+" if self.current_deviation > 0 else ""
            status_text = f"{sign}{self.current_deviation:.1f} Hz"

            status_msg, msg_color = self._get_status_message_and_color(self.current_deviation)
            needle_color, _, _ = self._get_needle_color_and_glow(self.current_deviation)

            self.canvas.create_text(
                self.center_x,
                self.center_y + 40,
                text=status_msg,
                fill=msg_color,
                font=('Segoe UI', 22, 'bold')
            )
            self.canvas.create_text(
                self.center_x,
                self.center_y + 70,
                text=status_text,
                fill=needle_color,
                font=('Segoe UI', 18, 'bold')
            )
        else:
            self.canvas.create_text(
                self.center_x,
                self.center_y + 40,
                text="READY",
                fill='#888888',
                font=('Segoe UI', 22, 'bold')
            )
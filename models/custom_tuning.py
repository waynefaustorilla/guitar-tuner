from typing import Dict
from .tuning_preset import TuningPreset


class CustomTuning(TuningPreset):
    def __init__(self, strings: Dict[str, float]):
        super().__init__("Custom Tuning", strings)
    
    def update_string_frequency(self, string_name: str, frequency: float):
        if 20 <= frequency <= 2000:
            self._strings[string_name] = frequency

        else:
            raise ValueError(f"Frequency must be between 20 and 2000 Hz")
    
    def update_all_strings(self, strings: Dict[str, float]):
        for string_name, frequency in strings.items():
            if frequency < 20 or frequency > 2000:
                raise ValueError(f"Frequency for {string_name} must be between 20 and 2000 Hz")

        self._strings = strings.copy()

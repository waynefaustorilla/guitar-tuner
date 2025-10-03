from typing import Dict, List
from .tuning_preset import TuningPreset


class Instrument:
    def __init__(self, name: str, display_name: str, icon: str, min_frequency: float, max_frequency: float, tuning_presets: Dict[str, TuningPreset]):
        self._name = name
        self._display_name = display_name
        self._icon = icon
        self._min_frequency = min_frequency
        self._max_frequency = max_frequency
        self._tuning_presets = tuning_presets

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def display_name(self) -> str:
        return self._display_name
    
    @property
    def icon(self) -> str:
        return self._icon
    
    @property
    def full_display_name(self) -> str:
        return f"{self._icon} {self._display_name}"
    
    @property
    def min_frequency(self) -> float:
        return self._min_frequency
    
    @property
    def max_frequency(self) -> float:
        return self._max_frequency
    
    def get_tuning_presets(self) -> Dict[str, TuningPreset]:
        return self._tuning_presets.copy()
    
    def get_tuning_preset_names(self) -> List[str]:
        return list(self._tuning_presets.keys())
    
    def get_preset(self, name: str) -> TuningPreset:
        return self._tuning_presets.get(name)
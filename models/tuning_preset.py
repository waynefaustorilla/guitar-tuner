from typing import Dict


class TuningPreset:
    def __init__(self, name: str, strings: Dict[str, float]):
        self._name = name
        self._strings = strings.copy()
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def strings(self) -> Dict[str, float]:
        return self._strings.copy()
    
    def get_frequency(self, string_name: str) -> float:
        return self._strings.get(string_name, 0.0)
    
    def get_string_names(self) -> list:
        return list(self._strings.keys())

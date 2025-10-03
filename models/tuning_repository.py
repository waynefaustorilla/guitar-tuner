from typing import Dict
from .tuning_preset import TuningPreset


class TuningRepository:
    def __init__(self):
        self._presets = self._initialize_presets()
    
    def _initialize_presets(self) -> Dict[str, TuningPreset]:
        return {
            'Standard (E A D G B E)': TuningPreset(
                'Standard (E A D G B E)',
                {
                    'E (Low)': 82.41,
                    'A': 110.00,
                    'D': 146.83,
                    'G': 196.00,
                    'B': 246.94,
                    'E (High)': 329.63
                }
            ),
            'Drop D (D A D G B E)': TuningPreset(
                'Drop D (D A D G B E)',
                {
                    'D (Low)': 73.42,
                    'A': 110.00,
                    'D': 146.83,
                    'G': 196.00,
                    'B': 246.94,
                    'E (High)': 329.63
                }
            ),
            'Drop C (C G C F A D)': TuningPreset(
                'Drop C (C G C F A D)',
                {
                    'C (Low)': 65.41,
                    'G': 98.00,
                    'C': 130.81,
                    'F': 174.61,
                    'A': 220.00,
                    'D (High)': 293.66
                }
            ),
            'Half Step Down (Eb Ab Db Gb Bb Eb)': TuningPreset(
                'Half Step Down (Eb Ab Db Gb Bb Eb)',
                {
                    'Eb (Low)': 77.78,
                    'Ab': 103.83,
                    'Db': 138.59,
                    'Gb': 185.00,
                    'Bb': 233.08,
                    'Eb (High)': 311.13
                }
            ),
            'Open G (D G D G B D)': TuningPreset(
                'Open G (D G D G B D)',
                {
                    'D (Low)': 73.42,
                    'G': 98.00,
                    'D': 146.83,
                    'G (High)': 196.00,
                    'B': 246.94,
                    'D (High)': 293.66
                }
            ),
            'Open D (D A D F# A D)': TuningPreset(
                'Open D (D A D F# A D)',
                {
                    'D (Low)': 73.42,
                    'A': 110.00,
                    'D': 146.83,
                    'F#': 185.00,
                    'A (High)': 220.00,
                    'D (High)': 293.66
                }
            ),
            'DADGAD (D A D G A D)': TuningPreset(
                'DADGAD (D A D G A D)',
                {
                    'D (Low)': 73.42,
                    'A': 110.00,
                    'D': 146.83,
                    'G': 196.00,
                    'A (High)': 220.00,
                    'D (High)': 293.66
                }
            )
        }
    
    def get_preset(self, name: str) -> TuningPreset:
        return self._presets.get(name)
    
    def get_all_preset_names(self) -> list:
        return list(self._presets.keys())
    
    def get_default_preset(self) -> TuningPreset:
        return self._presets['Standard (E A D G B E)']
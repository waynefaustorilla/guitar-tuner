from typing import Dict
from .tuning_preset import TuningPreset
from config import NoteFrequencies as NF


class TuningRepository:
    def __init__(self):
        self._presets = self._initialize_presets()

    def _initialize_presets(self) -> Dict[str, TuningPreset]:
        return {
            'Standard (E A D G B E)': TuningPreset(
                'Standard (E A D G B E)',
                {
                    'E (Low)': NF.E2,
                    'A': NF.A2,
                    'D': NF.D3,
                    'G': NF.G3,
                    'B': NF.B3,
                    'E (High)': NF.E4
                }
            ),
            'Drop D (D A D G B E)': TuningPreset(
                'Drop D (D A D G B E)',
                {
                    'D (Low)': NF.D2,
                    'A': NF.A2,
                    'D': NF.D3,
                    'G': NF.G3,
                    'B': NF.B3,
                    'E (High)': NF.E4
                }
            ),
            'Drop C (C G C F A D)': TuningPreset(
                'Drop C (C G C F A D)',
                {
                    'C (Low)': NF.C2,
                    'G': NF.G2,
                    'C': NF.C3,
                    'F': NF.F3,
                    'A': NF.A3,
                    'D (High)': NF.D4
                }
            ),
            'Half Step Down (Eb Ab Db Gb Bb Eb)': TuningPreset(
                'Half Step Down (Eb Ab Db Gb Bb Eb)',
                {
                    'Eb (Low)': NF.Eb2,
                    'Ab': NF.Ab3,
                    'Db': NF.Db3,
                    'Gb': NF.Gb3,
                    'Bb': NF.Bb3,
                    'Eb (High)': NF.Eb4
                }
            ),
            'Open G (D G D G B D)': TuningPreset(
                'Open G (D G D G B D)',
                {
                    'D (Low)': NF.D2,
                    'G': NF.G2,
                    'D': NF.D3,
                    'G (High)': NF.G3,
                    'B': NF.B3,
                    'D (High)': NF.D4
                }
            ),
            'Open D (D A D F# A D)': TuningPreset(
                'Open D (D A D F# A D)',
                {
                    'D (Low)': NF.D2,
                    'A': NF.A2,
                    'D': NF.D3,
                    'F#': NF.Gb3,
                    'A (High)': NF.A3,
                    'D (High)': NF.D4
                }
            ),
            'DADGAD (D A D G A D)': TuningPreset(
                'DADGAD (D A D G A D)',
                {
                    'D (Low)': NF.D2,
                    'A': NF.A2,
                    'D': NF.D3,
                    'G': NF.G3,
                    'A (High)': NF.A3,
                    'D (High)': NF.D4
                }
            )
        }
    
    def get_preset(self, name: str) -> TuningPreset:
        return self._presets.get(name)
    
    def get_all_preset_names(self) -> list:
        return list(self._presets.keys())
    
    def get_default_preset(self) -> TuningPreset:
        return self._presets['Standard (E A D G B E)']
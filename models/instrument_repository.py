from typing import Dict, List
from .instrument import Instrument
from .tuning_preset import TuningPreset
from config import NoteFrequencies as NF


class InstrumentRepository:
    def __init__(self):
        self._instruments = self._initialize_instruments()

    def _initialize_instruments(self) -> Dict[str, Instrument]:
        return {
            'acoustic_guitar': self._create_acoustic_guitar(),
            'electric_guitar': self._create_electric_guitar(),
            'bass': self._create_bass(),
            'ukulele': self._create_ukulele()
        }

    def _create_acoustic_guitar(self) -> Instrument:
        tunings = {
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
            ),
            'Open G (D G D G B D)': TuningPreset(
                'Open G (D G D G B D)',
                {
                    'D (Low)': NF.D2,
                    'G': NF.G2,
                    'D': NF.D3,
                    'G (Mid)': NF.G3,
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
            )
        }

        return Instrument(name='acoustic_guitar', display_name='Acoustic Guitar', icon='🎸', min_frequency=70.0, max_frequency=400.0, tuning_presets=tunings)
    
    def _create_electric_guitar(self) -> Instrument:
        tunings = {
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
            'Drop B (B F# B E G# C#)': TuningPreset(
                'Drop B (B F# B E G# C#)',
                {
                    'B (Low)': NF.B1,
                    'F#': NF.Gb2,
                    'B': NF.B2,
                    'E': NF.E3,
                    'G#': NF.Ab3,
                    'C# (High)': NF.Db4
                }
            )
        }

        return Instrument(name='electric_guitar', display_name='Electric Guitar', icon='🎸', min_frequency=60.0, max_frequency=400.0, tuning_presets=tunings)
    
    def _create_bass(self) -> Instrument:
        tunings = {
            'Standard 4-String (E A D G)': TuningPreset(
                'Standard 4-String (E A D G)',
                {
                    'E (Low)': NF.E1,
                    'A': NF.A1,
                    'D': NF.D2,
                    'G': NF.G2
                }
            ),
            'Drop D (D A D G)': TuningPreset(
                'Drop D (D A D G)',
                {
                    'D (Low)': NF.D1,
                    'A': NF.A1,
                    'D': NF.D2,
                    'G': NF.G2
                }
            ),
            'Standard 5-String (B E A D G)': TuningPreset(
                'Standard 5-String (B E A D G)',
                {
                    'B (Low)': NF.B0,
                    'E': NF.E1,
                    'A': NF.A1,
                    'D': NF.D2,
                    'G': NF.G2
                }
            ),
            'Tenor (A D G C)': TuningPreset(
                'Tenor (A D G C)',
                {
                    'A (Low)': NF.A1,
                    'D': NF.D2,
                    'G': NF.G2,
                    'C': NF.C3
                }
            )
        }

        return Instrument(name='bass', display_name='Bass Guitar', icon='🎸', min_frequency=30.0, max_frequency=150.0, tuning_presets=tunings)

    def _create_ukulele(self) -> Instrument:
        tunings = {
            'Standard (G C E A)': TuningPreset(
                'Standard (G C E A)',
                {
                    'G': NF.G4,
                    'C': NF.C4,
                    'E': NF.E4,
                    'A': NF.A4
                }
            ),
            'Low G (G C E A)': TuningPreset(
                'Low G (G C E A)',
                {
                    'G (Low)': NF.G3,
                    'C': NF.C4,
                    'E': NF.E4,
                    'A': NF.A4
                }
            ),
            'Baritone (D G B E)': TuningPreset(
                'Baritone (D G B E)',
                {
                    'D': NF.D3,
                    'G': NF.G3,
                    'B': NF.B3,
                    'E': NF.E4
                }
            ),
            'D Tuning (A D F# B)': TuningPreset(
                'D Tuning (A D F# B)',
                {
                    'A': NF.A4,
                    'D': NF.D4,
                    'F#': NF.Gb4,
                    'B': NF.B4
                }
            )
        }
        
        return Instrument(name='ukulele', display_name='Ukulele', icon='🎵', min_frequency=140.0, max_frequency=550.0, tuning_presets=tunings)
    
    def get_all_instruments(self) -> Dict[str, Instrument]:
        return self._instruments.copy()
    
    def get_instrument_names(self) -> List[str]:
        return list(self._instruments.keys())
    
    def get_instrument(self, name: str) -> Instrument:
        return self._instruments.get(name)

    def get_default_instrument(self) -> Instrument:
        return self._instruments['acoustic_guitar']
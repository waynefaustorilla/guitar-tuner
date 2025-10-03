from typing import Dict, List
from .instrument import Instrument
from .tuning_preset import TuningPreset


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
            ),
            'Open G (D G D G B D)': TuningPreset(
                'Open G (D G D G B D)',
                {
                    'D (Low)': 73.42,
                    'G': 98.00,
                    'D': 146.83,
                    'G (Mid)': 196.00,
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
            )
        }
        
        return Instrument(name='acoustic_guitar', display_name='Acoustic Guitar', icon='🎸', min_frequency=70.0, max_frequency=400.0, tuning_presets=tunings)
    
    def _create_electric_guitar(self) -> Instrument:
        tunings = {
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
            'Drop B (B F# B E G# C#)': TuningPreset(
                'Drop B (B F# B E G# C#)',
                {
                    'B (Low)': 61.74,
                    'F#': 92.50,
                    'B': 123.47,
                    'E': 164.81,
                    'G#': 207.65,
                    'C# (High)': 277.18
                }
            )
        }
        
        return Instrument(name='electric_guitar', display_name='Electric Guitar', icon='🎸', min_frequency=60.0, max_frequency=400.0, tuning_presets=tunings)
    
    def _create_bass(self) -> Instrument:
        tunings = {
            'Standard 4-String (E A D G)': TuningPreset(
                'Standard 4-String (E A D G)',
                {
                    'E (Low)': 41.20,
                    'A': 55.00,
                    'D': 73.42,
                    'G': 98.00
                }
            ),
            'Drop D (D A D G)': TuningPreset(
                'Drop D (D A D G)',
                {
                    'D (Low)': 36.71,
                    'A': 55.00,
                    'D': 73.42,
                    'G': 98.00
                }
            ),
            'Standard 5-String (B E A D G)': TuningPreset(
                'Standard 5-String (B E A D G)',
                {
                    'B (Low)': 30.87,
                    'E': 41.20,
                    'A': 55.00,
                    'D': 73.42,
                    'G': 98.00
                }
            ),
            'Tenor (A D G C)': TuningPreset(
                'Tenor (A D G C)',
                {
                    'A (Low)': 55.00,
                    'D': 73.42,
                    'G': 98.00,
                    'C': 130.81
                }
            )
        }
        
        return Instrument(name='bass', display_name='Bass Guitar', icon='🎸', min_frequency=30.0, max_frequency=150.0, tuning_presets=tunings)
    
    def _create_ukulele(self) -> Instrument:
        tunings = {
            'Standard (G C E A)': TuningPreset(
                'Standard (G C E A)',
                {
                    'G': 392.00,
                    'C': 261.63,
                    'E': 329.63,
                    'A': 440.00
                }
            ),
            'Low G (G C E A)': TuningPreset(
                'Low G (G C E A)',
                {
                    'G (Low)': 196.00,
                    'C': 261.63,
                    'E': 329.63,
                    'A': 440.00
                }
            ),
            'Baritone (D G B E)': TuningPreset(
                'Baritone (D G B E)',
                {
                    'D': 146.83,
                    'G': 196.00,
                    'B': 246.94,
                    'E': 329.63
                }
            ),
            'D Tuning (A D F# B)': TuningPreset(
                'D Tuning (A D F# B)',
                {
                    'A': 440.00,
                    'D': 293.66,
                    'F#': 369.99,
                    'B': 493.88
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
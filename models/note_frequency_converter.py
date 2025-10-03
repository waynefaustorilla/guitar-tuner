from typing import Tuple, List
import math


class NoteFrequencyConverter:
    NOTE_NAMES = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']

    NOTE_TO_SEMITONE = {
        'C': 0, 'C#': 1, 'Db': 1,
        'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4,
        'F': 5, 'F#': 6, 'Gb': 6,
        'G': 7, 'G#': 8, 'Ab': 8,
        'A': 9, 'A#': 10, 'Bb': 10,
        'B': 11
    }

    STANDARD_NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    OCTAVE_RANGE = list(range(1, 6))
    
    def __init__(self, reference_frequency: float = 440.0):
        self.reference_frequency = reference_frequency
    
    def note_to_frequency(self, note: str, octave: int) -> float:
        if note not in self.NOTE_TO_SEMITONE:
            raise ValueError(f"Invalid note: {note}")
        
        semitone_in_octave = self.NOTE_TO_SEMITONE[note]
        semitones_from_a4 = (octave - 4) * 12 + (semitone_in_octave - 9)
        
        frequency = self.reference_frequency * (2 ** (semitones_from_a4 / 12))
        
        return round(frequency, 2)
    
    def frequency_to_note(self, frequency: float) -> Tuple[str, int, float]:
        semitones_from_a4 = 12 * math.log2(frequency / self.reference_frequency)
        
        nearest_semitone = round(semitones_from_a4)
        
        cents_deviation = (semitones_from_a4 - nearest_semitone) * 100
        
        total_semitones = nearest_semitone + 9
        octave = 4 + (total_semitones // 12)
        semitone_in_octave = total_semitones % 12
        
        note = self.STANDARD_NOTES[semitone_in_octave]
        
        return note, octave, round(cents_deviation, 1)
    
    def get_all_notes_in_range(self, min_freq: float = 60.0, max_freq: float = 350.0) -> List[Tuple[str, int, float]]:
        notes = []
        
        for octave in self.OCTAVE_RANGE:
            for note in self.STANDARD_NOTES:
                freq = self.note_to_frequency(note, octave)
                if min_freq <= freq <= max_freq:
                    notes.append((note, octave, freq))
        
        return notes
    
    def get_note_display_name(self, note: str, octave: int) -> str:
        return f"{note}{octave}"
    
    def parse_note_display_name(self, display_name: str) -> Tuple[str, int]:
        if len(display_name) >= 3 and display_name[-2] == '#':
            note = display_name[:-1]
            octave = int(display_name[-1])
        elif len(display_name) >= 2:
            note = display_name[:-1]
            octave = int(display_name[-1])
        else:
            raise ValueError(f"Invalid note display name: {display_name}")

        return note, octave
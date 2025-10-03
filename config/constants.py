class AudioConstants:
    CHUNK_SIZE = 4096
    SAMPLE_RATE = 44100
    MIN_VALID_FREQUENCY = 50.0
    MAX_VALID_FREQUENCY = 1000.0
    AUDIO_PROCESSING_SLEEP_INTERVAL = 0.05


class TuningConstants:
    IN_TUNE_THRESHOLD = 3.0
    CLOSE_THRESHOLD = 15.0


class UIConstants:
    TUNING_METER_WIDTH = 600
    TUNING_METER_HEIGHT = 350
    TUNING_METER_RADIUS = 180
    TUNING_METER_CENTER_Y_OFFSET = 80

    WINDOW_TITLE = "🎸 Guitar Tuner Pro"
    WINDOW_SUBTITLE = "Professional Instrument Tuning"


class NoteFrequencies:
    """Standard note frequencies in Hz (A4 = 440 Hz)"""

    # Bass notes (0 and 1)
    B0 = 30.87
    D1 = 36.71
    E1 = 41.20
    A1 = 55.00
    B1 = 61.74

    # Low octave notes (2)
    C2 = 65.41
    Db2 = 69.30
    D2 = 73.42
    E2 = 82.41
    Eb2 = 77.78
    Gb2 = 92.50
    G2 = 98.00
    A2 = 110.00
    B2 = 123.47

    # Mid-low octave notes (3)
    C3 = 130.81
    Db3 = 138.59
    D3 = 146.83
    E3 = 164.81
    Eb3 = 155.56
    F3 = 174.61
    Gb3 = 185.00
    G3 = 196.00
    Ab3 = 207.65
    A3 = 220.00
    Bb3 = 233.08
    B3 = 246.94

    # High octave notes (4)
    C4 = 261.63
    Db4 = 277.18
    D4 = 293.66
    E4 = 329.63
    Eb4 = 311.13
    F4 = 349.23
    Gb4 = 369.99
    G4 = 392.00
    Ab4 = 415.30
    A4 = 440.00
    B4 = 493.88
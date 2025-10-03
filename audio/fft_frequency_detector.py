from typing import Optional
import numpy as np
from scipy.signal import find_peaks
from .frequency_detector import FrequencyDetector


class FFTFrequencyDetector(FrequencyDetector):
    def __init__(self, sample_rate: int, chunk_size: int,
                 min_frequency: float = 50.0, max_frequency: float = 1000.0):
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
    def detect_frequency(self, audio_data: np.ndarray) -> Optional[float]:
        windowed = audio_data * np.hanning(len(audio_data))
        fft = np.abs(np.fft.rfft(windowed))
        freqs = np.fft.rfftfreq(len(audio_data), 1.0 / self.sample_rate)

        freq_mask = (freqs >= self.min_frequency) & (freqs <= self.max_frequency)
        fft_filtered = fft.copy()
        fft_filtered[~freq_mask] = 0

        peaks, _ = find_peaks(fft_filtered, height=np.max(fft_filtered) * 0.1)

        if len(peaks) == 0:
            return None

        peak_index = peaks[np.argmax(fft_filtered[peaks])]
        frequency = freqs[peak_index]

        if self.min_frequency <= frequency <= self.max_frequency:
            return frequency

        return None

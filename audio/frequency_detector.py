from abc import ABC, abstractmethod
from typing import Optional
import numpy as np


class FrequencyDetector(ABC):
    @abstractmethod
    def detect_frequency(self, audio_data: np.ndarray) -> Optional[float]:
        pass

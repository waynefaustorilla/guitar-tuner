from typing import Optional, Callable
from .audio_stream_manager import AudioStreamManager
from .frequency_detector import FrequencyDetector
from config import AudioConstants


class AudioProcessor:
    def __init__(self, stream_manager: AudioStreamManager, frequency_detector: FrequencyDetector, frequency_callback: Optional[Callable[[float], None]] = None):
        self.stream_manager = stream_manager
        self.frequency_detector = frequency_detector
        self.frequency_callback = frequency_callback
        self._is_processing = False
    
    def start_processing(self) -> bool:
        if self._is_processing:
            return False
        
        if not self.stream_manager.open_stream():
            return False
        
        self._is_processing = True

        return True
    
    def stop_processing(self):
        self._is_processing = False
        self.stream_manager.close_stream()
    
    def process_audio_frame(self) -> Optional[float]:
        if not self._is_processing:
            return None

        audio_data = self.stream_manager.read_audio_data()

        if audio_data is None:
            return None

        frequency = self.frequency_detector.detect_frequency(audio_data)

        if frequency and AudioConstants.MIN_VALID_FREQUENCY < frequency < AudioConstants.MAX_VALID_FREQUENCY:
            if self.frequency_callback:
                self.frequency_callback(frequency)

            return frequency

        return None
    
    def is_processing(self) -> bool:
        return self._is_processing
    
    def cleanup(self):
        self.stop_processing()
        self.stream_manager.terminate()
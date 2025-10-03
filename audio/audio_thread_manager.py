import threading
import time
from typing import Callable, Optional
from .audio_processor import AudioProcessor
from analysis import TuningAnalyzer, TuningResult
from config import AudioConstants


class AudioThreadManager:
    def __init__(self, audio_processor: AudioProcessor, tuning_analyzer: TuningAnalyzer, on_result_callback: Callable[[TuningResult], None], get_target_frequency: Callable[[], float]):
        self.audio_processor = audio_processor
        self.tuning_analyzer = tuning_analyzer
        self.on_result_callback = on_result_callback
        self.get_target_frequency = get_target_frequency
        
        self._audio_thread: Optional[threading.Thread] = None
        self._is_running = False
    
    def start(self) -> bool:
        if self._is_running:
            return False
        
        if not self.audio_processor.start_processing():
            return False
        
        self._is_running = True
        self._audio_thread = threading.Thread(target=self._audio_processing_loop)
        self._audio_thread.daemon = True
        self._audio_thread.start()
        return True
    
    def stop(self):
        self._is_running = False
        self.audio_processor.stop_processing()
    
    def is_running(self) -> bool:
        return self._is_running
    
    def _audio_processing_loop(self):
        while self._is_running:
            try:
                frequency = self.audio_processor.process_audio_frame()
                
                if frequency:
                    target_freq = self.get_target_frequency()
                    result = self.tuning_analyzer.analyze(frequency, target_freq)
                    self.on_result_callback(result)
            
            except Exception as e:
                print(f"Audio processing error: {e}")
            
            time.sleep(AudioConstants.AUDIO_PROCESSING_SLEEP_INTERVAL)
from typing import Optional
import numpy as np
import pyaudio


class AudioStreamManager:
    def __init__(self, chunk_size: int = 4096, sample_rate: int = 44100):
        self.chunk_size = chunk_size
        self.sample_rate = sample_rate
        self.format = pyaudio.paFloat32
        self.channels = 1
        
        self._audio = pyaudio.PyAudio()
        self._stream = None
    
    def open_stream(self) -> bool:
        try:
            self._stream = self._audio.open(format=self.format, channels=self.channels, rate=self.sample_rate, input=True, frames_per_buffer=self.chunk_size)
            return True

        except Exception as e:
            print(f"Error opening audio stream: {e}")
            return False
    
    def close_stream(self):
        if self._stream:
            self._stream.stop_stream()
            self._stream.close()
            self._stream = None
    
    def read_audio_data(self) -> Optional[np.ndarray]:
        if not self._stream:
            return None
        
        try:
            data = self._stream.read(self.chunk_size, exception_on_overflow=False)
            return np.frombuffer(data, dtype=np.float32)
        except Exception as e:
            print(f"Error reading audio data: {e}")
            return None
    
    def is_stream_open(self) -> bool:
        return self._stream is not None
    
    def terminate(self):
        self.close_stream()
        self._audio.terminate()

from .tuning_status import TuningStatus
from .tuning_result import TuningResult


class TuningAnalyzer:
    def __init__(self, in_tune_threshold: float = 3.0, close_threshold: float = 15.0):
        self.in_tune_threshold = in_tune_threshold
        self.close_threshold = close_threshold
    
    def analyze(self, detected_frequency: float, target_frequency: float) -> TuningResult:
        deviation = detected_frequency - target_frequency
        status = self._determine_status(deviation)
        
        return TuningResult(detected_frequency=detected_frequency, target_frequency=target_frequency, deviation=deviation, status=status)
    
    def _determine_status(self, deviation: float) -> TuningStatus:
        abs_deviation = abs(deviation)
        
        if abs_deviation < self.in_tune_threshold:
            return TuningStatus.IN_TUNE

        elif deviation > 0:
            return TuningStatus.TOO_HIGH

        else:
            return TuningStatus.TOO_LOW
    
    def is_close_to_target(self, deviation: float) -> bool:
        return abs(deviation) < self.close_threshold
    
    def get_tuning_color(self, deviation: float) -> str:
        abs_deviation = abs(deviation)

        if abs_deviation < self.in_tune_threshold:
            return '#27ae60'
        elif abs_deviation < self.close_threshold:
            return '#f39c12'
        else:
            return '#e74c3c'
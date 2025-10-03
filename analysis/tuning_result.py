from dataclasses import dataclass
from .tuning_status import TuningStatus


@dataclass
class TuningResult:
    detected_frequency: float
    target_frequency: float
    deviation: float
    status: TuningStatus
    
    @property
    def is_in_tune(self) -> bool:
        return self.status == TuningStatus.IN_TUNE
    
    @property
    def deviation_percentage(self) -> float:
        if self.target_frequency == 0:
            return 0.0

        return (self.deviation / self.target_frequency) * 100

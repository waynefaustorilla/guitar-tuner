from typing import Optional
from .instrument import Instrument
from .tuning_preset import TuningPreset


class TunerState:
    def __init__(self, instrument: Instrument, tuning: TuningPreset):
        self._instrument = instrument
        self._tuning = tuning
        self._current_string = tuning.get_string_names()[0] if tuning.get_string_names() else ""
    
    @property
    def instrument(self) -> Instrument:
        return self._instrument
    
    @instrument.setter
    def instrument(self, value: Instrument):
        self._instrument = value
    
    @property
    def tuning(self) -> TuningPreset:
        return self._tuning
    
    @tuning.setter
    def tuning(self, value: TuningPreset):
        self._tuning = value
    
    @property
    def current_string(self) -> str:
        return self._current_string
    
    @current_string.setter
    def current_string(self, value: str):
        self._current_string = value
    
    def get_current_frequency(self) -> float:
        return self._tuning.get_frequency(self._current_string)
    
    def get_string_names(self) -> list:
        return self._tuning.get_string_names()


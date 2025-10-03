from enum import Enum


class TuningStatus(Enum):
    IN_TUNE = "IN_TUNE"
    TOO_HIGH = "TOO_HIGH"
    TOO_LOW = "TOO_LOW"
    UNKNOWN = "UNKNOWN"

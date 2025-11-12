"""Analytics configuration."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class AnalyticsConfig:
    """Analytics configuration."""

    data_path: str = os.getenv("DATA_PATH", "./data")
    
    # Benchmark config
    benchmark_periods: list = None
    
    def __post_init__(self):
        if self.benchmark_periods is None:
            self.benchmark_periods = [30, 60, 90, 252]


config = AnalyticsConfig()

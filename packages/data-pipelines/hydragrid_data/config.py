"""Data pipelines configuration."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class DataConfig:
    """Data pipeline configuration."""

    data_path: str = os.getenv("DATA_PATH", "./data")
    parquet_path: str = os.getenv("PARQUET_PATH", "./data/parquet")
    
    # Data sources
    equities_source: str = "yfinance"
    futures_source: str = "local"
    
    # Cache
    cache_ttl_hours: int = 24


config = DataConfig()

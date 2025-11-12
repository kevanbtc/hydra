"""Engine core configuration."""

import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


@dataclass
class EngineConfig:
    """Global engine configuration."""

    env: str = os.getenv("HYDRAGRID_ENV", "dev")
    data_path: str = os.getenv("DATA_PATH", "./data")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    # Risk limits
    global_max_leverage: float = float(os.getenv("GLOBAL_MAX_LEVERAGE", "2.0"))
    max_daily_loss_pct: float = float(os.getenv("MAX_DAILY_LOSS_PCT", "5.0"))
    
    # Execution
    default_timeout_seconds: int = 30
    
    @classmethod
    def from_env(cls) -> "EngineConfig":
        """Load config from environment."""
        return cls()


config = EngineConfig.from_env()

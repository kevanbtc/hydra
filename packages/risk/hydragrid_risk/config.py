"""Risk configuration."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class RiskConfig:
    """Risk management configuration."""

    global_max_leverage: float = float(os.getenv("GLOBAL_MAX_LEVERAGE", "2.0"))
    max_daily_loss_pct: float = float(os.getenv("MAX_DAILY_LOSS_PCT", "5.0"))
    
    # Risk models
    var_confidence: float = 0.95
    cvar_confidence: float = 0.95
    max_drawdown_pct: float = 20.0


config = RiskConfig()

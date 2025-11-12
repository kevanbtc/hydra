"""Infrastructure configuration."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class InfraConfig:
    """Infrastructure and API configuration."""

    env: str = os.getenv("HYDRAGRID_ENV", "dev")
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    cors_origins: str = os.getenv("API_CORS_ORIGINS", "*")
    
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


config = InfraConfig()

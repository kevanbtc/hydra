"""Swarm configuration."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class SwarmConfig:
    """Swarm and MCP configuration."""

    mode: str = os.getenv("SWARM_MODE", "committee")
    num_agents: int = int(os.getenv("NUM_AGENTS", "5"))
    
    # Agent behaviors
    agent_timeout_seconds: int = 60
    voting_strategy: str = "weighted_median"


config = SwarmConfig()

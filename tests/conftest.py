"""Test fixtures and conftest for HydraGrid."""

import pytest


@pytest.fixture
def sample_config():
    """Provide a sample configuration for testing."""
    return {
        "env": "test",
        "global_max_leverage": 2.0,
        "max_daily_loss_pct": 5.0,
    }

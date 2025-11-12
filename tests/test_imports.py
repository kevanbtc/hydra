"""Smoke test: verify all packages import without error."""

import pytest


def test_engine_core_imports():
    """Engine core should import cleanly."""
    import unykornx_engine
    import unykornx_engine.config

    assert unykornx_engine.config.config is not None


def test_data_pipelines_imports():
    """Data pipelines should import cleanly."""
    import hydragrid_data
    import hydragrid_data.config

    assert hydragrid_data.config.config is not None


def test_strategies_stock_imports():
    """Stock strategies should import cleanly."""
    import unykornx_strategies_stock

    assert unykornx_strategies_stock is not None


def test_strategies_energy_imports():
    """Energy strategies should import cleanly."""
    import unykornx_strategies_energy

    assert unykornx_strategies_energy is not None


def test_swarm_imports():
    """Swarm should import cleanly."""
    import hydragrid_swarm
    import hydragrid_swarm.config

    assert hydragrid_swarm.config.config is not None


def test_risk_imports():
    """Risk should import cleanly."""
    import hydragrid_risk
    import hydragrid_risk.config

    assert hydragrid_risk.config.config is not None


def test_analytics_imports():
    """Analytics should import cleanly."""
    import hydragrid_analytics
    import hydragrid_analytics.config

    assert hydragrid_analytics.config.config is not None


def test_infra_imports():
    """Infrastructure should import cleanly."""
    import hydragrid_infra
    import hydragrid_infra.config

    assert hydragrid_infra.config.config is not None


@pytest.mark.parametrize(
    "package_name",
    [
        "unykornx_engine",
        "hydragrid_data",
        "unykornx_strategies_stock",
        "unykornx_strategies_energy",
        "hydragrid_swarm",
        "hydragrid_risk",
        "hydragrid_analytics",
        "hydragrid_infra",
    ],
)
def test_all_packages_have_version(package_name):
    """All packages should define __version__."""
    import importlib

    pkg = importlib.import_module(package_name)
    assert hasattr(pkg, "__version__")

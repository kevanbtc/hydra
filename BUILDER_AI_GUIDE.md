# Builder AI Instructions for HydraGrid

This file is for the builder-AI assigned to implement HydraGrid phases.

## Current Status: Phase 1 Complete ✓

The **skeleton monorepo** is in place. All directories exist, configs are set, and package structure is validated.

## For Phase 2 Implementation

When assigned Phase 2 ("Engine-core + toy strategies + backtest"), follow these steps:

### 1. Start Location
```
packages/engine-core/unykornx_engine/
```

This is where 90% of Phase 2 work happens.

### 2. Implementation Order

**FIRST**: Study the existing stubs:
- `packages/engine-core/unykornx_engine/config.py` – already loads from env
- `packages/engine-core/unykornx_engine/__init__.py` – package structure
- Look at the "Phase 2" section in `packages/docs/PHASE_GUIDE.md`

**SECOND**: Implement core classes (in this order):
```
1. instruments.py        → Stock, Future, Spread classes
2. orders.py             → Order model, state machine
3. portfolio.py          → Position tracking, PnL
4. venues/base.py        → VenueClient ABC
5. events.py             → Event types
6. execution.py          → Smart routing
7. orchestrator.py       → Main event loop
8. backtest.py           → Historical backtester
```

**THIRD**: Add data stubs:
```
packages/data-pipelines/hydragrid_data/
  - equities/ingest_equities.py
  - futures_energy/ingest_futures.py
```

**FOURTH**: Implement two simple strategies:
```
packages/strategies-stock/unykornx_strategies_stock/
  - mean_reversion_equities.py

packages/strategies-energy/unykornx_strategies_energy/
  - calendar_spread_trader.py
```

**FIFTH**: Hook up analytics:
```
packages/analytics/hydragrid_analytics/
  - timeseries.py (Sharpe, Sortino, max DD)
  - trades.py     (win rate, payoff, expectancy)
  - reports.py    (JSON output)
```

**SIXTH**: Write tests:
```
tests/
  - test_engine_core_instruments.py
  - test_backtest_simple.py
  - test_energy_calendar_spread.py
```

### 3. Design Patterns to Follow

**Instrument Protocol**:
```python
class Instrument(Protocol):
    symbol: str
    asset_class: str  # "equity", "future", "spread"
    multiplier: float
    min_tick: float
```

**Strategy Protocol**:
```python
class Strategy(Protocol):
    def on_data(self, snapshot: MarketSnapshot) -> StrategySignal:
        ...
```

**VenueClient Interface**:
```python
class VenueClient(ABC):
    def get_quotes(self, symbols: list) -> dict: ...
    def place_order(self, order: Order) -> str: ...
    def cancel_order(self, order_id: str) -> bool: ...
    def get_positions(self) -> list: ...
```

### 4. Testing Checklist

Phase 2 is done when:
- [ ] `pytest tests -v` – all tests pass
- [ ] `python -m unykornx_engine.backtest --strategy=mean_reversion_equities --symbol=AAPL` works
- [ ] Output includes: Sharpe, max DD, win rate, trade list
- [ ] No import errors in any package
- [ ] Energy calendar spread backtest also works

### 5. Environment & Debug

**Useful commands**:
```bash
# Install in dev mode (from hydragrid root)
pip install -e .[all]

# Run tests with coverage
pytest tests -v --cov=packages

# Run specific test
pytest tests/test_backtest_simple.py::test_mean_reversion_aapl -v

# Debug config loading
python -c "from unykornx_engine.config import config; print(config)"
```

**VS Code Launch Configs** (already defined in `.vscode/launch.json`):
- "Python: Run Backtest" – Run backtest.py
- "Python: Run Tests" – Run test suite
- "Python: Debug [module]" – Attach debugger

### 6. Common Pitfalls to Avoid

1. **Don't hardcode broker details** → use venues/ abstraction
2. **Don't mix strategy logic with execution** → keep them separate
3. **Don't forget event types** → use events.py for market/trade/risk events
4. **Don't assume market hours** → make backtest time-zone agnostic
5. **Risk must be enforced in orchestrator**, not in strategies

### 7. Code Quality

All code must pass:
```bash
black --check packages/
flake8 packages/
mypy packages/ --ignore-missing-imports
pytest tests/ -v
```

These are run on save in VS Code (see `.vscode/settings.json`).

### 8. Quick Reference

| File | Purpose |
|------|---------|
| `instruments.py` | Asset classes (Stock, Future, Spread) |
| `orders.py` | Order model + state machine |
| `portfolio.py` | Track positions, PnL, margin |
| `venues/base.py` | Broker interface (ABC) |
| `orchestrator.py` | Main loop that wires everything |
| `backtest.py` | Historical backtester |
| `events.py` | Event types (MarketEvent, TradeEvent, RiskEvent) |

### 9. Asking for Help

If stuck on a module:
1. Check `ARCHITECTURE.md` for design intent
2. Check existing `__init__.py` and `config.py` for patterns
3. Check test stubs in `tests/` for expected signatures
4. Look at vendor-specific clients in `venues/` for interface patterns

---

## Phase 3+ Notes

After Phase 2 is complete, you'll be reassigned to `packages/analytics/` for Phase 3 (benchmarking), then `packages/swarm/` for Phase 4 (MCP agents), etc.

Each phase is designed to build on the previous without requiring massive rewrites.

Good luck, builder!

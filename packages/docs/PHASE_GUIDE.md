# Phase Implementation Guide

## Phase 1: Skeleton + VS Code Workspace ✓

**Status**: Complete

**What we did**:
- Created full monorepo directory structure
- Set up `.vscode` configs (settings, launch configs, extensions)
- Created `pyproject.toml`, `pytest.ini`, `.flake8`
- Added skeleton `__init__.py` and `config.py` in all packages
- Added test imports to verify structure

**Validation**:
```bash
cd hydragrid
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[all]
pytest tests -v
```

Expected: All import tests pass, zero failures.

---

## Phase 2: Engine-core + Toy Strategies + Backtest

**What to build**:

### 2.1 Engine Core Skeleton
File: `packages/engine-core/unykornx_engine/`

Create:
- `instruments.py` – Define `Stock`, `Future`, `Spread` classes
- `portfolio.py` – Track positions, PnL, margin
- `orders.py` – Order model + state machine
- `venues/base.py` – `VenueClient` ABC
- `execution.py` – Route strategies → orders
- `orchestrator.py` – Main event loop
- `events.py` – Market/trade/risk event types
- `backtest.py` – Historical data loop + execution sim

### 2.2 Data Stubs
File: `packages/data-pipelines/hydragrid_data/`

Create:
- `equities/ingest_equities.py` – Download OHLCV for test symbols (AAPL, SPY)
- `futures_energy/ingest_futures.py` – Stub or CSV mock data for NG, CL

### 2.3 Simple Strategies
File: `packages/strategies-stock/` and `packages/strategies-energy/`

Create:
- **Stock**: `mean_reversion_equities.py` – Simple 20-day mean reversion
- **Energy**: `calendar_spread_trader.py` – Simple NG front/back spread

### 2.4 Analytics Hooks
File: `packages/analytics/hydragrid_analytics/`

Create:
- `timeseries.py` – Compute Sharpe, Sortino, max DD on a PnL series
- `trades.py` – Win rate, payoff, expectancy per trade
- `reports.py` – JSON output summaries

### 2.5 Tests
File: `tests/`

Create:
- `test_engine_core_instruments.py` – Can create/modify orders
- `test_backtest_simple.py` – Run mean reversion backtest on AAPL, check Sharpe > 0
- `test_energy_calendar_spread.py` – NG spread backtest, verify positions

**Deliverable**:
```bash
python -m unykornx_engine.backtest --strategy=mean_reversion_equities --symbol=AAPL
# Output: JSON with Sharpe, win rate, DD, trade list
```

**Phase 2 is complete when**: Backtest CLI works for 1 stock + 1 energy strategy, metrics computed.

---

## Phase 3: Analytics + Benchmarks

**What to build**:

### 3.1 Benchmark Config
File: `packages/analytics/hydragrid_analytics/benchmarks.py`

Create:
- Load strategy configs from YAML
- Run backtest suite for multiple strategies
- Output JSON with results

### 3.2 API Stubs
File: `packages/infra/hydragrid_infra/api/`

Create:
- `main.py` – FastAPI app
- `routes/benchmarks.py` – GET `/benchmarks` returns JSONL results

### 3.3 Tests
Create:
- `test_benchmark_runner.py` – Run 3-strategy benchmark, check all metrics present

**Deliverable**:
```bash
uvicorn hydragrid_infra.api.main:app --reload
# GET http://localhost:8000/benchmarks
# Returns: JSON list of strategy benchmarks
```

**Phase 3 is complete when**: API endpoint returns benchmark results.

---

## Phase 4: Swarm + MCP Tools

**What to build**:

### 4.1 MCP Tools
File: `packages/swarm/hydragrid_swarm/mcp/tools/`

Create:
- `backtest_tool.py` – Call engine backtest, return stats
- `risk_tool.py` – Query risk engine, run scenarios
- `data_query_tool.py` – Fetch features, regime signals

### 4.2 Agents
File: `packages/swarm/hydragrid_swarm/agents/`

Create:
- `base.py` – `Agent` ABC
- `data_agent.py` – DataAgent (queries data via MCP tool)
- `regime_agent.py` – RegimeAgent (classifies bull/bear)
- `strategy_architect.py` – StrategyArchitect (proposes config)
- `risk_agent.py` – RiskAgent (runs scenarios)

### 4.3 Committee
File: `packages/swarm/hydragrid_swarm/committee.py`

Create:
- Aggregate agent outputs → `MetaStrategyConfig`
- Weighted voting or median aggregation

### 4.4 Tests
Create:
- `test_swarm_cycle.py` – Run one swarm cycle, check config produced

**Deliverable**:
```bash
python -m hydragrid_swarm.committee
# Runs one swarm cycle, outputs MetaStrategyConfig JSON
```

**Phase 4 is complete when**: Swarm produces valid strategy config.

---

## Phase 5: API + Portal

**What to build**:

### 5.1 API Routes
File: `packages/infra/hydragrid_infra/api/routes/`

Create:
- `auth.py` – POST `/auth/connect_broker` (stub, store broker ID)
- `profiles.py` – GET/POST `/profiles`
- `metrics.py` – GET `/metrics/live` (mock PnL)
- `swarm.py` – GET `/swarm/status`

### 5.2 Workers
File: `packages/infra/hydragrid_infra/workers/`

Create:
- `live_trading_worker.py` – Background loop, applies swarm config

### 5.3 Portal
File: `packages/web-portal/`

Create (Next.js skeleton):
- `pages/dashboard.tsx` – Equity, PnL, PRI pie chart
- `pages/profiles.tsx` – Strategy picker
- Connect to API

### 5.4 Tests
Create:
- `test_api_endpoints.py` – Hit each route, check 200

**Deliverable**:
```bash
uvicorn hydragrid_infra.api.main:app
# Open http://localhost:3000 (portal)
# Connect broker → pick profile → see dashboard
```

**Phase 5 is complete when**: Portal loads dashboard, shows live mock data.

---

## Phase 6: Energy Expansion + Real Venues

**What to build**:

### 6.1 Real Venue Clients
File: `packages/engine-core/unykornx_engine/venues/`

Create:
- `ib_client.py` – Interactive Brokers (for stocks + futures)
- `alpaca_client.py` – Alpaca (equities only, optional)
- `energy_exchange.py` – Futures exchange (CME, EEX, etc.)

### 6.2 Energy Strategies Expansion
File: `packages/strategies-energy/unykornx_strategies_energy/`

Add:
- `term_structure_carry.py` – Proper contango/backwardation trading
- `vol_arb_energy.py` – Volatility arbitrage
- `load_forecast_trader.py` – Power demand forecasting (ML-driven)

### 6.3 Risk Enhancements
File: `packages/risk/hydragrid_risk/`

Enhance:
- Curve risk (front vs back month)
- Spread risk
- Cross-market correlation

### 6.4 Regime Models
File: `packages/swarm/hydragrid_swarm/agents/`

Enhance:
- Separate equity/energy regime models
- Cross-asset correlation awareness

**Deliverable**:
Live trading on both equities + energy, swarm-driven.

---

## Quick Start Checklist

```
Phase 1 ✓ – Monorepo skeleton
  [ ] Repos imports without error
  [ ] Tests pass: pytest tests -v
  [ ] VS Code workspace opens all folders

Phase 2 – Engine + toy strategies
  [ ] Backtest CLI works
  [ ] Mean reversion equity strategy runs
  [ ] Calendar spread energy strategy runs
  [ ] Metrics computed correctly

Phase 3 – Analytics + API
  [ ] Benchmark runner works
  [ ] API endpoint returns results
  [ ] Portal skeleton loads

Phase 4 – Swarm
  [ ] Agents run independently
  [ ] Committee produces config
  [ ] Swarm cycle complete

Phase 5 – Portal + multi-user
  [ ] API auth + profiles work
  [ ] Portal shows live dashboard
  [ ] Swarm decisions reflected in UI

Phase 6 – Real venues + energy
  [ ] Paper trade on IB/Alpaca
  [ ] Energy futures live
  [ ] Cross-asset regime detection
```

---

## Notes for Builder AI

When implementing each phase, consult:
- `ARCHITECTURE.md` for design details
- `pyproject.toml` for dependency versions
- `.vscode/launch.json` for debug configs
- Existing test stubs for patterns

Each phase is designed to be **independent** but **buildable** in sequence. Start with Phase 2, point AI at that package folder, and iterate.

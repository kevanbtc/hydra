# HydraGrid Architecture

This document describes the architectural design of UnykornX HydraGrid.

## Design Principles

1. **Instrument Agnostic**: Strategies work on abstract market data, not broker-specific formats.
2. **Venue Independent**: Multiple brokers/exchanges plugged via consistent interface.
3. **Modular AI**: Swarm agents are orthogonal to trading logic, coordinated via MCP.
4. **Risk-First**: Risk constraints baked into every module, enforced at orchestration layer.
5. **Extensible**: New strategies, venues, instruments require no core rewrites.

## Core Modules

### Engine Core
Universal order, portfolio, and execution engine.

**Responsibilities**:
- Instrument definitions (stocks, futures, spreads, options)
- Portfolio tracking (positions, PnL, margin)
- Order management (creation, routing, state machine)
- Venue abstraction layer
- Execution orchestration (backtesting, live trading)
- Risk enforcement

### Data Pipelines
Transforms dirty market data into clean, usable time series.

**Equities**: Daily EOD, intraday, fundamentals, universe selection.

**Energy/Futures**: Futures curves, term structure, calendar spreads, congestion signals.

### Strategy Packages
Two separate but equivalent strategy packs.

**Stock Strategies**:
- Mean reversion
- Momentum/trend
- Stat arb (pairs)
- Factor tilt (value/momentum/quality)
- Volatility breakouts

**Energy Strategies**:
- Term structure carry
- Calendar spreads
- Vol arb (future: options)
- Load forecasting (future: powered by ML)

### Risk Engine
Hard stops and portfolio risk analytics.

**Responsibilities**:
- Position limits (leverage, exposure, per-asset)
- Scenario testing (shocks, drawdowns)
- Risk metrics (VaR, CVaR, drawdown, curve risk)
- Risk intensity (PRI) for UI

### Analytics
Metrics, benchmarking, and backtesting.

**Responsibilities**:
- Time series metrics (returns, Sharpe, Sortino, DD)
- Trade-level stats (win rate, payoff, expectancy)
- Exposure tracking (gross, net, turnover)
- Benchmark comparisons
- Regime simulation (for stress testing)

### Swarm & MCP
AI agents orchestrated by MCP tools.

**Agents**:
- **DataAgent**: Fetches features, builds regimes
- **RegimeAgent**: Bull/bear/chop classification (equities + energy)
- **StrategyArchitect**: Proposes strategy mixes + parameterizations
- **RiskAgent**: Scenario tests, veto/shrink exposure
- **DeploymentAgent**: Decides when to go live/paper

**MCP Tools**:
- Data query tool
- Backtest/benchmark tool
- Risk tool
- Open-source catalog tool
- Market signal tool

**Committee**: Aggregates agent opinions → MetaStrategyConfig

### Infrastructure & API
SaaS delivery layer.

**API Endpoints**:
- `POST /auth/connect_broker` – auth
- `GET /profiles` – trading profiles
- `POST /profiles` – create/update
- `GET /metrics/live` – live PnL/risk
- `GET /benchmarks` – baseline comparisons
- `GET /swarm/status` – agent decisions

**Workers**:
- Backtest worker
- Benchmark worker
- Live trading worker

### Web Portal
Dashboard for users.

**Pages**:
- Dashboard (equity, PnL, PRI, exposure)
- Profiles (choose strategy set + risk tier)
- Benchmarks (user vs baseline)
- Swarm Lab (agent decisions, overrides)

## Data Flow

### Backtest Flow
1. DataAgent queries historical data → features
2. Strategies consume features → signals
3. Orchestrator: signals → risk checks → order queue
4. Backtest engine: order queue + execution model → fills/PnL
5. Analytics: compute metrics

### Live Trading Flow
1. DataAgent: stream data → live features
2. RegimeAgent: classify regime (continuous)
3. StrategyArchitect: (hourly/daily) propose strategy config
4. RiskAgent: veto/shrink as needed
5. Committee: aggregate → MetaStrategyConfig
6. Orchestrator: apply config → live strategies → signals → risk → orders
7. Venue: execute orders
8. Portal: reflect live PnL/metrics

### Swarm Cycle
```
On schedule or trigger:
  DataAgent → (data, features, recent perf)
  RegimeAgent → (regime classification)
  StrategyArchitect → (strategy proposal)
  RiskAgent → (scenario tests)
  Committee → (voting) → MetaStrategyConfig
  Orchestrator ← (pulls new config) → apply
```

## Extensibility Points

### New Strategy
1. Inherit from `Strategy` protocol
2. Implement `on_data(snapshot) -> StrategySignal`
3. Register in engine config
4. Add benchmarks + tests

### New Venue
1. Inherit from `VenueClient` interface
2. Implement `get_quotes`, `place_order`, `cancel_order`, `get_positions`
3. Register in execution layer
4. Test with existing strategies

### New Agent
1. Inherit from `Agent` ABC
2. Implement decision logic + MCP tool calls
3. Register with `Committee`
4. Define voting weights

### New Risk Metric
1. Implement in `risk.portfolio_risk`
2. Add MCP tool endpoint
3. Wire into `RiskAgent`
4. Surface on portal

## Testing Strategy

- **Unit tests**: Per-module logic (instruments, orders, portfolio)
- **Integration tests**: Strategy + engine + data (no live venue)
- **Backtest tests**: Historical scenarios, known outcomes
- **End-to-end tests**: API + swarm + full orchestration

## Deployment

**Development**: Single-machine, local brokers, paper trading.

**Staging**: Multiple workers, real data, paper trading + limited live.

**Production**: Distributed workers, real venues, risk gates, monitoring.

See `packages/infra/` for deployment configs.

---

See [PHASE_GUIDE.md](PHASE_GUIDE.md) for implementation roadmap.

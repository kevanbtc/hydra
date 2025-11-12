# UnykornX HydraGrid – Complete Skeleton Structure

Last Updated: November 12, 2025
Status: **Phase 1 Complete ✓**

---

## Directory Tree

```
hydragrid/
├── .vscode/                          # VS Code workspace config
│   ├── settings.json                 # Python formatting & linting
│   ├── launch.json                   # Debugger launch configs
│   └── extensions.json               # Recommended extensions
│
├── packages/
│   ├── engine-core/                  # 🔧 Universal trading engine
│   │   ├── __init__.py
│   │   └── unykornx_engine/
│   │       ├── __init__.py
│   │       ├── config.py             # Engine configuration
│   │       ├── instruments.py        # [PHASE 2] Stock, Future, Spread
│   │       ├── portfolio.py          # [PHASE 2] Position tracking
│   │       ├── orders.py             # [PHASE 2] Order model
│   │       ├── events.py             # [PHASE 2] Event types
│   │       ├── execution.py          # [PHASE 2] Smart routing
│   │       ├── orchestrator.py       # [PHASE 2] Main event loop
│   │       ├── backtest.py           # [PHASE 2] Historical backtester
│   │       ├── logging.py            # [PHASE 2] Structured logging
│   │       └── venues/
│   │           ├── __init__.py
│   │           ├── base.py           # [PHASE 2] VenueClient ABC
│   │           ├── ib_client.py      # [PHASE 6] Interactive Brokers
│   │           ├── alpaca_client.py  # [PHASE 6] Alpaca
│   │           └── energy_exchange.py # [PHASE 6] Futures exchanges
│   │
│   ├── data-pipelines/               # 📊 Market data ingestion
│   │   ├── __init__.py
│   │   └── hydragrid_data/
│   │       ├── __init__.py
│   │       ├── config.py
│   │       ├── equities/
│   │       │   ├── __init__.py
│   │       │   ├── ingest_equities.py # [PHASE 2] Download OHLCV
│   │       │   ├── fundamentals.py    # [PHASE 3+] Earnings, factors
│   │       │   └── universe.py        # [PHASE 3+] Universe selection
│   │       ├── futures_energy/
│   │       │   ├── __init__.py
│   │       │   ├── ingest_futures.py  # [PHASE 2] Futures data
│   │       │   ├── term_structure.py  # [PHASE 6] Curve building
│   │       │   ├── calendar_spreads.py # [PHASE 6] Spread series
│   │       │   └── congestion_signals.py # [PHASE 6] Power signals
│   │       └── storage/
│   │           ├── __init__.py
│   │           ├── local_parquet.py   # [PHASE 3] Parquet storage
│   │           └── db.py              # [PHASE 5+] Database layer
│   │
│   ├── strategies-stock/             # 📈 Equity strategies
│   │   ├── __init__.py
│   │   └── unykornx_strategies_stock/
│   │       ├── __init__.py
│   │       ├── mean_reversion_equities.py   # [PHASE 2]
│   │       ├── momentum_trend_equities.py   # [PHASE 3]
│   │       ├── stat_arb_pairs.py            # [PHASE 3]
│   │       ├── factor_tilt.py               # [PHASE 4]
│   │       └── volatility_breakout.py       # [PHASE 4]
│   │
│   ├── strategies-energy/            # ⚡ Energy/futures strategies
│   │   ├── __init__.py
│   │   └── unykornx_strategies_energy/
│   │       ├── __init__.py
│   │       ├── calendar_spread_trader.py    # [PHASE 2]
│   │       ├── term_structure_carry.py      # [PHASE 6]
│   │       ├── vol_arb_energy.py            # [PHASE 6]
│   │       └── load_forecast_trader.py      # [PHASE 6]
│   │
│   ├── swarm/                        # 🤖 AI agent orchestration
│   │   ├── __init__.py
│   │   └── hydragrid_swarm/
│   │       ├── __init__.py
│   │       ├── config.py
│   │       ├── base.py               # [PHASE 4] Agent ABC
│   │       ├── committee.py          # [PHASE 4] Voting aggregator
│   │       ├── policies.py           # [PHASE 5] Meta-policies
│   │       ├── planner.py            # [PHASE 5] Lab planner
│   │       ├── mcp/
│   │       │   ├── __init__.py
│   │       │   └── tools/
│   │       │       ├── __init__.py
│   │       │       ├── benchmark_tool.py   # [PHASE 4]
│   │       │       ├── backtest_tool.py    # [PHASE 4]
│   │       │       ├── risk_tool.py        # [PHASE 4]
│   │       │       ├── data_query_tool.py  # [PHASE 4]
│   │       │       └── catalog_tool.py     # [PHASE 4]
│   │       └── agents/
│   │           ├── __init__.py
│   │           ├── base.py                 # [PHASE 4]
│   │           ├── data_agent.py           # [PHASE 4]
│   │           ├── regime_agent.py         # [PHASE 4]
│   │           ├── strategy_architect.py   # [PHASE 4]
│   │           ├── risk_agent.py           # [PHASE 4]
│   │           └── deployment_agent.py     # [PHASE 5]
│   │
│   ├── risk/                         # 🛡️ Risk management
│   │   ├── __init__.py
│   │   └── hydragrid_risk/
│   │       ├── __init__.py
│   │       ├── config.py
│   │       ├── limits.py              # [PHASE 2] Hard limits
│   │       ├── sizing.py              # [PHASE 2] Position sizing
│   │       ├── scenarios.py           # [PHASE 3] Stress scenarios
│   │       ├── portfolio_risk.py      # [PHASE 3] Risk metrics
│   │       └── pri.py                 # [PHASE 5] Portfolio Risk Intensity
│   │
│   ├── analytics/                    # 📈 Metrics & benchmarks
│   │   ├── __init__.py
│   │   └── hydragrid_analytics/
│   │       ├── __init__.py
│   │       ├── config.py
│   │       ├── timeseries.py          # [PHASE 2] Time series metrics
│   │       ├── trades.py              # [PHASE 2] Trade-level stats
│   │       ├── exposure.py            # [PHASE 3] Exposure tracking
│   │       ├── benchmarks.py          # [PHASE 3] Benchmark runner
│   │       ├── sim_market.py          # [PHASE 4] Market simulation
│   │       ├── sim_orderbook.py       # [PHASE 4] Execution simulation
│   │       └── reports.py             # [PHASE 3] JSON/HTML reports
│   │
│   ├── infra/                        # 🚀 Deployment & API
│   ├── onchain/                      # ⛓️ Control plane (Solidity)
│   │   ├── contracts/                # HydraVault, PolicyStore, Oracles, etc.
│   │   ├── scripts/                  # deploy.ts, configure.ts
│   │   ├── test/                     # Hardhat tests
│   │   ├── hardhat.config.ts
│   │   └── package.json
│   │
│   │   ├── __init__.py
│   │   └── hydragrid_infra/
│   │       ├── __init__.py
│   │       ├── config.py
│   │       ├── api/
│   │       │   ├── __init__.py
│   │       │   ├── main.py            # [PHASE 3] FastAPI app
│   │       │   └── routes/
│   │       │       ├── __init__.py
│   │       │       ├── health.py      # [PHASE 3]
│   │       │       ├── auth.py        # [PHASE 5]
│   │       │       ├── profiles.py    # [PHASE 5]
│   │       │       ├── metrics.py     # [PHASE 5]
│   │       │       ├── benchmarks.py  # [PHASE 3]
│   │       │       └── swarm.py       # [PHASE 5]
│   │       ├── workers/
│   │       │   ├── __init__.py
│   │       │   ├── backtest_worker.py    # [PHASE 3]
│   │       │   ├── benchmark_worker.py   # [PHASE 3]
│   │       │   └── live_trading_worker.py # [PHASE 5]
│   │       └── config/
│   │           ├── base.yaml             # [PHASE 5]
│   │           ├── dev.yaml
│   │           └── prod.yaml
│   │
│   ├── web-portal/                   # 🎨 Frontend dashboard
│   │   ├── [PHASE 5] Next.js/React skeleton
│   │   ├── pages/
│   │   │   ├── dashboard.tsx
│   │   │   ├── profiles.tsx
│   │   │   ├── benchmarks.tsx
│   │   │   └── swarm_lab.tsx
│   │   └── components/
│   │
│   └── docs/                         # 📚 Documentation
│       ├── ARCHITECTURE.md           # System design
│       ├── PHASE_GUIDE.md            # Implementation roadmap
│       ├── API.md                    # [PHASE 5] API documentation
│       ├── ONCHAIN.md                # On-chain contracts & flows
│       └── DEPLOYMENT.md             # [PHASE 5+] Deployment guide
│
├── tests/                            # 🧪 Test suite
│   ├── conftest.py                   # Pytest fixtures
│   ├── test_imports.py               # Import verification
│   ├── test_engine_core_*.py         # [PHASE 2] Engine tests
│   ├── test_backtest_*.py            # [PHASE 2] Backtest tests
│   ├── test_strategies_*.py          # [PHASE 2+] Strategy tests
│   ├── test_analytics_*.py           # [PHASE 3] Analytics tests
│   ├── test_api_*.py                 # [PHASE 3] API tests
│   └── test_swarm_*.py               # [PHASE 4] Swarm tests
│
├── .vscode/
├── .github/                          # [PHASE 5+] CI/CD (GitHub Actions)
│
├── .env.example                      # Environment variables template
├── .env                              # [CREATED BY USER] Local env
├── .gitignore                        # Git ignore patterns
├── .flake8                           # Flake8 config
├── pytest.ini                        # Pytest config
├── pyproject.toml                    # Project metadata & deps
│
├── README.md                         # Main documentation
├── LICENSE                           # MIT License
├── BUILDER_AI_GUIDE.md              # Instructions for Phase 2 builder
├── PHASE1_VALIDATION.py              # Phase 1 checklist script
├── show_phase1_status.py             # Status dashboard script
│
└── hydragrid.code-workspace          # VS Code multi-root workspace

```

---

## Key Files (Phase 1 Complete)

| File | Purpose |
|------|---------|
| `pyproject.toml` | Python dependencies, build config |
| `.vscode/settings.json` | Black, Flake8, mypy, pytest settings |
| `.vscode/launch.json` | Debug launch configs (backtest, swarm, tests) |
| `hydragrid.code-workspace` | VS Code multi-root workspace (open to work on any package) |
| `README.md` | Main project overview |
| `ARCHITECTURE.md` | Full system design (in `packages/docs/`) |
| `PHASE_GUIDE.md` | Phase-by-phase roadmap (in `packages/docs/`) |
| `BUILDER_AI_GUIDE.md` | Instructions for Phase 2 builder-AI |

---

## Phase Status

| Phase | Name | Status | Modules |
|-------|------|--------|---------|
| 1 | Skeleton | ✅ Complete | All directories, configs, test infrastructure |
| 2 | Engine + Toy Strategies | ⏳ Next | engine-core, data-pipelines, strategies |
| 3 | Analytics + Benchmarks | ⏳ Later | analytics, infra/api |
| 4 | Swarm + MCP Tools | ⏳ Later | swarm, mcp tools, agents |
| 5 | API + Portal | ⏳ Later | infra, web-portal |
| 6 | Energy + Real Venues | ⏳ Later | venues, energy strategies |

---

## Environment Setup

```bash
# 1. Create virtual environment
cd hydragrid
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -e .[all]

# 3. Verify imports
pytest tests/test_imports.py -v

# 4. Run Phase 1 validation
python show_phase1_status.py

# 5. Open in VS Code
code hydragrid.code-workspace
```

---

## Next: Phase 2

**When ready for Phase 2 (Engine-core + toy strategies + backtest):**

1. Read: `BUILDER_AI_GUIDE.md`
2. Read: `packages/docs/PHASE_GUIDE.md` (Phase 2 section)
3. Point builder-AI at: `packages/engine-core/unykornx_engine/`
4. Expected deliverable: Working backtest CLI + metrics

---

## Notes

- **[PHASE X]** indicates when that module/file is first used/implemented
- All packages follow identical patterns: `__init__.py` + `config.py` + submodules
- Tests are centralized in `/tests` but organized by phase
- Documentation is in `packages/docs/` (ARCHITECTURE.md, PHASE_GUIDE.md)
- Configuration is centralized in `pyproject.toml` and `.vscode/`
- VS Code workspace allows working on any package independently
- All code follows Black (formatting) + Flake8 (linting) + mypy (typing) standards

---

**Created**: November 12, 2025  
**System**: UnykornX HydraGrid v0.0.1  
**Prepared for**: Phase 2 Implementation

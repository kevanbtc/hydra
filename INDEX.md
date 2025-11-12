# HydraGrid Documentation Index

**Status**: Phase 1 Complete ✓ | Ready for Phase 2 Implementation

---

## 📖 Start Here

| Document | Purpose | For Whom |
|----------|---------|----------|
| **README.md** | Project overview, quick start, phases | Everyone |
| **STRUCTURE.md** | Complete directory tree with phase markers | Developers |
| **ARCHITECTURE.md** | Full system design & principles | Architects, Phase 2+ builders |
| **PHASE_GUIDE.md** | Phase-by-phase implementation roadmap | Phase 2+ builders |
| **BUILDER_AI_GUIDE.md** | Instructions for Phase 2 builder-AI | Phase 2 builder |

---

## 🚀 For Phase 2 Builder AI

**Read these first** (in order):
1. `README.md` – Understand what HydraGrid is
2. `ARCHITECTURE.md` (in `packages/docs/`) – Understand the design
3. `BUILDER_AI_GUIDE.md` – Get specific Phase 2 instructions
4. `PHASE_GUIDE.md` (in `packages/docs/`) – Read "Phase 2" section

**Then implement** (in order):
1. `packages/engine-core/unykornx_engine/instruments.py`
2. `packages/engine-core/unykornx_engine/orders.py`
3. (... continue with Phase 2 checklist)

**Validate** by running:
```bash
pytest tests -v
python show_phase1_status.py
```

---

## 🎯 Quick Navigation

### Development
- **Project root**: `hydragrid/`
- **Workspace**: `hydragrid/hydragrid.code-workspace`
- **Config**: `pyproject.toml`, `.vscode/settings.json`
- **Tests**: `tests/`

### By Package
- **Engine**: `packages/engine-core/unykornx_engine/` – [PHASE 2]
- **Data**: `packages/data-pipelines/hydragrid_data/` – [PHASE 2+]
- **Strategies (Stock)**: `packages/strategies-stock/` – [PHASE 2]
- **Strategies (Energy)**: `packages/strategies-energy/` – [PHASE 2]
- **Swarm**: `packages/swarm/hydragrid_swarm/` – [PHASE 4]
- **Risk**: `packages/risk/hydragrid_risk/` – [PHASE 2+]
- **Analytics**: `packages/analytics/hydragrid_analytics/` – [PHASE 3]
- **API/Infra**: `packages/infra/hydragrid_infra/` – [PHASE 3+]
- **Portal**: `packages/web-portal/` – [PHASE 5]
- **On-Chain Control Plane**: `packages/onchain/` – [PHASE 2 foundation]
  - Contracts: `HydraVault`, `HydraVaultFactory`, `StrategyRegistry`, `MCPPolicyStore`, `MCPOracle`, `RiskGuardian`, `PerformanceOracle`, `Governance`, `TokenHYDRA`
  - Scripts: `deploy.ts` (stack deploy), `configure.ts` (placeholder wiring)
  - Tests: Hardhat tests (e.g. `hydra_vault.test.ts`)
  - Docs: `packages/docs/ONCHAIN.md`

### Documentation
- **Main**: `README.md`, `STRUCTURE.md` (this repo root)
- **Deep Dive**: `packages/docs/ARCHITECTURE.md`, `packages/docs/PHASE_GUIDE.md`
- **CI/CD**: `.github/` – [PHASE 5+]

---

## 📋 Phase Checklist

### Phase 1: Skeleton ✅
- [x] Directory structure created
- [x] VS Code configs (.vscode/)
- [x] pyproject.toml + pytest.ini
- [x] All package __init__.py + config.py
- [x] Test infrastructure (conftest.py, test_imports.py)
- [x] Documentation (README, ARCHITECTURE, PHASE_GUIDE)
- [x] Validation scripts (PHASE1_VALIDATION.py, show_phase1_status.py)

### Phase 2: Engine + Toy Strategies ⏳
- [ ] Implement engine-core modules (instruments, orders, portfolio, etc.)
- [ ] Add data ingestion stubs (equities, futures)
- [ ] Implement 2 simple strategies (stock + energy)
- [ ] Hook up analytics
- [ ] Write tests

### Phase 3: Analytics + Benchmarks ⏳
- [ ] Complete analytics modules
- [ ] Implement benchmark runner
- [ ] Add API stubs
- [ ] Portal skeleton

### Phase 4: Swarm + MCP ⏳
- [ ] Implement MCP tools
- [ ] Implement agents (DataAgent, RegimeAgent, etc.)
- [ ] Implement committee voting
- [ ] Wire into orchestrator

### Phase 5: API + Portal ⏳
- [ ] Complete FastAPI routes
- [ ] Build React dashboard
- [ ] Multi-user auth + profiles
- [ ] Live metrics + swarm status

### Phase 6: Energy + Real Venues ⏳
- [ ] Add real broker clients (IB, Alpaca, etc.)
- [ ] Expand energy strategies
- [ ] Enhanced risk models
- [ ] Cross-asset regime detection

---

## 🛠️ Development Commands

```bash
# Setup
cd hydragrid
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[all]

# Testing
pytest tests -v                      # Run all tests
pytest tests -v --cov=packages       # With coverage
pytest tests/test_imports.py -v      # Just import tests

# Linting
black packages/                       # Format
flake8 packages/                      # Check style
mypy packages/ --ignore-missing-imports

# Validation
python show_phase1_status.py          # Phase 1 status
python PHASE1_VALIDATION.py           # Checklist

# IDE
code hydragrid.code-workspace         # Open in VS Code
```

---

## 📚 Key Concepts

### Instruments
- **Stock**: Equities, ETFs (US + global)
- **Future**: Futures contracts (energy, commodities, etc.)
- **Spread**: Calendar spreads, pairs, etc.
- **Option**: (Future extension)

### Venues
- **IB**: Interactive Brokers (stocks + futures)
- **Alpaca**: Retail equities
- **Crypto**: (Optional extension)
- **Futures Exchange**: CME, EEX, etc.

### Strategies
- **Regime-based**: Bull/bear/chop classification
- **Carry**: Term structure trades
- **Mean Reversion**: Oversold/overbought reversals
- **Momentum**: Trend following
- **Vol Arb**: Volatility arbitrage

### Risk
- **Hard Limits**: Leverage, exposure, daily loss
- **Portfolio Risk**: VaR, CVaR, drawdown, curve risk
- **PRI**: Portfolio Risk Intensity (UI metric)

### AI Swarm
- **DataAgent**: Features + market data
- **RegimeAgent**: Bull/bear/chop classification
- **StrategyArchitect**: Strategy mix proposals
- **RiskAgent**: Scenario testing
- **Committee**: Aggregate → MetaStrategyConfig

---

## 🔐 License

MIT License. See [LICENSE](LICENSE).

---

## ❓ FAQ

**Q: Where do I start?**  
A: `README.md` → `ARCHITECTURE.md` → `PHASE_GUIDE.md` (Phase 2 section)

**Q: How do I run Phase 2?**  
A: Read `BUILDER_AI_GUIDE.md` for detailed instructions.

**Q: Can I work on different packages simultaneously?**  
A: Yes! Use `hydragrid.code-workspace` to open multiple packages side-by-side.

**Q: What if I need to add a new package?**  
A: Follow the pattern: create `packages/new-pkg/unykornx_new_pkg/`, add `__init__.py` + `config.py`, register in `pyproject.toml`.

**Q: How do I debug?**  
A: Use VS Code launch configs in `.vscode/launch.json`. Set breakpoints and hit F5.

---

**Last Updated**: November 12, 2025  
**HydraGrid Version**: 0.0.1  
**Status**: Phase 1 Complete, Ready for Phase 2 Builder Assignment

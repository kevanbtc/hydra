# UnykornX HydraGrid

**Multi-asset AI trading system**: equities + energy futures, governed by an AI swarm with MCP tools.

## Overview

HydraGrid is a modular, multi-asset trading platform designed for:

- **Equity/ETF trading** (US + global)
- **Energy market trading** (power futures, gas/oil futures, spreads)
- **AI-driven strategy orchestration** (swarm of agents + MCP tools)
- **Multi-tenant SaaS delivery** (API + web portal)
- **Extensibility** (new venues, instruments, strategies without rewrites)

## Architecture

See [ARCHITECTURE.md](packages/docs/ARCHITECTURE.md) for the full design document.

### Quick Structure

```
hydragrid/
  packages/
    engine-core/           → Universal order/portfolio engine
    data-pipelines/        → Stock & energy data ingestion
    strategies-stock/      → Equity strategies
    strategies-energy/     → Futures/energy strategies
    swarm/                 → AI agents + MCP orchestration
    risk/                  → Risk engine, limits, scenarios
    analytics/             → Metrics, backtests, benchmarks
    infra/                 → API, workers, deployment
    web-portal/            → Frontend + user dashboard
    docs/                  → Documentation
```

## Setup (Phase 1: Skeleton)

### Prerequisites

- Python 3.10+
- `pip` or `pipenv`

### Installation

1. Clone the repo:
   ```bash
   cd hydragrid
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. Install in development mode:
   ```bash
   pip install -e .[all]
   ```

4. Copy `.env.example` to `.env` and configure:
   ```bash
   cp .env.example .env
   ```

### Run Tests

```bash
pytest tests -v
```

## Build Phases

- **Phase 1**: Skeleton + VS Code workspace ✓
- **Phase 2**: Engine-core + toy strategies + backtest
- **Phase 3**: Analytics & benchmarks
- **Phase 4**: Swarm + MCP tools
- **Phase 5**: API & Portal
- **Phase 6**: Energy expansion + real venues

## Usage (Next Steps)

After Phase 1 scaffold is complete:

1. Point builder-AI at `packages/engine-core/` to implement **Phase 2**.
2. Each phase unlocks the next with increasing complexity.

See [PHASE_GUIDE.md](packages/docs/PHASE_GUIDE.md) for detailed implementation steps per phase.

## Contributing

Contributions follow the project structure and coding standards in `.vscode/settings.json` and `pyproject.toml`.

## License

MIT. See [LICENSE](LICENSE).

## Contact

HydraGrid Dev Team

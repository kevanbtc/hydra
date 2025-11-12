# UnykornX HydraGrid

**Multi-asset AI trading system**: equities + energy futures, governed by an AI swarm with MCP tools.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Color-coded repo map](#color-coded-repo-map)
- [Diagrams & flow trees](#diagrams--flow-trees)
- [Setup (Phase 1: Skeleton)](#setup-phase-1-skeleton)
- [Build Phases](#build-phases)
- [Usage (Next Steps)](#usage-next-steps)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

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

```text
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

---

## Color-coded repo map

Legend: packages are grouped by functional domain and color-coded consistently across docs and diagrams.

- Data: ![data](https://img.shields.io/badge/Data-1f77b4?style=flat&labelColor=1b2a41&logoColor=white)
- Engine: ![engine](https://img.shields.io/badge/Engine-17a2b8?style=flat&labelColor=1b2a41&logoColor=white)
- Strategies: ![strategies](https://img.shields.io/badge/Strategies-6f42c1?style=flat&labelColor=1b2a41&logoColor=white)
- Risk: ![risk](https://img.shields.io/badge/Risk-d9534f?style=flat&labelColor=1b2a41&logoColor=white)
- Swarm (AI/MCP): ![swarm](https://img.shields.io/badge/Swarm-ff7f0e?style=flat&labelColor=1b2a41&logoColor=white)
- Analytics: ![analytics](https://img.shields.io/badge/Analytics-2ca02c?style=flat&labelColor=1b2a41&logoColor=white)
- Infra/API: ![infra](https://img.shields.io/badge/Infra/API-6c757d?style=flat&labelColor=1b2a41&logoColor=white)
- On-chain: ![onchain](https://img.shields.io/badge/On--chain-8c564b?style=flat&labelColor=1b2a41&logoColor=white)

| Package | Domain | Path |
|---|---|---|
| ![engine](https://img.shields.io/badge/Engine-17a2b8?style=flat&labelColor=1b2a41&logo=data:image/svg+xml;base64,PHN2Zy8+) | Engine core | `packages/engine-core/unykornx_engine/` |
| ![data](https://img.shields.io/badge/Data-1f77b4?style=flat&labelColor=1b2a41) | Data pipelines | `packages/data-pipelines/hydragrid_data/` |
| ![strategies](https://img.shields.io/badge/Strategies-6f42c1?style=flat&labelColor=1b2a41) | Stock strategies | `packages/strategies-stock/unykornx_strategies_stock/` |
| ![strategies](https://img.shields.io/badge/Strategies-6f42c1?style=flat&labelColor=1b2a41) | Energy strategies | `packages/strategies-energy/unykornx_strategies_energy/` |
| ![swarm](https://img.shields.io/badge/Swarm-ff7f0e?style=flat&labelColor=1b2a41) | AI agents + MCP | `packages/swarm/hydragrid_swarm/` |
| ![risk](https://img.shields.io/badge/Risk-d9534f?style=flat&labelColor=1b2a41) | Risk engine | `packages/risk/hydragrid_risk/` |
| ![analytics](https://img.shields.io/badge/Analytics-2ca02c?style=flat&labelColor=1b2a41) | Analytics | `packages/analytics/hydragrid_analytics/` |
| ![infra](https://img.shields.io/badge/Infra/API-6c757d?style=flat&labelColor=1b2a41) | API, workers, deploy | `packages/infra/hydragrid_infra/` |
| ![onchain](https://img.shields.io/badge/On--chain-8c564b?style=flat&labelColor=1b2a41) | Contracts + scripts | `packages/onchain/` |

Color legend and end-to-end diagrams are in [DIAGRAMS.md](packages/docs/DIAGRAMS.md).

---

## Diagrams & flow trees

See consolidated diagrams (system architecture, data flow, swarm decisioning, on-chain control plane, risk policy flows) in [DIAGRAMS.md](packages/docs/DIAGRAMS.md).

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

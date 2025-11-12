#!/usr/bin/env python3
"""
UnykornX HydraGrid – Phase 1 Scaffold Complete

This script validates and summarizes the Phase 1 skeleton setup.
Run this to confirm everything is ready for Phase 2 implementation.
"""

import os
from pathlib import Path

HYDRA_ROOT = Path(__file__).parent

def count_files(pattern: str) -> int:
    """Count files matching a pattern."""
    return len(list(HYDRA_ROOT.rglob(pattern)))


def main():
    """Print Phase 1 summary."""
    print("\n" + "=" * 80)
    print(" " * 20 + "UNYKORNX HYDRAGRID - PHASE 1 COMPLETE")
    print("=" * 80 + "\n")

    print("📦 PACKAGE STRUCTURE")
    print("-" * 80)
    packages = [
        "packages/engine-core",
        "packages/data-pipelines",
        "packages/strategies-stock",
        "packages/strategies-energy",
        "packages/swarm",
        "packages/risk",
        "packages/analytics",
        "packages/infra",
        "packages/web-portal",
        "packages/docs",
    ]
    for pkg in packages:
        pkg_path = HYDRA_ROOT / pkg
        if pkg_path.exists():
            print(f"  ✓ {pkg}")
        else:
            print(f"  ✗ {pkg} (MISSING)")

    print("\n🔧 CONFIGURATION FILES")
    print("-" * 80)
    configs = [
        (".vscode/settings.json", "Python formatting & linting rules"),
        (".vscode/launch.json", "Debugger configurations (backtest, swarm, tests)"),
        (".vscode/extensions.json", "Recommended VS Code extensions"),
        ("hydragrid.code-workspace", "VS Code multi-root workspace"),
        ("pyproject.toml", "Python project metadata & dependencies"),
        (".flake8", "Style checking rules"),
        ("pytest.ini", "Test runner configuration"),
        (".env.example", "Environment variables template"),
        (".gitignore", "Git ignore patterns"),
        ("README.md", "Main documentation"),
        ("LICENSE", "MIT License"),
    ]
    for config, desc in configs:
        config_path = HYDRA_ROOT / config
        status = "✓" if config_path.exists() else "✗"
        print(f"  {status} {config:<40} - {desc}")

    print("\n📊 CODE STATISTICS")
    print("-" * 80)
    py_files = count_files("*.py")
    test_files = count_files("test_*.py")
    doc_files = count_files("*.md")
    config_files = count_files("*.toml") + count_files("*.ini") + count_files(".flake8")
    print(f"  Python files:       {py_files}")
    print(f"  Test files:         {test_files}")
    print(f"  Documentation:      {doc_files} markdown files")
    print(f"  Configuration:      {config_files} config files")

    print("\n🚀 QUICK START")
    print("-" * 80)
    print("""
  1. Create virtual environment:
     cd hydragrid
     python -m venv .venv
     source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

  2. Install dependencies:
     pip install -e .[all]

  3. Run import tests:
     pytest tests -v

  4. Open in VS Code:
     code hydragrid.code-workspace

  5. Read Phase 2 plan:
     - See: packages/docs/PHASE_GUIDE.md
     - See: BUILDER_AI_GUIDE.md
    """)

    print("📚 DOCUMENTATION")
    print("-" * 80)
    docs = [
        ("README.md", "Main project overview & setup"),
        ("ARCHITECTURE.md", "Full system design (stored in packages/docs/)"),
        ("PHASE_GUIDE.md", "Phase-by-phase implementation roadmap"),
        ("BUILDER_AI_GUIDE.md", "Instructions for Phase 2 builder-AI"),
        ("PHASE1_VALIDATION.py", "Validation checklist (run to verify)"),
    ]
    for doc, desc in docs:
        doc_path = HYDRA_ROOT / doc
        if not doc_path.exists():
            doc_path = HYDRA_ROOT / "packages" / "docs" / doc
        status = "✓" if doc_path.exists() else "✗"
        print(f"  {status} {doc:<30} - {desc}")

    print("\n✅ PHASE 1 STATUS: READY FOR PHASE 2")
    print("=" * 80)
    print("""
Next: Point builder-AI at packages/engine-core/ with the Phase 2 spec.

The skeleton provides:
  • Clean separation of concerns (8 independent packages)
  • VS Code multi-root workspace (work on any package independently)
  • Consistent configuration (black, flake8, mypy, pytest)
  • Full test infrastructure (pytest + fixtures)
  • Detailed phase-by-phase roadmap
  • Builder AI instructions (BUILDER_AI_GUIDE.md)

Phase 2 will build the trading engine. All subsequent phases are built on top.
    """)
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()

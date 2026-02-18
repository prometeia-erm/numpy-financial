# Repository Guidelines

## Fork Scope & Upstream Sync
- This repository is a fork of an external upstream project and must be periodically realigned with upstream changes.
- Keep local divergence intentionally small: this fork should primarily contain custom build workflows and security checks.
- Avoid introducing product-level feature drift here unless explicitly approved as fork-specific maintenance.
- When syncing from upstream, prefer clean reconciliation commits that separate upstream sync from local fork adjustments.

## Project Structure & Module Organization
- Core package: `numpy_financial/` (`_financial.py` for Python implementation, `_cfinancial.pyx` for Cython support, `__init__.py` exports).
- Tests: `numpy_financial/tests/` (main suite in `test_financial.py`, property-based helpers in `strategies.py`).
- Docs: `doc/source/` (Sphinx sources) and `docweb/` (site assets).
- Benchmarks: `benchmarks/` with `asv.conf.json` for Airspeed Velocity runs.
- Build/config: `pyproject.toml`, `meson.build`, `noxfile.py`, `environment.yml`.

## Build, Test, and Development Commands
- `python -m pip install -e .[test,dev]`: install package with test/dev dependencies.
- `nox`: run the full CI-aligned matrix (`tests_py311_np1`, `tests_py311_np2`, `tests_py313_np2`).
- `nox -s tests_py313_np2`: run one targeted compatibility session.
- `pytest -q`: run tests directly in the active environment.
- `mypy --no-incremental --cache-dir=/dev/null .`: run static typing checks used in CI.
- `pyright`: run secondary type checker.
- `spin build` / `spin test`: build and test via the Scientific Python workflow.

## Coding Style & Naming Conventions
- Follow PEP 8 with 4-space indentation and explicit type hints on new/changed code.
- Use `snake_case` for functions/variables, `PascalCase` for exceptions/classes, and module-private helpers prefixed with `_`.
- Keep public API exports explicit (update `__all__` when introducing public symbols).
- Prefer NumPy-aware vectorized logic and preserve scalar/array behavior parity.

## Testing Guidelines
- Frameworks: `pytest` + `hypothesis`.
- Add tests in `numpy_financial/tests/test_*.py`; keep deterministic unit tests near related function coverage.
- For numeric behavior changes, include edge cases (e.g., `rate == 0`, scalar vs array input, Decimal support where applicable).
- Run `nox` before opening a PR to validate Python/NumPy compatibility.

## Commit & Pull Request Guidelines
- Follow existing history style: concise, imperative subjects, often prefixed with scope/tag (examples: `ci: ...`, `build: ...`, `TYP: ...`, `STY: ...`).
- Keep commits focused; separate refactors from behavior changes.
- PRs should include: clear summary, rationale, test evidence (commands run), and linked issue(s) when relevant.
- Update docs/tests alongside API or behavior changes.

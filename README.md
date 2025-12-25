# Linux Auth Log Analyzer

Python tool to parse Linux authentication logs (e.g. `/var/log/auth.log`) and extract security-relevant signals (failed logins, suspicious IPs/users) with reproducible checks (tests + lint + CI).

[![CI](https://github.com/sauldmorales/linux-auth-log-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/sauldmorales/linux-auth-log-analyzer/actions/workflows/ci.yml)

## What it does
- Parses `auth.log`-style lines into actionable info (summaries, IP/user counts, patterns).
- Enforces reproducibility: **tests + lint + CI** (not “works on my machine”).

## Project structure

.
├── src/
│   └── auth_log_analyzer.py
├── tests/
│   └── test_smoke.py
├── sample_data/
│   └── auth.log
├── requirements.txt
├── pyproject.toml
├── .github/workflows/ci.yml
└── README.md


## Requirements

Python 3.10+ (recommended: 3.11)

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run
```bash
python src/auth_log_analyzer.py sample_data/auth.log
```
## Test
```bash
python -m pytest -q tests
```
## Lint
```bash
ruff check .
```
## CI

GitHub Actions runs on every push / pull request and executes:
install deps
lint (ruff)
tests (pytest)

## Security notes

Do not commit real logs that contain private data (IPs, usernames, hostnames).
Use sample_data/ for reproducible demos


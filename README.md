![CI](https://github.com/sauldmorales/linux-auth-log-analyzer/actions/workflows/ci.yml/badge.svg)
## Setup
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

## Tests

pytest

## Run

python src/auth_log_analyzer.py sample_data/auth.log

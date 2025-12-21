import subprocess
import sys
from pathlib import Path

def test_cli_runs_on_sample_log():
    sample = Path("sample_data/auth.log")
    assert sample.exists(), "Falta sample_data/auth.log en el repo"
    r = subprocess.run(
        [sys.executable, "src/auth_log_analyzer.py", str(sample)],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, f"STDERR:\n{r.stderr}"
    assert r.stdout.strip() != ""

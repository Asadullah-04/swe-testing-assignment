import subprocess
import sys


def run_cli(expr: str) -> str:
    completed = subprocess.run(
        [sys.executable, "-m", "quickcalc.cli", expr],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def test_user_flow_addition():
    assert run_cli("5 + 3 =") == "8"


def test_clear_resets():
    assert run_cli("9 * 9 = C") == "0"


def test_division_by_zero_shows_error():
    assert run_cli("10 / 0 =") == "Error"
"""CLI regression tests: conflicting generation modes must be rejected."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from clipassgen.app import cli


def _run_cli(monkeypatch, capsys, argv):
    monkeypatch.setattr(sys, "argv", ["clipassgen"] + argv)
    return cli(), capsys.readouterr()


def test_conflicting_modes_rejected(monkeypatch, capsys):
    """--smart --strong must fail instead of silently running one mode."""
    monkeypatch.setattr(
        sys, "argv",
        ["clipassgen", "--smart", "--strong", "-s", "long enough secret phrase", "-l", "16"],
    )
    with pytest.raises(SystemExit) as exc_info:
        cli()
    assert exc_info.value.code == 1
    assert "cannot be combined" in capsys.readouterr().out


def test_conflicting_code_and_public_rejected(monkeypatch, capsys):
    monkeypatch.setattr(
        sys, "argv",
        ["clipassgen", "--code", "--public", "-s", "long enough secret phrase", "-l", "8"],
    )
    with pytest.raises(SystemExit) as exc_info:
        cli()
    assert exc_info.value.code == 1
    assert "cannot be combined" in capsys.readouterr().out


def test_single_mode_still_works(monkeypatch, capsys):
    """A single --code mode must keep working after the guard."""
    returncode, output = _run_cli(monkeypatch, capsys, ["--code", "-l", "8"])
    assert returncode is None
    assert len(output.out.strip()) == 8

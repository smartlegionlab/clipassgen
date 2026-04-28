# Copyright © 2026, Alexander Suvorov
"""clipassgen (Console Smart Password Generator CLI) - Terminal-based smart password generator with
deterministic password generation. Generate passwords from secret phrases - same secret always produces
the same password, no storage required."""
from clipassgen.app import cli


if __name__ == '__main__':
    cli()

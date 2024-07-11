# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Console Smart Passwords Generator."""
from clipassgen.app_manager import AppManager


def cli():
    app_manager = AppManager()
    app_manager.main_menu()


if __name__ == '__main__':
    cli()

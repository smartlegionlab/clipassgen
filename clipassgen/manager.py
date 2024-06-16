# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from clipassgen import __version__
from clipassgen.commander import CommandMan
from smartcliapp import Informer


class CliMan(Informer):
    name = 'clipassgen'
    title = 'CliPassGen'
    description = 'Console Smart Password Generator'
    version = __version__
    copyright = 'Copyright © 2024, A.A. Suvorov'
    url = 'https://github.com/smartlegionlab'
    commander = CommandMan()

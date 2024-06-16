# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import click


class Config:

    click_group = click.group(
        context_settings={'help_option_names': ['-h', '--help']},
        invoke_without_command=True
    )

    length_option = click.option(
        '--num', '-n',
        type=click.INT,
        help='Password length.',
    )

    secret_option = click.option(
        '--secret', '-s',
        type=click.STRING,
        default='',
        help='Secret phrase.',
        hide_input=True,
    )

    name_option = click.option(
        '--login', '-l',
        type=click.STRING,
        help='Name or login.',
        default='',
    )

# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import click

from clipassgen.config import Config
from clipassgen.manager import CliMan


@Config.click_group
@click.version_option(f'{CliMan.name} v{CliMan.version}')
@click.pass_context
def cli(ctx):
    CliMan.show_head()
    if ctx.invoked_subcommand is None:
        CliMan.commander.menu()


@cli.command('menu')
def menu():
    return CliMan.commander.menu()


@cli.command('smart')
@Config.name_option
@Config.secret_option
@Config.length_option
def smart(login, secret, num):
    return CliMan.commander.smart(
        login,
        secret,
        num,
    )


@cli.command('normal')
@Config.length_option
@Config.secret_option
def normal(secret, num):
    return CliMan.commander.normal(
        secret=secret,
        length=num,
    )


@cli.command('base')
@Config.length_option
def default(num):
    return CliMan.commander.base(
        length=num,
    )


@cli.result_callback()
def process_result(result):
    CliMan.show_footer()


if __name__ == '__main__':
    cli()

# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import click
from smartcliapp import CliManager

from smartpasslib.generators import SmartPasswordMaster


class CommandMan:
    @staticmethod
    def _prompt_length(start: int = 4, end: int = 1000):
        length = click.prompt(
            f'Password length ({start}-{end})',
            type=click.IntRange(start, end, clamp=True)
        )
        return length

    @staticmethod
    def _prompt_secret() -> str:
        secret = click.prompt(
            f'Enter your secret phrase',
            type=click.STRING,
            hide_input=True
        )
        return secret

    @staticmethod
    def _prompt_login() -> str:
        login = click.prompt(
            f'Enter a name or login',
            type=click.STRING
        )
        return login

    def __init__(self):
        self._smart_pass_gen = SmartPasswordMaster()
        self._cli_man = CliManager()

    def menu(self):
        while 1:
            self._cli_man.printer.smart.echo('Main menu')
            self._cli_man.printer.base.echo('s: Smart Password Generator (login + secret phrase)')
            self._cli_man.printer.base.echo('n: Smart Password Generator (secret phrase)')
            self._cli_man.printer.base.echo('b: Base Password Generator')
            self._cli_man.printer.base.echo('q: quit')
            self._cli_man.printer.smart.echo()
            char = click.getchar()

            if char.lower() in ('q', 'й'):
                break

            elif char.lower() in ('s', 'ы'):
                self.smart()

            elif char.lower() in ('n', 'т'):
                self.normal()

            elif char.lower() in ('b', 'и'):
                self.base()
            else:
                self._cli_man.printer.smart.echo()
                self._cli_man.printer.base.echo('Invalid input!')

            self._cli_man.printer.smart.echo()
            input('Enter to continue...')

    def smart(self, login='', secret='', length=0):
        self._cli_man.printer.smart.echo("Smart Password Generator")
        if not login:
            login = self._prompt_login()
        if not secret:
            secret = self._prompt_secret()
        if not length or length <= 0:
            length = self._prompt_length()
        password = self._smart_pass_gen.get_smart_password(login=login, secret=secret, length=length)
        self._cli_man.printer.base.echo()
        self._show_result(password)
        self._cli_man.printer.base.echo()
        return password

    def normal(self, secret='', length=0):
        self._cli_man.printer.smart.echo("Normal Password Generator")
        if not secret:
            secret = self._prompt_secret()
        if not length or length <= 0:
            length = self._prompt_length()
        password = self._smart_pass_gen.get_smart_password(secret=secret, length=length)
        self._cli_man.printer.base.echo()
        self._show_result(password)
        self._cli_man.printer.base.echo()
        return password

    def base(self, length=0):
        if not length or length <= 0:
            length = self._prompt_length()
        self._cli_man.printer.smart.echo("Base Password Generator")
        password = self._smart_pass_gen.get_password(length=length)
        self._cli_man.printer.base.echo()
        self._show_result(password)
        self._cli_man.printer.base.echo()
        return password

    def _show_result(self, result):
        self._cli_man.printer.base.echo(result)

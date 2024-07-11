# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import getpass
import sys

from clipassgen.config import Config
from clipassgen.smart_pass_gen import SmartPasswordMaster
from clipassgen.smart_printer import SmartPrinter


class AppManager:
    
    def __init__(self):
        self.config = Config()
        self.smart_printer = SmartPrinter()
        self.smart_pass_gen = SmartPasswordMaster()

    def main_menu(self):
        self.smart_printer.show_head(text=self.config.name)
        while True:
            self.smart_printer.print_center('Main Menu:')
            print('1. Smart password generator (with login).')
            print('2. Smart password generator.')
            print('3. Base password generator.')
            print('0. Exit.')
            choice = input('Enter your choice: ')
            if choice == '1':
                self.generate_smart_password_with_login()
            elif choice == '2':
                self.generate_smart_password()
            elif choice == '3':
                self.generate_base_password()
            elif choice == '0':
                self.exit_app()
            else:
                self.smart_printer.print_framed('Error! Invalid choice')

    @staticmethod
    def _get_login():
        while True:
            login = input('Enter your login: ')
            if not login:
                print('Invalid login')
            return login

    @staticmethod
    def _get_secret():
        while True:
            secret = getpass.getpass("Enter secret phrase (hidden): ")
            if not secret:
                print('No secret phrase entered!')
                continue
            return secret

    @staticmethod
    def _get_length():
        while True:
            length = input('Enter length: ')
            try:
                length = int(length)
                if not length or (length < 10 or length > 1000):
                    raise ValueError
            except ValueError:
                print('Invalid length! (10-1000)')
                continue
            return length

    @staticmethod
    def _continue():
        input('Press enter to continue... ')

    def generate_smart_password_with_login(self):
        self.smart_printer.print_center(text='Smart Password (with login)')
        login = self._get_login()
        secret = self._get_secret()
        length = self._get_length()
        password = self.smart_pass_gen.get_smart_password(login, secret, length)
        self.show_password(password)

    def generate_smart_password(self):
        self.smart_printer.print_center(text='Smart Password')
        secret = self._get_secret()
        length = self._get_length()
        password = self.smart_pass_gen.get_smart_password(secret=secret, length=length)
        self.show_password(password)

    def generate_base_password(self):
        self.smart_printer.print_center(text='Base Password')
        length = self._get_length()
        password = self.smart_pass_gen.get_password(length=length)
        self.show_password(password)

    def show_password(self, password):
        print(f'\n{password}\n')
        self._continue()

    def exit_app(self):
        self.smart_printer.show_footer(url=self.config.url, copyright_=self.config.copyright_)
        sys.exit(0)

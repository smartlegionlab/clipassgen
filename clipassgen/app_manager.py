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

    @classmethod
    def main_menu(cls):
        SmartPrinter.show_head(text=Config.name)
        while True:
            SmartPrinter.print_center('Main Menu:')
            print('1. Smart password generator (with login).')
            print('2. Smart password generator.')
            print('3. Base password generator.')
            print('0. Exit.')
            choice = input('Enter your choice: ')
            if choice == '1':
                cls.generate_smart_password()
            elif choice == '2':
                cls.generate_default_smart_password()
            elif choice == '3':
                cls.generate_base_password()
            elif choice == '0':
                cls.exit_app()
            else:
                SmartPrinter.print_framed('Error! Invalid choice')

    @staticmethod
    def _get_login():
        while True:
            login = input('Enter your login: ')
            if not login:
                print('Invalid login')
            return login

    @staticmethod
    def _get_secret(security_flag=True):
        while True:
            if security_flag:
                secret = getpass.getpass("Enter secret phrase (hidden): ")
            else:
                secret = input('Enter secret phrase (hidden): ')
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
                print('Invalid length! Minimum length = 10. Maximum length = 1000.')
                continue
            return length

    @staticmethod
    def _continue():
        input('Press enter to continue... ')

    @classmethod
    def generate_smart_password(cls):
        SmartPrinter.print_center(text='Smart Password (with login)')
        login = cls._get_login()
        secret = cls._get_secret()
        length = cls._get_length()
        password = SmartPasswordMaster.generate_smart_password(login, secret, length)
        cls.show_password(password)

    @classmethod
    def generate_default_smart_password(cls):
        SmartPrinter.print_center(text='Smart Password')
        secret = cls._get_secret()
        length = cls._get_length()
        password = SmartPasswordMaster.generate_default_smart_password(secret=secret, length=length)
        cls.show_password(password)

    @classmethod
    def generate_base_password(cls):
        SmartPrinter.print_center(text='Base Password')
        length = cls._get_length()
        password = SmartPasswordMaster.generate_strong_password(length=length)
        cls.show_password(password)

    @classmethod
    def show_password(cls, password):
        print(f'\n{password}\n')
        cls._continue()

    @staticmethod
    def exit_app():
        SmartPrinter.show_footer(url=Config.url, copyright_=Config.copyright_)
        sys.exit(0)

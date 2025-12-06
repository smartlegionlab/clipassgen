# Copyright © 2025, Alexander Suvorov
import getpass
import sys

from clipassgen.config import Config
from clipassgen.smart_printer import SmartPrinter
from smartpasslib import SmartPasswordMaster


class AppManager:

    @classmethod
    def main_menu(cls):
        SmartPrinter.show_head(text=f"{Config.name} v2.1.0")
        cls._show_warning()

        while True:
            SmartPrinter.print_center('Main Menu:')
            print('1. Smart Password (from secret)')
            print('2. Strong Random Password')
            print('3. Base Random Password')
            print('4. Authentication Code')
            print('0. Exit')

            choice = input('Enter your choice: ')

            if choice == '1':
                cls.generate_smart_password()
            elif choice == '2':
                cls.generate_strong_password()
            elif choice == '3':
                cls.generate_base_password()
            elif choice == '4':
                cls.generate_code()
            elif choice == '0':
                cls.exit_app()
            else:
                SmartPrinter.print_framed('Error! Invalid choice')

    @staticmethod
    def _show_warning():
        print("\n" + "=" * 60)
        print("⚠️  CLIPASSGEN v2.1.0")
        print("=" * 60)
        print("• Login parameter removed")
        print("• All v1.x passwords are INVALID")
        print("• Only secret phrase needed")
        print("=" * 60)
        input("\nPress Enter to continue...")

    @staticmethod
    def _get_secret():
        while True:
            secret = getpass.getpass("Enter secret phrase (hidden): ")

            if not secret:
                print('Secret phrase cannot be empty!')
                continue

            secret2 = getpass.getpass("Confirm secret phrase (hidden): ")

            if secret != secret2:
                print('Secret phrases do not match!')
                continue

            return secret

    @staticmethod
    def _get_length(min_len=4, max_len=1000, default=12):
        while True:
            prompt = f'Enter length [{min_len}-{max_len}] (default {default}): '
            length_input = input(prompt)

            if not length_input:
                return default

            try:
                length = int(length_input)
                if length < min_len or length > max_len:
                    print(f'Length must be between {min_len} and {max_len}')
                    continue
                return length
            except ValueError:
                print('Please enter a valid number')
                continue

    @staticmethod
    def _continue():
        input('\nPress Enter to continue... ')

    @classmethod
    def generate_smart_password(cls):
        SmartPrinter.print_center(text='Smart Password Generator')
        print("\nGenerates password from your secret phrase.")
        print("Same secret + same length = same password every time.\n")

        secret = cls._get_secret()
        length = cls._get_length(min_len=4, max_len=1000, default=16)

        password = SmartPasswordMaster.generate_smart_password(
            secret=secret,
            length=length
        )

        cls._show_password(password)
        cls._show_public_key(secret)

    @classmethod
    def generate_strong_password(cls):
        SmartPrinter.print_center(text='Strong Password Generator')
        length = cls._get_length(min_len=4, max_len=1000, default=16)

        password = SmartPasswordMaster.generate_strong_password(length=length)
        cls._show_password(password)

    @classmethod
    def generate_base_password(cls):
        SmartPrinter.print_center(text='Base Password Generator')
        length = cls._get_length(min_len=4, max_len=1000, default=12)

        password = SmartPasswordMaster.generate_base_password(length=length)
        cls._show_password(password)

    @classmethod
    def generate_code(cls):
        SmartPrinter.print_center(text='Authentication Code Generator')
        length = cls._get_length(min_len=4, max_len=20, default=8)

        password = SmartPasswordMaster.generate_code(length=length)
        cls._show_password(password)

    @classmethod
    def _show_password(cls, password):
        SmartPrinter.print_framed('Generated Password:')
        print(password)
        print(f"\nLength: {len(password)} characters")
        cls._continue()

    @classmethod
    def _show_public_key(cls, secret):
        public_key = SmartPasswordMaster.generate_public_key(secret=secret)

        SmartPrinter.print_framed('Public Key (for verification):')
        print(public_key)
        print(f"\nStore this key to verify your secret later.")
        cls._continue()

    @staticmethod
    def exit_app():
        SmartPrinter.show_footer(url=Config.url, copyright_=Config.copyright_)
        sys.exit(0)

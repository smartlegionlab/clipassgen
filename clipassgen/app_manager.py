# Copyright © 2026, Alexander Suvorov
import getpass
import sys

from clipassgen.config import Config
from clipassgen.smart_printer import SmartPrinter
from smartpasslib import SmartPasswordMaster


class AppManager:
    smart_printer = SmartPrinter()
    smart_password_master = SmartPasswordMaster()
    config = Config()

    @classmethod
    def main_menu(cls):
        cls.smart_printer.show_head(text=f"{cls.config.name}")

        while True:
            cls.smart_printer.print_center('Main Menu:')
            print('1. Smart Password (from secret)')
            print('2. Strong Random Password')
            print('3. Base Random Password')
            print('4. Authentication Code')
            print('5. Help')
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
            elif choice == '5':
                cls._show_help()
            elif choice == '0':
                cls.exit_app()
            else:
                cls.smart_printer.print_framed('Error! Invalid choice')

    @classmethod
    def _show_help(cls):
        cls.smart_printer.print_center(text='Help')
        print(f"""
    CLIPASSGEN {cls.config.version} - Console Smart Password Generator

    DECENTRALIZED BY DESIGN:
    • No cloud, no database, no trust required
    • Your secrets never leave your device
    • There is no "forgot password" button — you are in complete control
    • Works offline — no internet connection needed

    HOW IT WORKS:
    1. Provide a secret phrase (minimum 12 characters)
    2. System generates a public key from the secret
    3. Password is generated deterministically
    4. Same secret + same length = same password across all platforms

    To generate a password:
    1. Choose generation mode
    2. Enter secret phrase (for smart mode)
    3. Copy the generated password

    GENERATION MODES:
    • Smart Password     — Deterministic from secret phrase (CROSS-PLATFORM!)
    • Strong Random      — Cryptographically secure random password
    • Base Random        — Simple random password
    • Authentication Code — Short code for 2FA/MFA (4-100 chars)

    SECURITY NOTES:
    • Passwords are NEVER stored anywhere
    • Secret phrases must be at least 12 characters
    • Case-sensitive secret phrases
    • Lost secret phrase = permanently lost passwords
    • Public key can be stored for verification

    CROSS-PLATFORM COMPATIBILITY:
    Same secret + same length = identical passwords on:
    • Python (Desktop, CLI)
    • C# (Desktop, CLI)
    • Web, Android, and all smartpasslib implementations

    COMMAND LINE MODE:
      clipassgen --smart -s "your_secret_phrase" -l 16
      clipassgen --strong -l 20
      clipassgen --code -l 8
      clipassgen --public -s "your_secret_phrase"
      clipassgen --verify -s "your_secret_phrase" -k "public_key"

    For more information, visit the project page on GitHub: {cls.config.url}

    """)
        cls.smart_printer.print_framed(f'Complete documentation: {cls.config.url}')
        input("\nPress Enter to continue...")

    @classmethod
    def _get_secret(cls):
        print("\nIMPORTANT: Your secret phrase (minimum 12 characters):")
        print("• Is case-sensitive")
        print("• Should be memorable but secure")
        print("• Will generate the same password every time")
        print("\nGood examples: 'MyCat🐱Hippo2026' or 'P@ssw0rd!LongSecret'")
        print("Bad examples: 'password123', 'qwerty', 'mysecret'\n")
        while True:

            secret = getpass.getpass("Enter secret phrase (hidden): ")

            if not secret:
                print('Secret phrase cannot be empty!')
                continue

            if len(secret) < 12:
                print(f'Error: Secret phrase must be at least 12 characters (current: {len(secret)})')
                continue

            secret2 = getpass.getpass("Confirm secret phrase (hidden): ")

            if secret != secret2:
                print('Secret phrases do not match!')
                continue

            return secret

    @classmethod
    def _get_length(cls, min_len=12, max_len=100, default=16):
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

    @classmethod
    def _get_code_length(cls, min_len=4, max_len=100, default=8):
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
        cls.smart_printer.print_center(text='Smart Password Generator')
        print("\nGenerates password from your secret phrase.")
        print("Same secret + same length = same password every time.\n")

        secret = cls._get_secret()
        length = cls._get_length(min_len=12, max_len=100, default=16)

        password = cls.smart_password_master.generate_smart_password(
            secret=secret,
            length=length
        )

        cls._show_password(password)
        cls._show_public_key(secret)

    @classmethod
    def generate_strong_password(cls):
        cls.smart_printer.print_center(text='Strong Password Generator')
        length = cls._get_length(min_len=12, max_len=100, default=16)

        password = cls.smart_password_master.generate_strong_password(length=length)
        cls._show_password(password)

    @classmethod
    def generate_base_password(cls):
        cls.smart_printer.print_center(text='Base Password Generator')
        length = cls._get_length(min_len=12, max_len=100, default=16)

        password = cls.smart_password_master.generate_base_password(length=length)
        cls._show_password(password)

    @classmethod
    def generate_code(cls):
        cls.smart_printer.print_center(text='Authentication Code Generator')
        length = cls._get_code_length(min_len=4, max_len=100, default=8)

        password = cls.smart_password_master.generate_code(length=length)
        cls._show_password(password)

    @classmethod
    def _show_password(cls, password):
        cls.smart_printer.print_framed('Generated Password:')
        print(password)
        print(f"\nLength: {len(password)} characters")
        cls._continue()

    @classmethod
    def _show_public_key(cls, secret):
        public_key = cls.smart_password_master.generate_public_key(secret=secret)

        cls.smart_printer.print_framed('Public Key (for verification):')
        print(public_key)
        print(f"\nStore this key to verify your secret later.")
        cls._continue()

    @classmethod
    def exit_app(cls):
        cls.smart_printer.show_footer(url=cls.config.url, copyright_=cls.config.copyright_)
        sys.exit(0)

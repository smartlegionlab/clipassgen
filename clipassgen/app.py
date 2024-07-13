# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Console Smart Passwords Generator."""
import argparse
import sys

from clipassgen.app_manager import AppManager


def cli():
    app_manager = AppManager()
    parser = argparse.ArgumentParser(description='Console Smart Passwords Generator.')
    parser.add_argument('-n', type=int, help='Number from 10 to 1000', default=None)
    parser.add_argument('-s', type=str, help='Secret phrase')
    parser.add_argument('-l', type=str, help='Login')

    args = parser.parse_args()

    length = args.n

    if length and not (10 <= length <= 1000):
        print("Error: -l should be a number between 10 and 1000.")
        sys.exit(0)

    secret = args.s
    login = args.l
    password = ''
    if length is None and secret is None and login is None:
        app_manager.main_menu()
    elif length is not None and login is not None and secret is None:
        print("Error: -s is required when using -n and -l together.")
    elif length is not None and login is not None and secret is not None:
        if login.strip() != "" and secret.strip() != "":
            password = app_manager.smart_pass_gen.get_smart_password(login, secret, length)
        else:
            print('Error! Exemple: python app.py -n 10 -l "login" -s "secret"')
    elif length is not None and secret is not None and login is None:
        if secret.strip() != "":
            password = app_manager.smart_pass_gen.get_default_password(secret, length)
        else:
            print("Error: -s should not be empty.")
    elif length is not None and secret is None and login is None:
        password = app_manager.smart_pass_gen.get_password(length)
    else:
        print("Invalid combination of arguments.")

    if password:
        print(f'{password}')


if __name__ == '__main__':
    cli()


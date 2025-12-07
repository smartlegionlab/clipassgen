# Copyright © 2025, Alexander Suvorov
"""Console Smart Passwords Generator."""
import argparse
import sys

from clipassgen.app_manager import AppManager
from smartpasslib import SmartPasswordMaster


def cli():
    parser = argparse.ArgumentParser(description='Console Smart Passwords Generator v2.1.3')

    parser.add_argument('-l', '--length', type=int, help='Password length (4-1000)', default=12)
    parser.add_argument('-s', '--secret', type=str, help='Secret phrase for smart password')

    parser.add_argument('--smart', action='store_true', help='Generate smart password from secret')
    parser.add_argument('--strong', action='store_true', help='Generate strong random password')
    parser.add_argument('--base', action='store_true', help='Generate base random password')
    parser.add_argument('--code', action='store_true', help='Generate authentication code')

    args = parser.parse_args()

    if args.length < 4 or args.length > 1000:
        print("Error: Length must be between 4 and 1000")
        sys.exit(1)

    if not any([args.smart, args.strong, args.base, args.code]) and not args.secret:
        AppManager.main_menu()
        return

    smart_password_master = SmartPasswordMaster()

    password = ''

    if args.smart and args.secret:
        password = smart_password_master.generate_smart_password(
            secret=args.secret,
            length=args.length
        )

    elif args.strong:
        password = smart_password_master.generate_strong_password(args.length)

    elif args.base:
        password = smart_password_master.generate_base_password(args.length)

    elif args.code:
        password = smart_password_master.generate_code(args.length)

    else:
        print("Error: Invalid arguments")
        print("Examples:")
        print("  clipassgen --smart -s 'mysecret' -l 16")
        print("  clipassgen --strong -l 20")
        print("  clipassgen --code -l 8")
        sys.exit(1)

    if password:
        print(password)


if __name__ == '__main__':
    cli()

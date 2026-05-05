# Copyright © 2026, Alexander Suvorov
"""Console Smart Passwords Generator."""
import argparse
import sys

from clipassgen.app_manager import AppManager
from smartpasslib import SmartPasswordMaster


def cli():
    parser = argparse.ArgumentParser(description='Console Smart Passwords Generator v4.0.0')

    parser.add_argument('-l', '--length', type=int, help='Password length (12-100) or code length (4-100)', default=12)
    parser.add_argument('-s', '--secret', type=str, help='Secret phrase for smart password')
    parser.add_argument('-k', '--key', type=str, help='Public key for verification')

    parser.add_argument('--smart', action='store_true', help='Generate smart password from secret')
    parser.add_argument('--strong', action='store_true', help='Generate strong random password')
    parser.add_argument('--base', action='store_true', help='Generate base random password')
    parser.add_argument('--code', action='store_true', help='Generate authentication code')
    parser.add_argument('--public', action='store_true', help='Generate public key from secret')
    parser.add_argument('--verify', action='store_true', help='Verify secret against public key')

    args = parser.parse_args()

    if not any([args.smart, args.strong, args.base, args.code, args.public, args.verify]) and not args.secret:
        AppManager.main_menu()
        return

    smart_password_master = SmartPasswordMaster()

    if args.public:
        if not args.secret:
            print("Error: --public requires -s/--secret")
            sys.exit(1)
        try:
            public_key = smart_password_master.generate_public_key(secret=args.secret)
            print(f"Public key: {public_key}")
            print("\nStore this key to verify your secret later.")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        return

    if args.verify:
        if not args.secret or not args.key:
            print("Error: --verify requires -s/--secret and -k/--key")
            sys.exit(1)
        try:
            is_valid = smart_password_master.check_public_key(
                secret=args.secret,
                public_key=args.key
            )
            if is_valid:
                print("Verification successful: Secret matches the public key")
            else:
                print("Verification failed: Secret does NOT match the public key")
                sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        return

    if args.code:
        if args.length < 4 or args.length > 100:
            print("Error: Code length must be between 4 and 100")
            sys.exit(1)
        try:
            password = smart_password_master.generate_code(args.length)
            print(password)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        return

    if args.length < 12 or args.length > 100:
        print("Error: Password length must be between 12 and 100")
        sys.exit(1)

    if args.smart and not args.secret:
        print("Error: --smart requires -s/--secret")
        sys.exit(1)

    password = None

    if args.smart and args.secret:
        try:
            password = smart_password_master.generate_smart_password(
                secret=args.secret,
                length=args.length
            )
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    elif args.strong:
        try:
            password = smart_password_master.generate_strong_password(args.length)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    elif args.base:
        try:
            password = smart_password_master.generate_base_password(args.length)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    else:
        print("Error: Invalid arguments")
        print("Examples:")
        print("  clipassgen --smart -s 'my_strong_secret' -l 16")
        print("  clipassgen --strong -l 20")
        print("  clipassgen --base -l 16")
        print("  clipassgen --code -l 8")
        print("  clipassgen --public -s 'my_strong_secret'")
        print("  clipassgen --verify -s 'my_strong_secret' -k 'public_key'")
        sys.exit(1)

    if password:
        print(password)


if __name__ == '__main__':
    cli()

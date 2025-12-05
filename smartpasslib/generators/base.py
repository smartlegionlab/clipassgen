# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
import random
import string


class BasePasswordGenerator:
    """
    Generator for basic random passwords.
    """

    letters = string.ascii_letters
    digits = string.digits
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length: int = 12) -> str:
        """
        Generate a random password of specified length.

        Args:
            length: Length of password to generate (default: 12)

        Returns:
            str: Randomly generated password
        """
        symbols_string = cls.letters + cls.digits + cls.symbols
        return ''.join((random.choice(symbols_string) for _ in range(length)))

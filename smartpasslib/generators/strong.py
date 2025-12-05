# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
import secrets
import string


class StrongPasswordGenerator:
    """
    Generator for cryptographically strong random passwords.

    Guarantees at least one character from each character class.
    """

    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length: int = 12) -> str:
        """
        Generate strong password with guaranteed character diversity.

        Args:
            length: Password length, minimum 4

        Returns:
            str: Cryptographically strong password

        Raises:
            ValueError: If length is less than 4
        """
        if length < 4:
            raise ValueError("The length cannot be less than 4.")

        result = [
            secrets.choice(cls.upper_letters),
            secrets.choice(cls.lower_letters),
            secrets.choice(cls.digits),
            secrets.choice(cls.symbols),
        ]
        result += [
            secrets.choice(cls.upper_letters + cls.lower_letters + cls.digits + cls.symbols)
            for _ in range(length - 4)
        ]
        secrets.SystemRandom().shuffle(result)
        return ''.join(result)

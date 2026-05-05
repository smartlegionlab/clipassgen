# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import secrets

from smartpasslib.core.chars import PasswordChars


class StrongPasswordGenerator(PasswordChars):
    """
    Generator for cryptographically strong random passwords.

    Guarantees at least one character from each character class.
    """

    @classmethod
    def generate(cls, length: int = 12) -> str:
        """
        Generate strong password with guaranteed character diversity.

        Args:
            length: Password length, minimum 12, maximum 100

        Returns:
            str: Cryptographically strong password

        Raises:
            ValueError: If length is less than 12 or greater than 100
        """
        if length < 12:
            raise ValueError("Password length must be at least 12 characters")
        if length > 100:
            raise ValueError("Password length cannot exceed 100 characters")

        result = [
            secrets.choice(cls.lowercase),
            secrets.choice(cls.uppercase),
            secrets.choice(cls.digits),
            secrets.choice(cls.symbols),
        ]
        result += [
            secrets.choice(cls.all())
            for _ in range(length - 4)
        ]
        secrets.SystemRandom().shuffle(result)
        return ''.join(result)

# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import secrets

from smartpasslib.core.chars import PasswordChars


class BasePasswordGenerator(PasswordChars):
    """
    Generator for cryptographically secure random passwords.
    """

    @classmethod
    def generate(cls, length: int = 12) -> str:
        """
        Generate a cryptographically secure random password.

        Args:
            length: Length of password to generate (default: 12)

        Returns:
            str: Randomly generated password (different every time)
        """
        return ''.join(secrets.choice(cls.all()) for _ in range(length))

    @classmethod
    def generate_token(cls, bytes_count: int = 32) -> str:
        """
        Generate a random hex token (e.g., for API keys).

        Args:
            bytes_count: Number of random bytes (default: 32)

        Returns:
            str: Hexadecimal string of length bytes_count * 2
        """
        return secrets.token_hex(bytes_count)

    @classmethod
    def generate_urlsafe_token(cls, bytes_count: int = 32) -> str:
        """
        Generate a URL-safe random token.

        Args:
            bytes_count: Number of random bytes (default: 32)

        Returns:
            str: URL-safe base64 encoded string
        """
        return secrets.token_urlsafe(bytes_count)

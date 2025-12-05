# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
from smartpasslib.generators.hash import HashGenerator


class SmartKeyGenerator:
    """
    Generator for cryptographic keys from secret phrases.
    """

    @classmethod
    def _create_key(cls, secret, steps: int = 30) -> str:
        """
        Internal method to create a key through iterative hashing.
        """
        all_hash = cls.get_hash(secret)
        for i in range(steps):
            temp_string = f"{all_hash}:{secret}:{i}"
            all_hash = cls.get_hash(temp_string)
        return cls.get_hash(all_hash)

    @classmethod
    def generate_public_key(cls, secret) -> str:
        """
        Generate a public verification key from secret phrase.

        Args:
            secret: Secret phrase

        Returns:
            str: Public key for verification
        """
        return cls._create_key(secret=secret, steps=60)

    @classmethod
    def generate_private_key(cls, secret) -> str:
        """
        Generate a private key from secret phrase.

        Args:
            secret: Secret phrase

        Returns:
            str: Private key
        """
        return cls._create_key(secret=secret, steps=30)

    @classmethod
    def check_key(cls, secret: str, key: str) -> bool:
        """
        Verify if a key matches the secret phrase.

        Args:
            secret: Secret phrase to check
            key: Key to verify

        Returns:
            bool: True if key was generated from this secret
        """
        return cls.generate_public_key(secret=secret) == key

    @classmethod
    def get_hash(cls, text: str = '') -> str:
        """
        Generate SHA3-512 hash of text.

        Args:
            text: Input text

        Returns:
            str: Hexadecimal hash
        """
        text = str(text)
        return HashGenerator.generate(str(text.encode('utf-8')))

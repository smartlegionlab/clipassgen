# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import hashlib


class SmartKeyGenerator:
    """
    Generator for cryptographic keys from secret phrases.
    Uses SHA-256 for cross-platform compatibility.
    """

    @classmethod
    def _create_key(cls, secret: str, steps: int = 30) -> str:
        """
        Internal method to create a key through iterative hashing.
        """
        all_hash = cls.get_hash(secret)
        for i in range(steps):
            temp_string = f"{all_hash}:{secret}:{i}"
            all_hash = cls.get_hash(temp_string)
        return all_hash

    @classmethod
    def generate_public_key(cls, secret: str) -> str:
        """
        Generate a public verification key from secret phrase.
        """
        return cls._create_key(secret=secret, steps=60)

    @classmethod
    def generate_private_key(cls, secret: str) -> str:
        """
        Generate a private key from secret phrase.
        """
        return cls._create_key(secret=secret, steps=30)

    @classmethod
    def check_key(cls, secret: str, key: str) -> bool:
        """
        Verify if a key matches the secret phrase.
        """
        return cls.generate_public_key(secret=secret) == key

    @classmethod
    def get_hash(cls, text: str = '') -> str:
        """
        Generate SHA-256 hash of text (cross-platform!).
        """
        text = str(text)
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

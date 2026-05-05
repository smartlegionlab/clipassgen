# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import hashlib


class SmartKeyGenerator:
    """
    Generator for cryptographic keys from secret phrases.
    Uses SHA-256 for cross-platform compatibility.
    """

    @staticmethod
    def _validate_secret(secret: str) -> None:
        """
        Validate secret phrase length.

        Args:
            secret: Secret phrase to validate

        Raises:
            ValueError: If secret is less than 12 characters
        """
        if len(str(secret)) < 12:
            raise ValueError("Secret phrase must be at least 12 characters")

    @classmethod
    def _get_steps_from_secret(cls, secret: str, min_steps: int, max_steps: int, salt: str = "") -> int:
        """
        Get deterministic steps count based on secret hash.

        Args:
            secret: Secret phrase
            min_steps: Minimum steps
            max_steps: Maximum steps
            salt: Salt to add to secret for different step calculations

        Returns:
            int: Steps count between min_steps and max_steps
        """
        hash_value = cls.get_hash(f"{secret}:{salt}")
        hash_int = int(hash_value[:8], 16)
        steps = min_steps + (hash_int % (max_steps - min_steps + 1))
        return steps

    @classmethod
    def _create_key(cls, secret: str, steps: int, salt: str = "") -> str:
        """
        Internal method to create a key through iterative hashing.
        """
        all_hash = cls.get_hash(f"{secret}:{salt}")
        for i in range(steps):
            temp_string = f"{all_hash}:{i}"
            all_hash = cls.get_hash(temp_string)
        return all_hash

    @classmethod
    def generate_public_key(cls, secret: str) -> str:
        """Generate a public verification key from secret phrase."""
        cls._validate_secret(secret)
        steps = cls._get_steps_from_secret(secret, 45, 60, salt="public")
        return cls._create_key(secret=secret, steps=steps, salt="public")

    @classmethod
    def generate_private_key(cls, secret: str) -> str:
        """Generate a private key from secret phrase."""
        cls._validate_secret(secret)
        steps = cls._get_steps_from_secret(secret, 15, 30, salt="private")
        return cls._create_key(secret=secret, steps=steps, salt="private")

    @classmethod
    def check_key(cls, secret: str, key: str) -> bool:
        """
        Verify if a key matches the secret phrase.
        """
        cls._validate_secret(secret)
        return cls.generate_public_key(secret=secret) == key

    @classmethod
    def get_hash(cls, text: str = '') -> str:
        """
        Generate SHA-256 hash of text (cross-platform!).
        """
        text = str(text)
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

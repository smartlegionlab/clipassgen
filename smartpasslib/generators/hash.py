# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import hashlib


class HashGenerator:
    """
    Generator for cryptographic hash values.
    Uses SHA-256 for cross-platform compatibility.
    """

    @classmethod
    def generate(cls, text: str) -> str:
        """
        Generate SHA-256 hash for the given text.

        Args:
            text: Input text to hash

        Returns:
            str: Hexadecimal SHA-256 hash (64 characters)
        """
        text = str(text)
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

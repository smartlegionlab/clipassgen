# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
import hashlib


class HashGenerator:
    """
    Generator for cryptographic hash values.
    """

    @classmethod
    def generate(cls, text: str) -> str:
        """
        Generate SHA3-512 hash for the given text.

        Args:
            text: Input text to hash

        Returns:
            str: Hexadecimal SHA3-512 hash
        """
        text = str(text)
        sha = hashlib.sha3_512(text.encode('utf-8'))
        return sha.hexdigest()

# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import hashlib

from smartpasslib import SmartKeyGenerator
from smartpasslib.core.chars import PasswordChars


class SmartPasswordGenerator(PasswordChars):
    """
    Generator for deterministic cross-platform smart passwords.

    Uses SHA-256 to generate reproducible passwords from a seed string.
    The same seed and length will produce identical passwords on any platform
    that implements SHA-256.
    """

    @classmethod
    def generate(cls, seed: str, length: int = 12) -> str:
        """
        Generate a deterministic smart password from a seed string.

        Args:
            seed: String that determines the password (same seed = same password)
            length: Length of password to generate (default: 12)

        Returns:
            str: Deterministically generated smart password
        """
        seed = SmartKeyGenerator.generate_private_key(secret=seed)
        result = []
        counter = 0

        while len(result) < length:
            data = f"{seed}:{counter}".encode()
            hash_bytes = hashlib.sha256(data).digest()

            for byte in hash_bytes:
                if len(result) < length:
                    result.append(cls.all()[byte % len(cls.all())])
            counter += 1

        return ''.join(result)

# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
import os


class UrandomGenerator:
    """
    OS cryptographic random bytes generator using urandom.
    """

    @classmethod
    def generate(cls, size: int = 32) -> bytes:
        """
        Generate cryptographically secure random bytes.

        Args:
            size: Number of bytes to generate (default: 32)

        Returns:
            bytes: Random bytes from OS cryptographic source
        """
        return os.urandom(size)

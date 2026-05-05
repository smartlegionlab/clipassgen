# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import os


class UrandomGenerator:
    """
    OS cryptographic random bytes generator using urandom.
    """

    @classmethod
    def generate(cls, size: int = 32) -> bytes:
        """Generate cryptographically secure random bytes."""
        if size < 1:
            raise ValueError("Size must be at least 1 byte")
        if size > 1024 * 1024:
            raise ValueError("Size cannot exceed 1 MB")
        return os.urandom(size)

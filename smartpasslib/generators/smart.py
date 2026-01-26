# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import random
from typing import Union

from smartpasslib.generators.base import BasePasswordGenerator


class SmartPasswordGenerator:
    """
    Deterministic password generator using seed-based randomness.

    Generates reproducible passwords from cryptographic seeds.
    """

    @classmethod
    def generate(cls, seed: Union[str, bytes], length: int = 15) -> str:
        """
        Generate deterministic password from seed.

        Args:
            seed: Cryptographic seed for deterministic generation
            length: Password length (default: 15)

        Returns:
            str: Deterministically generated password
        """
        original_state = random.getstate()
        random.seed(seed)
        password = BasePasswordGenerator.generate(length)
        random.setstate(original_state)
        return password

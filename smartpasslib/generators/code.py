# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import secrets

from smartpasslib.core.chars import PasswordChars


class CodeGenerator(PasswordChars):
    """
    Generator for secure codes with guaranteed character sets.
    """

    @classmethod
    def generate(cls, length: int = 6) -> str:
        """
        Generate a secure code with at least one character from each required set.

        Args:
            length: Code length, minimum 4 characters

        Returns:
            str: Generated code

        Raises:
            ValueError: If length is less than 4
        """
        if length < 4:
            raise ValueError("The code length must be at least 4 characters..")

        code = [
            secrets.choice(cls.lowercase),
            secrets.choice(cls.uppercase),
            secrets.choice(cls.digits),
            secrets.choice(cls.symbols)
        ]

        code += [secrets.choice(cls.all()) for _ in range(length - 4)]

        secrets.SystemRandom().shuffle(code)

        return ''.join(code)

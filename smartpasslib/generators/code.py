# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import secrets
import string


class CodeGenerator:
    """
    Generator for secure codes with guaranteed character sets.
    """

    special_chars = "!@#$%^&*"

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

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits

        code = [
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits),
            secrets.choice(cls.special_chars)
        ]

        all_chars = lowercase + uppercase + digits + cls.special_chars
        code += [secrets.choice(all_chars) for _ in range(length - 4)]

        secrets.SystemRandom().shuffle(code)

        return ''.join(code)

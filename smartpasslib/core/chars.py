# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import string


class PasswordChars:
    """
    Shared character sets for all password generators.
    Centralized to avoid duplication across classes.
    """

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    letters = lowercase + uppercase
    digits = string.digits
    symbols = '!@#$&*-_'

    @classmethod
    def all(cls) -> str:
        """All characters combined"""
        return cls.letters + cls.digits + cls.symbols

    @classmethod
    def without_symbols(cls) -> str:
        """Letters and digits only"""
        return cls.letters + cls.digits

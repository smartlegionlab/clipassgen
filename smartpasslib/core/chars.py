# Copyright (©) 2026, Alexander Suvorov. All rights reserved.


class PasswordChars:
    """
    Shared character sets for all password generators.
    Centralized to avoid duplication across classes.
    !!! CROSS-PLATFORM STANDARD !!!
    All implementations (Python, C#, Go, JS, Kotlin) MUST use this exact string:
    "!@#$%^&*()_+-=[]{};:,.<>?/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    """
    BASE_STRING = "!@#$%^&*()_+-=[]{};:,.<>?/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = '!@#$%^&*()_+-=[]{};:,.<>?/'

    @classmethod
    def all(cls) -> str:
        """All characters combined"""
        return cls.symbols + cls.uppercase + cls.digits + cls.lowercase

    @classmethod
    def without_symbols(cls) -> str:
        """Letters and digits only"""
        return cls.uppercase + cls.digits + cls.lowercase

# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
from smartpasslib import CodeGenerator
from smartpasslib.generators.base import BasePasswordGenerator
from smartpasslib.generators.key import SmartKeyGenerator
from smartpasslib.generators.smart import SmartPasswordGenerator
from smartpasslib.generators.strong import StrongPasswordGenerator


class SmartPasswordMaster:
    """
    Main interface for password generation and key management.
    """

    @staticmethod
    def generate_code(length: int = 8) -> str:
        """
        Generate secure verification code.

        Args:
            length: Code length (default: 8)

        Returns:
            str: Generated code
        """
        return CodeGenerator.generate(length)

    @staticmethod
    def generate_base_password(length: int = 12) -> str:
        """
        Generate random base password.

        Args:
            length: Password length (default: 12)

        Returns:
            str: Generated password
        """
        return BasePasswordGenerator.generate(length=length)

    @staticmethod
    def generate_strong_password(length: int = 12) -> str:
        """
        Generate cryptographically strong password.

        Args:
            length: Password length (default: 12)

        Returns:
            str: Generated password
        """
        return StrongPasswordGenerator.generate(length=length)

    @classmethod
    def generate_smart_password(cls, secret, length: int = 12) -> str:
        """
        Generate deterministic password from secret phrase.

        Args:
            secret: Secret phrase
            length: Password length (default: 12)

        Returns:
            str: Generated password
        """
        seed = SmartKeyGenerator.generate_private_key(secret=secret)
        return SmartPasswordGenerator.generate(seed, length=length)

    @classmethod
    def generate_public_key(cls, secret: str) -> str:
        """
        Generate public verification key from secret.

        Args:
            secret: Secret phrase

        Returns:
            str: Public key for verification
        """
        return SmartKeyGenerator.generate_public_key(secret=secret)

    @classmethod
    def generate_private_key(cls, secret: str) -> str:
        """
        Generate private key from secret phrase.

        Args:
            secret: Secret phrase

        Returns:
            str: Private key
        """
        return SmartKeyGenerator.generate_public_key(secret=secret)

    @classmethod
    def check_public_key(cls, secret: str, public_key: str) -> bool:
        """
        Verify if public key matches secret phrase.

        Args:
            secret: Secret phrase to verify
            public_key: Public key to check

        Returns:
            bool: True if key was generated from this secret
        """
        return SmartKeyGenerator.check_key(secret, public_key)

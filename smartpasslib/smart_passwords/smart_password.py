# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
from typing import Dict


class SmartPassword:
    """
    Metadata container for smart password verification and generation.

    Stores only verification data, not actual passwords or secrets.
    """

    def __init__(self, public_key: str, description: str, length: int = 12):
        """
        Initialize smart password metadata.

        Args:
            public_key: Public verification key for secret phrase
            description: Service/account description
            length: Password length to generate (default: 12)
        """
        self._public_key = public_key
        self._description = description
        self._length = length

    @property
    def public_key(self) -> str:
        """
        Public verification key.

        Returns:
            str: Key for verifying secret phrase knowledge
        """
        return self._public_key

    @property
    def description(self) -> str:
        """
        Service/account description.

        Returns:
            str: Human-readable description
        """
        return self._description

    @property
    def length(self) -> int:
        """
        Password length.

        Returns:
            int: Length of password to generate
        """
        return self._length

    def to_dict(self) -> Dict[str, str | int]:
        """
        Convert to dictionary for serialization.

        Returns:
            Dict[str, str | int]: Dictionary representation
        """
        return {
            "public_key": self._public_key,
            "description": self._description,
            "length": self._length
        }

    @staticmethod
    def from_dict(data: Dict[str, str | int]) -> 'SmartPassword':
        """
        Create instance from dictionary.

        Args:
            data: Dictionary with public_key, description, and length

        Returns:
            SmartPassword: Reconstructed instance
        """
        return SmartPassword(
            public_key=data['public_key'],
            description=data['description'],
            length=data['length']
        )

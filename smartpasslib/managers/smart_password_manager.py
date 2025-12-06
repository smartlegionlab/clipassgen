# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
import json
import os
from typing import Dict, Optional

from smartpasslib.masters.smart_password_master import SmartPasswordMaster
from smartpasslib.factories.smart_password_factory import SmartPasswordFactory
from smartpasslib.smart_passwords.smart_password import SmartPassword


class SmartPasswordManager:
    """
    Manager for smart password metadata storage and operations.

    Stores only verification data, not actual passwords or secrets.
    """

    def __init__(self, filename: str = '~/.cases.json'):
        """
        Initialize manager with storage file.

        Args:
            filename: Path to JSON storage file (default: ~/.cases.json)
        """
        self.filename = os.path.expanduser(filename)
        self.smart_passwords = self._load_data()
        self.smart_pass_factory = SmartPasswordFactory()

    @property
    def passwords(self) -> Dict[str, SmartPassword]:
        """
        Get all stored smart password metadata.

        Returns:
            Dict[str, SmartPassword]: Dictionary mapping public keys to password metadata
        """
        return self.smart_passwords

    @staticmethod
    def generate_base_password(length: int = 12) -> str:
        """
        Generate random base password.

        Args:
            length: Password length (default: 12)

        Returns:
            str: Generated password
        """
        return SmartPasswordMaster.generate_strong_password(length)

    @classmethod
    def generate_smart_password(cls, secret: str, length: int = 12) -> str:
        """
        Generate deterministic smart password from secret.

        Args:
            secret: Secret phrase
            length: Password length (default: 12)

        Returns:
            str: Generated password
        """
        return SmartPasswordMaster.generate_smart_password(secret, length)

    @classmethod
    def generate_public_key(cls, secret: str) -> str:
        """
        Generate public verification key from secret.

        Args:
            secret: Secret phrase

        Returns:
            str: Public verification key
        """
        return SmartPasswordMaster.generate_public_key(secret)

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
        return SmartPasswordMaster.check_public_key(secret, public_key)

    def add_smart_password(self, smart_password: SmartPassword):
        """
        Add smart password metadata to storage.

        Args:
            smart_password: SmartPassword object with verification data
        """
        self.smart_passwords[smart_password.public_key] = smart_password
        self._write_data()

    def get_smart_password(self, public_key: str) -> Optional[SmartPassword]:
        """
        Retrieve smart password metadata by public key.

        Args:
            public_key: Public verification key

        Returns:
            Optional[SmartPassword]: Password metadata or None if not found
        """
        return self.smart_passwords.get(public_key)

    def update_smart_password(self, public_key: str, description: str = None, length: int = None) -> bool:
        """
        Update metadata of an existing smart password.

        Args:
            public_key: Public key of the password to update
            description: New description (optional)
            length: New password length (optional)

        Returns:
            bool: True if update was successful, False if password not found

        Raises:
            ValueError: If length is provided and less than 1
        """
        password = self.get_smart_password(public_key)
        if password is None:
            return False

        password.update(description=description, length=length)
        self._write_data()
        return True

    def delete_smart_password(self, public_key: str):
        """
        Delete smart password metadata by public key.

        Args:
            public_key: Public verification key

        Raises:
            KeyError: If public key not found
        """
        if public_key in self.smart_passwords:
            del self.smart_passwords[public_key]
            self._write_data()
        else:
            raise KeyError("Public Key not found.")

    def clear(self):
        """
        Clear all stored password metadata.
        """
        self.smart_passwords = {}

    @property
    def password_count(self) -> int:
        """
        Get number of stored password metadata entries.

        Returns:
            int: Number of entries
        """
        return len(self.smart_passwords)

    def _load_data(self) -> Dict[str, SmartPassword]:
        """
        Load passwords metadata from storage file.

        Returns:
            Dict[str, SmartPassword]: Loaded password metadata
        """
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return {public_key: SmartPassword.from_dict(item) for public_key, item in data.items()}
        else:
            return {}

    def _write_data(self):
        """
        Write passwords metadata to storage file.
        """
        with open(self.filename, 'w') as f:
            json.dump({public_key: sp.to_dict() for public_key, sp in self.smart_passwords.items()}, f, indent=4)

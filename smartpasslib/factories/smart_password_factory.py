# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
from smartpasslib.smart_passwords.smart_password import SmartPassword


class SmartPasswordFactory:
    """
    Factory class for creating SmartPassword objects.
    """

    @classmethod
    def create_smart_password(cls, public_key: str, description: str, length: int = 12) -> SmartPassword:
        """
        Create a new SmartPassword instance.

        Args:
            public_key: Public key for verifying secret phrase knowledge
            description: Service/account description
            length: Password length (default: 12)

        Returns:
            SmartPassword: Configured smart password object
        """
        return SmartPassword(public_key=public_key, description=description, length=length)

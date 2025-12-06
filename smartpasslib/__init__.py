# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
"""Smart Passwords Library: Cryptographic password generation and management without storage.
Generate passwords from secrets, verify knowledge without exposure, manage metadata securely."""
from smartpasslib.factories.smart_password_factory import SmartPasswordFactory
from smartpasslib.generators.base import BasePasswordGenerator
from smartpasslib.generators.hash import HashGenerator
from smartpasslib.generators.key import SmartKeyGenerator
from smartpasslib.generators.smart import SmartPasswordGenerator
from smartpasslib.generators.strong import StrongPasswordGenerator
from smartpasslib.generators.urandom import UrandomGenerator
from smartpasslib.generators.code import CodeGenerator
from smartpasslib.managers.smart_password_manager import SmartPasswordManager
from smartpasslib.masters.smart_password_master import SmartPasswordMaster
from smartpasslib.smart_passwords.smart_password import SmartPassword
__version__ = '2.1.0'
__author__ = 'A.A. Suvorov'
__all__ = [
    "SmartPasswordMaster",
    "HashGenerator",
    "UrandomGenerator",
    "SmartKeyGenerator",
    "BasePasswordGenerator",
    "StrongPasswordGenerator",
    "SmartPasswordGenerator",
    "SmartPasswordFactory",
    "SmartPasswordManager",
    "SmartPassword",
    "CodeGenerator",
]

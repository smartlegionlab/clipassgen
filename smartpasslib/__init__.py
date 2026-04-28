# ----------------------------------------------------------------------------------------------------------------------
# SmartPassLib v3.0.2 - Python smart password library - Cross-platform deterministic password generation
# ----------------------------------------------------------------------------------------------------------------------
# Cryptographic password generation and management without storage. Generate passwords from secrets,
# verify knowledge without exposure, manage metadata securely.
# Same secret phrase + same length = same password across all platforms.
# Decentralized by design — no central servers, no cloud dependency, no third-party trust required.
#
# Compatible with SmartPassLib C#/JS/Kotlin/Go implementations
#
# Key derivation:
#
#  - Private key: 30 iterations of SHA-256 (used for password generation,
#    never stored anywhere, generated on the fly, upon request)
#  - Public Key: 60 iterations of SHA-256 (used for verification,
#    stored locally, does not require secure storage)
#
# Secret phrase:
#   - is not transferred anywhere
#   - is not stored anywhere
#   - is required to generate the private key when creating a smart password
#
# ----------------------------------------------------------------------------------------------------------------------
# Ecosystem:
#   - Core library (Python): https://github.com/smartlegionlab/smartpasslib
#   - Core library (JS): https://github.com/smartlegionlab/smartpasslib-js
#   - Core library (Kotlin): https://github.com/smartlegionlab/smartpasslib-kotlin
#   - Core library (Go): https://github.com/smartlegionlab/smartpasslib-go
#   - Core library (C#): https://github.com/smartlegionlab/smartpasslib-csharp
#   - Desktop Python: https://github.com/smartlegionlab/smart-password-manager-desktop
#   - Desktop C#: https://github.com/smartlegionlab/SmartPasswordManagerCsharpDesktop
#   - CLI Manager Python: https://github.com/smartlegionlab/clipassman
#   - CLI Manager C#: https://github.com/smartlegionlab/SmartPasswordManagerCsharpCli
#   - CLI Generator Python: https://github.com/smartlegionlab/clipassgen
#   - CLI Generator C#: https://github.com/smartlegionlab/SmartPasswordGeneratorCsharpCli
#   - Web: https://github.com/smartlegionlab/smart-password-manager-web
#   - Android: https://github.com/smartlegionlab/smart-password-manager-android
# ----------------------------------------------------------------------------------------------------------------------
# Author: Alexander Suvorov https://github.com/smartlegionlab
# License: BSD 3-Clause https://github.com/smartlegionlab/smartpasslib/blob/master/LICENSE
# ----------------------------------------------------------------------------------------------------------------------
# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
# ----------------------------------------------------------------------------------------------------------------------
"""Smart Passwords Library: Cryptographic password generation and management without storage.
Generate passwords from secrets, verify knowledge without exposure, manage metadata securely.

Decentralized by design — no central servers, no cloud dependency, no third-party trust required.
"""

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

__version__ = '3.0.2'
__author__ = 'Alexander Suvorov'

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

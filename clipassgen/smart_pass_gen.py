# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import hashlib
import os
import random
import secrets
import string


class HashGenerator:
    @classmethod
    def generate(cls, text: str):
        text = str(text)
        sha = hashlib.sha3_512(text.encode('utf-8'))
        new_hash = sha.hexdigest()
        return new_hash


class UrandomGenerator:
    @classmethod
    def generate(cls, size=32):
        return os.urandom(size)


class SmartKeyGenerator:
    _hash_master = HashGenerator()

    @classmethod
    def _create_key(cls, login='', secret='', public_step=15):
        login_hash = cls._get_hash(text=login)
        secret_hash = cls._get_hash(text=secret)
        all_hash = cls._get_hash(text=login_hash + secret_hash)
        for _ in range(public_step):
            temp_hash = cls._get_hash(all_hash)
            all_hash = cls._get_hash(all_hash + temp_hash + secret_hash)
        return cls._get_hash(all_hash)

    @classmethod
    def get_public_key(cls, login='', secret=''):
        return cls._create_key(login, secret, 15)

    @classmethod
    def get_private_key(cls, login='', secret=''):
        return cls._create_key(login, secret, 30)

    @classmethod
    def check_data(cls, login='', secret='', key=''):
        return cls.get_public_key(login=login, secret=secret) == key

    @classmethod
    def _get_hash(cls, text=''):
        text = str(text)
        return cls._hash_master.generate(str(text.encode('utf-8')))


class BasePasswordGenerator:
    letters = string.ascii_letters
    digits = string.digits
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length=10):
        symbols_string = cls.letters + cls.digits + cls.symbols
        return ''.join((random.choice(symbols_string) for _ in range(length)))


class StrongPasswordGenerator:
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length: int = 10) -> str:
        if length < 4:
            raise ValueError("The length cannot be less than 4.")

        result = [
            secrets.choice(cls.upper_letters),
            secrets.choice(cls.lower_letters),
            secrets.choice(cls.digits),
            secrets.choice(cls.symbols),
        ]
        result += [
            secrets.choice(cls.upper_letters + cls.lower_letters + cls.digits + cls.symbols)
            for _ in range(length - 4)
        ]
        secrets.SystemRandom().shuffle(result)
        return ''.join(result)


class SmartPasswordGenerator:
    @classmethod
    def generate(cls, seed='', length=15, size=32) -> str:
        if not seed:
            seed = cls.get_seed(size)
        cls._set_seed(seed)
        password = BasePasswordGenerator.generate(length)
        seed = str(cls.get_seed())
        cls._set_seed(seed)
        return password

    @classmethod
    def _set_seed(cls, seed):
        seed = str(seed)
        random.seed(seed)
        return seed

    @classmethod
    def get_seed(cls, size=32) -> bytes:
        return UrandomGenerator.generate(size=size)


class PasswordGenerator:

    @staticmethod
    def get_password(length=10):
        return StrongPasswordGenerator.generate(length)

    @classmethod
    def get_default_password(cls, secret='', length=10):
        return cls.get_smart_password(secret=secret, length=length)

    @classmethod
    def get_smart_password(cls, login='', secret='', length=10):
        seed = SmartKeyGenerator.get_private_key(login, secret)
        return SmartPasswordGenerator.generate(seed, length=length)

    @classmethod
    def get_public_key(cls, login='', secret=''):
        return SmartKeyGenerator.get_public_key(login, secret)

    @classmethod
    def check_data(cls, login, secret, public_key):
        return SmartKeyGenerator.check_data(login, secret, public_key)

"""Deliberate security-hotspot fixture (weak crypto, insecure randomness)."""

import hashlib
import random


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def generate_session_token() -> str:
    return str(random.randint(100000, 999999))

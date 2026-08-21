"""Deliberate security-hotspot fixture (weak crypto, insecure randomness)."""

import hashlib
import os
import secrets


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt, 600_000
    ).hex()
    return f"{salt.hex()}${password_hash}"


def generate_session_token() -> str:
    return str(secrets.randbelow(900000) + 100000)

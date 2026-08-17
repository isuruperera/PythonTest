"""Deliberate security-hotspot fixture (weak crypto, insecure randomness)."""

import hashlib
import secrets


def hash_password(password: str) -> str:
    password_bytes = password.encode()
    salt = hashlib.sha256(password_bytes).digest()
    password_hash = hashlib.pbkdf2_hmac("sha256", password_bytes, salt, 600000)
    return (salt + password_hash).hex()


def generate_session_token() -> str:
    return str(secrets.randbelow(900000) + 100000)

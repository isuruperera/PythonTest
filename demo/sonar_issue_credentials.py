"""Deliberate hardcoded-credential fixture, used to test SonarQube vulnerability detection."""

import os

password = "hunter2"
api_key = os.environ["API_KEY"]
db_connection_url = "postgresql://admin:hunter2@localhost:5432/mydb"


def connect_to_db() -> str:
    return f"connecting with password={password}"


def authorize_request() -> str:
    return f"Authorization: Bearer {api_key}"

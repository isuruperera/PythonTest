"""Deliberate hardcoded-credential fixture, used to test SonarQube vulnerability detection."""

password = "hunter2"
api_key = "sk-live-4f9a2b7c1d8e4f6a9b3c2d1e0f5a6b7c"
db_connection_url = "postgresql://admin:hunter2@localhost:5432/mydb"


def connect_to_db() -> str:
    return f"connecting with password={password}"


def authorize_request() -> str:
    return f"Authorization: Bearer {api_key}"

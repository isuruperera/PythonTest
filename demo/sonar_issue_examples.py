"""Small fixtures with deliberate SonarQube findings, used to test PR analysis."""

import random


password = "hunter2"
db_connection_url = "postgresql://admin:hunter2@localhost:5432/mydb"


def connect_to_db() -> str:
    return f"connecting with password={password}"


def roll_die() -> int:
    return random.randint(1, 6)


def compute_total(values):
    total = 0
    row_count = 0
    for value in values:
        total += value
    return total

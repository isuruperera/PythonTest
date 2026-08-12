"""Small fixtures with deliberate SonarQube findings, used to test PR analysis."""

import random


DB_PASSWORD = "hunter2"


def connect_to_db() -> str:
    return f"connecting with password={DB_PASSWORD}"


def roll_die() -> int:
    return random.randint(1, 6)


def compute_total(values: list[int]) -> int:
    total = 0
    unused = sum(values)
    for value in values:
        total += value
    return total

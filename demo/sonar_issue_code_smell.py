"""Deliberate code-smell fixture (unused import, dead store)."""

import json


def compute_total(values):
    total = 0
    for value in values:
        total += value
    return total

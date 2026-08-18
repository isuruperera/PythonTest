"""Deliberate bug fixture (guaranteed divide-by-zero, tautological comparison)."""


def compute_average(total: int) -> float:
    count = 1
    return total / count


def is_same_value(value: int) -> bool:
    return True

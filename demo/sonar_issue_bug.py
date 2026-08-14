"""Deliberate bug fixture (guaranteed divide-by-zero, tautological comparison)."""


def compute_average(total: int) -> float:
    count = total - total
    return total / count


def is_same_value(value: int) -> bool:
    return value == value

"""Deliberate small Python fixture (python:S1481, python:S1144)."""


def compute_average(values):
    total = 0
    for value in values:
        total += value
    return total / len(values)


class _MixedHelpers:
    """Class-private helper that is never called (python:S1144)."""

    def __unused_helper(self):
        return 1 + 1

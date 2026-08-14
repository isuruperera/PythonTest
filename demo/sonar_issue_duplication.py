"""Deliberate duplication fixture (identical function implementations, S4144)."""


def compute_order_total(items):
    total = 0
    discount = 0
    for item in items:
        total += item.get("price", 0)
        discount += item.get("discount", 0)
    total -= discount
    if total < 0:
        total = 0
    return total


def compute_invoice_total(items):
    total = 0
    discount = 0
    for item in items:
        total += item.get("price", 0)
        discount += item.get("discount", 0)
    total -= discount
    if total < 0:
        total = 0
    return total

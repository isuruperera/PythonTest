"""Deliberate duplication fixture (identical function implementations, S4144)."""


def compute_order_total(items, tax_rate=0.0, shipping_flat_fee=0.0):
    total = 0
    discount = 0
    line_count = 0
    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 1)
        line_total = price * quantity
        total += line_total
        discount += item.get("discount", 0)
        line_count += 1
    total -= discount
    if total < 0:
        total = 0
    tax = total * tax_rate
    total += tax
    if line_count > 0:
        total += shipping_flat_fee
    if total < 0:
        total = 0
    return round(total, 2)


def compute_invoice_total(items, tax_rate=0.0, shipping_flat_fee=0.0):
    total = 0
    discount = 0
    line_count = 0
    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 1)
        line_total = price * quantity
        total += line_total
        discount += item.get("discount", 0)
        line_count += 1
    total -= discount
    if total < 0:
        total = 0
    tax = total * tax_rate
    total += tax
    if line_count > 0:
        total += shipping_flat_fee
    if total < 0:
        total = 0
    return round(total, 2)

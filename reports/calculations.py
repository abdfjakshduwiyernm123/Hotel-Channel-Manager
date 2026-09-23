from decimal import Decimal


def calculate_the_report(revenue, expense):
    gop = revenue - expense
    base_fee = revenue * Decimal("0.03")
    incentive_fee = gop * Decimal("0.1")
    remaining = gop - base_fee - incentive_fee
    return (gop, base_fee, incentive_fee, remaining)

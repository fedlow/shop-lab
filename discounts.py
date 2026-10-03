def apply_discount(total, percent):
    """Скидка в процентах. 10 -> вычесть 10%."""
    if not 0 <= percent <= 100:
        raise ValueError("Скидка должна быть от 0 до 100%")
    return total * (1 - percent / 100)


def apply_tax(total, percent):
    """Налог в процентах. 20 -> добавить 20%."""
    if percent < 0:
        raise ValueError("Налог не может быть отрицательным")
    return total * (1 + percent / 100)


def final_total(total, discount=0, tax=0):
    """Итог: сначала скидка, потом налог."""
    return apply_tax(apply_discount(total, discount), tax)
class Cart:
    """Корзина покупателя."""

    def __init__(self):
        self.items = []   # список товаров

    def add(self, product):
        self.items.append(product)

    def remove(self, name):
        for p in self.items:
            if p.name == name:
                self.items.remove(p)
                return True
        return False

    def clear(self):
        self.items.clear()

    def total_cost(self):
        return sum(p.price for p in self.items)

    def total_weight(self):
        return sum(p.weight for p in self.items)

    def show(self):
        if not self.items:
            print("  Корзина пуста.")
            return
        print(f"  {'Название':<20} | {'Категория':<12} | {'Цена':>8} | {'Вес':>6}")
        print("  " + "-" * 58)
        for p in self.items:
            print("  " + p.pretty())
        print("  " + "-" * 58)
        print(f"  Итого: {self.total_cost():.2f} ₽, вес: {self.total_weight():.2f} кг")
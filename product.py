class Product:
    """Товар в магазине."""

    def __init__(self, name, category, price, weight, description=""):
        self.name = name
        self.category = category
        self.price = float(price)
        self.weight = float(weight)
        self.description = description

    def edit(self, **kwargs):
        """Редактирует поля товара. Пример: p.edit(price=99.9, weight=1.2)."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
        return (f"Product({self.name!r}, cat={self.category!r}, "
                f"price={self.price}, weight={self.weight})")

    def pretty(self):
        return (f"{self.name:<20} | {self.category:<12} | "
                f"{self.price:>8.2f} ₽ | {self.weight:>6.2f} кг")
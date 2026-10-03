from product import Product


class Catalog:
    """Каталог товаров магазина."""

    def __init__(self):
        self.products = []

    def add_product(self, name, category, price, weight, description=""):
        p = Product(name, category, price, weight, description)
        self.products.append(p)
        return p

    def remove_product(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                return True
        return False

    def find(self, name):
        for p in self.products:
            if p.name == name:
                return p
        return None

    def show(self):
        if not self.products:
            print("  Каталог пуст.")
            return
        print(f"  {'Название':<20} | {'Категория':<12} | {'Цена':>8} | {'Вес':>6}")
        print("  " + "-" * 58)
        for p in self.products:
            print("  " + p.pretty())

    @staticmethod
    def default():
        """Заполненный каталог для демонстрации."""
        c = Catalog()
        c.add_product("Молоко",     "Продукты",  89.90,  1.0, "1 литр, 3.2%")
        c.add_product("Хлеб",       "Продукты",  45.00,  0.4, "Бородинский")
        c.add_product("Сыр",        "Продукты", 320.00,  0.5, "Гауда")
        c.add_product("Футболка",   "Одежда",  1290.00,  0.2, "Хлопок, размер M")
        c.add_product("Джинсы",     "Одежда",  3490.00,  0.7, "Синие, размер 32")
        c.add_product("Кроссовки",  "Обувь",   5990.00,  0.9, "Белые, размер 42")
        c.add_product("Наушники",   "Техника", 2490.00,  0.3, "Bluetooth")
        c.add_product("Клавиатура", "Техника", 3990.00,  0.8, "Механическая")
        c.add_product("Мышь",       "Техника",  890.00,  0.1, "Беспроводная")
        c.add_product("Книга",      "Книги",    690.00,  0.4, "«Чистый код»")
        return c
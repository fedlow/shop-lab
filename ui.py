from catalog import Catalog
from cart import Cart
from sorts import SORT_ALGORITHMS, SORT_KEYS
from discounts import final_total


def show_main_menu():
    print("\n" + "=" * 60)
    print("  МАГАЗИН")
    print("=" * 60)
    print("  1. Показать каталог")
    print("  2. Добавить товар из каталога в корзину")
    print("  3. Показать корзину")
    print("  4. Удалить товар из корзины")
    print("  5. Отсортировать корзину")
    print("  6. Итоговая стоимость (со скидкой и налогом)")
    print("  7. Очистить корзину")
    print("  0. Выход")
    print("=" * 60)


def choose_sort():
    print("\n  Выберите алгоритм сортировки:")
    for k, (name, _) in SORT_ALGORITHMS.items():
        print(f"    {k}. {name}")
    algo = input("  Алгоритм: ").strip()

    print("\n  Критерий сортировки:")
    for k, (name, _) in SORT_KEYS.items():
        print(f"    {k}. {name}")
    key_choice = input("  Критерий: ").strip()

    direction = input("  По возрастанию? (y/n): ").strip().lower()
    reverse = direction == "n"

    if algo not in SORT_ALGORITHMS or key_choice not in SORT_KEYS:
        print("  Неверный выбор.")
        return

    return algo, key_choice, reverse


def run():
    catalog = Catalog.default()
    cart = Cart()

    while True:
        show_main_menu()
        choice = input("  Ваш выбор: ").strip()

        if choice == "1":
            print("\n  --- Каталог ---")
            catalog.show()

        elif choice == "2":
            name = input("  Название товара: ").strip()
            p = catalog.find(name)
            if p:
                cart.add(p)
                print(f"  «{p.name}» добавлен в корзину.")
            else:
                print("  Товар не найден.")

        elif choice == "3":
            print("\n  --- Корзина ---")
            cart.show()

        elif choice == "4":
            name = input("  Название товара: ").strip()
            if cart.remove(name):
                print(f"  «{name}» удалён из корзины.")
            else:
                print("  Такого товара в корзине нет.")

        elif choice == "5":
            result = choose_sort()
            if result is None:
                continue
            algo, key_choice, reverse = result
            name_algo, func = SORT_ALGORITHMS[algo]
            name_key, key = SORT_KEYS[key_choice]
            cart.items = func(cart.items, key=key, reverse=reverse)
            print(f"\n  Отсортировано: {name_algo}, {name_key}, "
                  f"{'по убыванию' if reverse else 'по возрастанию'}.")
            cart.show()

        elif choice == "6":
            total = cart.total_cost()
            try:
                d = float(input("  Скидка, %: ").strip() or 0)
                t = float(input("  Налог, %: ").strip() or 0)
            except ValueError:
                print("  Неверное число.")
                continue
            print(f"  Сумма без скидок: {total:.2f} ₽")
            print(f"  Со скидкой {d}% и налогом {t}%: {final_total(total, d, t):.2f} ₽")

        elif choice == "7":
            cart.clear()
            print("  Корзина очищена.")

        elif choice == "0":
            print("  До свидания!")
            break

        else:
            print("  Неизвестная команда.")
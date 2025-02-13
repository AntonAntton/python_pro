class ProductWithGetSet:
    """
    Клас, що реалізує встановлення та отримання ціни товару через методи get_price() і set_price().
    """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.set_price(price)

    def get_price(self) -> float:
        """Повертає поточну ціну товару."""
        return self._price

    def set_price(self, value: float) -> None:
        """Встановлює нову ціну товару. Якщо ціна від'ємна, викидає ValueError."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value


class ProductWithProperty:
    """
    Клас, що використовує декоратор @property для управління ціною товару.
    """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        """Повертає поточну ціну товару."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Встановлює нову ціну товару. Якщо ціна від'ємна, викидає ValueError."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value


class PriceDescriptor:
    """
    Дескриптор, що контролює встановлення та отримання значення ціни товару.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, instance, owner) -> float:
        """Повертає значення ціни з __dict__ об'єкта."""
        return instance.__dict__[self.name]

    def __set__(self, instance, value: float) -> None:
        """Встановлює значення ціни. Якщо ціна від'ємна, викидає ValueError."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        instance.__dict__[self.name] = value


class ProductWithDescriptor:
    """
    Клас, що використовує дескриптор для управління ціною товару.
    """
    price = PriceDescriptor("_price")

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


# Тестування всіх трьох підходів

def test_product_classes():
    """Функція тестує класи ProductWithGetSet, ProductWithProperty та ProductWithDescriptor."""
    print("Testing a class with setters/getters")
    product1 = ProductWithGetSet("Product 1", 100.0)
    print(product1.get_price())
    product1.set_price(150.0)
    print(product1.get_price())
    try:
        product1.set_price(-50)
    except ValueError as e:
        print(e)

    print("\nTesting a class with @property")
    product2 = ProductWithProperty("Product 2", 200.0)
    print(product2.price)
    product2.price = 250.0
    print(product2.price)
    try:
        product2.price = -30
    except ValueError as e:
        print(e)

    print("\nTesting a class with a descriptor")
    product3 = ProductWithDescriptor("Product 3", 300.0)
    print(product3.price)
    product3.price = 350.0
    print(product3.price)  # 350.0
    try:
        product3.price = -40
    except ValueError as e:
        print(e)


# Виконання тестування
if __name__ == "__main__":
    test_product_classes()

class Calculator:
    """
    Простий клас калькулятора, що підтримує додавання та віднімання.
    """

    def add(self, a: int, b: int) -> int:
        """
        Додає два числа.
        """
        return a + b

    def substract(self, a: int, b: int) -> int:
        """
        Віднімає одне число від іншого.
        """
        return a - b


def call_function(obj: object, method_name: str, *args: int) -> int:
    """
    Динамічно викликає метод об'єкта за його назвою та передає аргументи.
    """
    # Доступ до методу динамічно
    method = getattr(obj, method_name)

    # Викликаємо метод з переданими аргументами та повертаємо результат
    return method(*args)


# Приклад використання
calc = Calculator()
print(call_function(calc, "add", 10, 5))
print(call_function(calc, "substract", 10, 5))

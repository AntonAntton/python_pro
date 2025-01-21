class Calculator:
    """
    Простий клас калькулятора, що підтримує додавання та віднімання.
    """

    def add(self, a: int, b: int) -> int:
        """
        Додає два числа.

        :param a: Перше число.
        :param b: Друге число.
        :return: Результат додавання.
        """
        return a + b

    def substract(self, a: int, b: int) -> int:
        """
        Віднімає одне число від іншого.

        :param a: Перше число.
        :param b: Друге число.
        :return: Результат віднімання.
        """
        return a - b


def call_function(obj: object, method_name: str, *args: int) -> int:
    """
    Динамічно викликає метод об'єкта за його назвою та передає аргументи.

    :param obj: Об'єкт, метод якого потрібно викликати.
    :param method_name: Назва методу, який потрібно викликати.
    :param args: Аргументи, які передаються методу.
    :return: Результат виконання методу.
    """
    # Доступ до методу динамічно
    method = getattr(obj, method_name)

    # Викликаємо метод з переданими аргументами та повертаємо результат
    return method(*args)


# Приклад використання
calc = Calculator()
print(call_function(calc, "add", 10, 5))  # Виведе 15
print(call_function(calc, "substract", 10, 5))  # Виведе 5

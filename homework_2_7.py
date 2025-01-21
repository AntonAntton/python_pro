import functools


def log_methods(cls: type) -> type:
    """
    Декоратор для класу, який обгортає всі методи класу і додає логування викликів.

    :param cls: Клас, методи якого потрібно обгорнути.
    :return: Клас з логуванням для кожного методу.
    """
    for name in dir(cls):  # Отримуємо всі атрибути класу
        if not name.startswith("__"):  # Пропускаємо спеціальні методи
            attr = getattr(cls, name)  # Отримуємо атрибут
            if callable(attr):  # Перевіряємо, чи це метод
                # Створюємо обгортку з явним збереженням методу
                def wrapper(method):
                    @functools.wraps(method)
                    def inner(self, *args, **kwargs):
                        """
                        Логування виклику методу.

                        :param self: Поточний екземпляр класу.
                        :param args: Параметри для методу.
                        :param kwargs: Іменовані параметри для методу.
                        :return: Повертає результат виклику оригінального методу.
                        """
                        print(f"Logging: {method.__name__} called with {args}")
                        return method(self, *args, **kwargs)

                    return inner

                setattr(cls, name, wrapper(attr))  # Заміняємо метод на обгортку
    return cls


@log_methods
class MyClass:
    """
    Клас з методами для демонстрації логування викликів.
    """

    def add(self, a: int, b: int) -> int:
        """
        Додає два числа.

        :param a: Перше число.
        :param b: Друге число.
        :return: Сума чисел.
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        Віднімає друге число від першого.

        :param a: Перше число.
        :param b: Друге число.
        :return: Різниця між числами.
        """
        return a - b


# Тестування
obj = MyClass()
obj.add(5, 3)  # Logging: add called with (5, 3)
obj.subtract(5, 3)  # Logging: subtract called with (5, 3)

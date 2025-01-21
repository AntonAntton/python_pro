class Proxy:
    """Клас-проксі, який перехоплює виклики методів для логування їх використання."""

    def __init__(self, obj: object) -> None:
        """
        Ініціалізує об'єкт Proxy з цільовим об'єктом.

        :param obj: Цільовий об'єкт, методи якого будуть перехоплюватися.
        """
        self.obj = obj

    def __getattr__(self, name: str) -> callable:
        """
        Перехоплює доступ до атрибутів і обгортає викликаються атрибути для логування викликів методів.

        :param name: Назва атрибута (методу).
        :return: Обгорнута функція (метод) з логуванням.
        """
        # Отримуємо метод з оригінального об'єкта
        method = getattr(self.obj, name)

        # Визначаємо обгортку для методу
        def wrapper(*args, **kwargs) -> object:
            """
            Логування виклику методу.

            :param args: Параметри для методу.
            :param kwargs: Іменовані параметри для методу.
            :return: Повертає результат виклику оригінального методу.
            """
            print(f"Calling method: {name} with args: {args}")
            return method(*args, **kwargs)

        return wrapper


class MyClass:
    """
    Приклад класу з методом greet.
    """

    def greet(self, name: str) -> str:
        """
        Повертає привітальне повідомлення.

        :param name: Ім'я для привітання.
        :return: Привітальне повідомлення.
        """
        return f"Hello, {name}!"


# Приклад використання:
obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))

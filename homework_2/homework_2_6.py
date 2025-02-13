class Proxy:
    """Клас-проксі, який перехоплює виклики методів для логування їх використання."""

    def __init__(self, obj: object) -> None:
        """
        Ініціалізує об'єкт Proxy з цільовим об'єктом.
        """
        self.obj = obj

    def __getattr__(self, name: str) -> callable:
        """
        Перехоплює доступ до атрибутів і обгортає викликаються атрибути для логування викликів методів.
        """
        # Отримуємо метод з оригінального об'єкта
        method = getattr(self.obj, name)

        # Визначаємо обгортку для методу
        def wrapper(*args, **kwargs) -> object:
            """
            Логування виклику методу.
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

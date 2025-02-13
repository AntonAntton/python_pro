class SingletonMeta(type):
    """
    Мета-клас для реалізації патерну Singleton.
    Забезпечує створення лише одного екземпляра класу.
    """
    instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        """
        Перевизначає виклик класу для створення лише одного екземпляра.
        """
        if cls not in cls.instances:
            # Створюємо новий екземпляр, якщо він ще не існує
            instance = super().__call__(*args, **kwargs)
            cls.instances[cls] = instance
        return cls.instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    Клас, який реалізує патерн Singleton.
    Використовує SingletonMeta як мета-клас для забезпечення одного екземпляра.
    """
    def __init__(self) -> None:
        """
        Ініціалізує клас Singleton та виводить повідомлення про створення екземпляра.
        """
        print("Creating instance")


# Приклад використання
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)

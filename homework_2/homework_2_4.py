from typing import Dict, Callable, Type

def create_class(class_name: str, methods: Dict[str, Callable]) -> Type:
    """
    Динамічно створює новий клас з заданою назвою та методами.

    :param class_name: Назва нового класу.
    :param methods: Словник методів, де ключ — це назва методу, а значення — функція.
    :return: Тип (клас) з динамічно доданими методами.
    """
    # Створюємо новий клас динамічно за допомогою type
    return type(class_name, (object,), methods)

def say_hello(self) -> str:
    """
    Повертає привітальне повідомлення.

    :return: Привітальне повідомлення.
    """
    return "Hello!"

def say_goodbye(self) -> str:
    """
    Повертає прощальне повідомлення.

    :return: Прощальне повідомлення.
    """
    return "Goodbye!"

# Словник методів
methods: Dict[str, Callable] = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

# Створюємо динамічний клас
MyDynamicClass = create_class("MyDynamicClass", methods)

# Приклад використання
obj = MyDynamicClass()
print(obj.say_hello())  # Hello!
print(obj.say_goodbye())  # Goodbye!
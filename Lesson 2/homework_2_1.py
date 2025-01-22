def analyze_object(obj: object) -> None:
    """
    Аналізує об'єкт, виводячи його тип і перераховуючи його атрибути та методи з їх типами.
    """
    # Виводимо тип об'єкта
    print(f"Type of object: {type(obj)}")

    # Отримуємо всі атрибути та методи об'єкта
    attributes_methods = dir(obj)

    # Виводимо атрибути та їх типи
    print("\nAttributes and methods:")
    for item in attributes_methods:
        value = getattr(obj, item, None)  # Отримуємо значення атрибута чи методу
        print(f"{item}: {type(value)}")  # Виводимо назву та тип атрибута чи методу


class MyClass:
    """
    Простий клас, який демонструє використання атрибутів та методів.
    """

    def __init__(self, value: str) -> None:
        """
        Ініціалізує екземпляр MyClass з заданим значенням.(
        """
        self.value = value

    def say_hello(self) -> str:
        """
        Повертає привітальне повідомлення, яке включає атрибут value.
        """
        return f"Hello, {self.value}"


# Приклад використання
obj = MyClass("World")
analyze_object(obj)

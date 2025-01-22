class MutableClass:
    """
    Клас, який дозволяє динамічно додавати та видаляти атрибути.
    """
    
    def __init__(self) -> None:
        """
        Ініціалізує екземпляр класу MutableClass.
        """
        pass

    def add_attribute(self, name: str, value: object) -> None:
        """
        Динамічно додає атрибут до екземпляра класу.
        """
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        """
        Динамічно видаляє атрибут з екземпляра класу.
        """
        delattr(self, name)


# Приклад використання:
obj = MutableClass()

# Додаємо атрибут динамічно
obj.add_attribute("name", "Python")
print(obj.name)

# Видаляємо атрибут динамічно
obj.remove_attribute("name")

class DynamicProperties:
    def __init__(self) -> None:
        """
        Ініціалізує клас DynamicProperties, який містить словник для збереження властивостей.
        """
        self.properties = {}

    def add_property(self, name: str, default_value: str) -> None:
        """
        Додає динамічну властивість до об'єкта. Визначає геттери та сеттери для властивості.
        """
        # Визначення геттера
        def getter(self) -> str:
            """
            Геттер для властивості.
            """
            return self.properties.get(name, default_value)

        # Визначення сеттера
        def setter(self, value: str) -> None:
            """
            Сеттер для властивості.
            """
            self.properties[name] = value

        # Створення властивості та динамічне додавання до класу
        setattr(self.__class__, name, property(getter, setter))


# Приклад використання
obj = DynamicProperties()
obj.add_property('name', 'default_name')

print(obj.name)
obj.name = "Python"
print(obj.name)

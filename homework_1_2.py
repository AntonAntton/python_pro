from typing import Union

class Rectangle:
    def __init__(self, width: Union[float, int], height: Union[float, int]):
        """Ініціалізая трикутника за заданними шириною і висотою"""
        self.width = width
        self.height = height

    def area(self) -> Union[float, int]:
        """Повертає площу трикутника"""
        return round(self.width * self.height, 2)

    def perimeter(self) -> Union[float, int]:
        """Поветрає периметр трикутника"""
        return round(2 * (self.width + self.height), 2)

    def is_square(self) -> bool:
        """Поветрає True якщо трикутник є квадрат, інакше False"""
        return self.width == self.height

    def resize(self, new_width: Union[float, int], new_height: Union[float, int]):
        """Міняє розмір трикутника за заданними новими шириною і висотою"""
        self.width = new_width
        self.height = new_height

# Перевірка классу Rectangle
rect = Rectangle(3, 9)

# Перевірка методу area
print("Area:", rect.area())

#Перевірка методу perimeter
print("Perimeter:", rect.perimeter())

# Перевірка методу is_square
print("Is square:", rect.is_square())

# Міняємо розмір трикутника
rect.resize(5.55, 5.55)

# Перевіряємо методи після зміни розмірів
print("New area:", rect.area())
print("New perimeter:", rect.perimeter())
print("Is square after resizing:", rect.is_square())

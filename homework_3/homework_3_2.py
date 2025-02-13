import math


class Vector:
    """
    Клас, що представляє двовимірний вектор та підтримує основні операції над ним.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Ініціалізація вектора з заданими координатами x та y.
        """
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        """
        Додавання двох векторів.
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        """
        Віднімання одного вектора від іншого.
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        """
        Множення вектора на число.
        """
        return Vector(self.x * scalar, self.y * scalar)

    def __lt__(self, other: "Vector") -> bool:
        """
        Порівняння векторів за довжиною (менше).
        """
        return self.length() < other.length()

    def __eq__(self, other: "Vector") -> bool:
        """
        Перевірка рівності довжин двох векторів.
        """
        return self.length() == other.length()

    def length(self) -> float:
        """
        Обчислення довжини вектора.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self) -> str:
        """
        Повертає строкове представлення вектора.
        """
        return f"Vector({self.x}, {self.y})"


# Приклад використання
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1.length())
print(v1 < v2)
print(v1 == v2)

import math


class Vector:
    """
    Клас, що представляє n-вимірний вектор.
    Підтримує основні операції: додавання, віднімання, множення та порівняння за довжиною.
    """

    def __init__(self, *components: float) -> None:
        """Ініціалізація вектора з переданими компонентами."""
        self.components: tuple = tuple(components)

    def __add__(self, other: "Vector") -> "Vector":
        """Додавання двох векторів."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other: "Vector") -> "Vector":
        """Віднімання двох векторів."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other: float) -> float:
        """Множення вектора на число або обчислення скалярного добутку двох векторів."""
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must be of the same dimension")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Multiplication with this type is not supported")

    def magnitude(self) -> float:
        """Обчислення довжини (модуля) вектора."""
        return math.sqrt(sum(a ** 2 for a in self.components))

    def __eq__(self, other: "Vector") -> bool:
        """Перевірка рівності двох векторів за їх довжиною."""
        return self.magnitude() == other.magnitude()

    def __lt__(self, other: "Vector") -> bool:
        """Перевірка, чи даний вектор коротший за інший."""
        return self.magnitude() < other.magnitude()

    def __le__(self, other: "Vector") -> bool:
        """Перевірка, чи даний вектор не довший за інший."""
        return self.magnitude() <= other.magnitude()

    def __gt__(self, other: "Vector") -> bool:
        """Перевірка, чи даний вектор довший за інший."""
        return self.magnitude() > other.magnitude()

    def __ge__(self, other: "Vector") -> bool:
        """Перевірка, чи даний вектор не коротший за інший."""
        return self.magnitude() >= other.magnitude()

    def __repr__(self) -> str:
        """Повертає рядкове представлення вектора."""
        return f"Vector{self.components}"


# Тести функцій
if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2:", v1 + v2)
    print("v1 - v2:", v1 - v2)
    print("v1 * 3:", v1 * 3)
    print("v1 * v2 (dot product):", v1 * v2)
    print("Magnitude of v1:", v1.magnitude())
    print("Is v1 equal to v2?", v1 == v2)
    print("Is v1 less than v2?", v1 < v2)
    print("Is v1 greater than or equal to v2?", v1 >= v2)

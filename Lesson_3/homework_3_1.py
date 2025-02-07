from math import gcd


class Fraction:
    """
    Клас для роботи з дробами.
    Містить методи для додавання, віднімання, множення та ділення дробів.
    Також підтримує спрощення дробів та коректне виведення.
    """

    def __init__(self, numerator: int, denominator: int):
        """
        Ініціалізація дробу.
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        # Спрощення дробу за допомогою найбільшого спільного дільника
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __add__(self, other: "Fraction") -> "Fraction":
        """
        Додавання двох дробів.
        """
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other: "Fraction") -> "Fraction":
        """
        Віднімання двох дробів.
        """
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __mul__(self, other: "Fraction") -> "Fraction":
        """
        Множення двох дробів.
        """
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        return NotImplemented

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """
        Ділення двох дробів.
        """
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero fraction")
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        return NotImplemented

    def __repr__(self) -> str:
        """
        Коректне представлення дробу у форматі "чисельник/знаменник".
        """
        return f"{self.numerator}/{self.denominator}"


# Приклад використання:
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

print(frac1 + frac2)
print(frac1 - frac2)
print(frac1 * frac2)
print(frac1 / frac2)

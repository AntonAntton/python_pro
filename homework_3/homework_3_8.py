from decimal import Decimal, ROUND_HALF_UP


class Price:
    """
    Клас Price представляє ціну товару з можливістю заокруглення до двох десяткових знаків.
    Містить методи для арифметичних операцій та порівняння цін.
    """

    def __init__(self, amount: float) -> None:
        """
        Ініціалізує об'єкт класу Price із округленим значенням ціни.
        """
        self.amount: Decimal = Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def __add__(self, other: "Price") -> "Price":
        """
        Додає дві ціни.
        """
        if isinstance(other, Price):
            return Price(self.amount + other.amount)
        raise TypeError(f"Unsupported operand type for +: 'Price' і '{type(other).__name__}'")

    def __sub__(self, other: "Price") -> "Price":
        """
        Віднімає одну ціну від іншої.
        """
        if isinstance(other, Price):
            return Price(self.amount - other.amount)
        raise TypeError(f"Unsupported operand type for -: 'Price' і '{type(other).__name__}'")

    def __eq__(self, other: object) -> bool:
        """
        Перевіряє рівність двох цін.
        """
        return isinstance(other, Price) and self.amount == other.amount

    def __lt__(self, other: "Price") -> bool:
        """
        Перевіряє, чи поточна ціна менша за іншу.
        """
        return isinstance(other, Price) and self.amount < other.amount

    def __le__(self, other: "Price") -> bool:
        """
        Перевіряє, чи поточна ціна менша або рівна іншій.
        """
        return isinstance(other, Price) and self.amount <= other.amount

    def __str__(self) -> str:
        """
        Повертає рядкове представлення ціни у форматі з двома десятковими знаками.
        """
        return f"${self.amount:.2f}"

    @classmethod
    def from_string(cls, price_str: str) -> "Price":
        """
        Створює об'єкт Price із рядкового представлення числа.
        """
        if not isinstance(price_str, str):
            raise ValueError(f"Expected a string, received {type(price_str).__name__}")
        try:
            return cls(Decimal(price_str))
        except Exception as e:
            raise ValueError(f"Incorrect price format: {price_str}") from e

# Приклад використання
price1 = Price(10.255)
price2 = Price(5.499)
price3 = Price.from_string("3.75")

print("Price 1:", price1)
print("Price 2:", price2)
print("Price 3:", price3)

# Арифметичні операції
total_price = price1 + price2
print("Total price:", total_price)

difference = price1 - price3
print("Difference:", difference)

# Порівняння
print("Is price1 greater than price2??", price1 > price2)
print("Is price3 equal to $3.75??", price3 == Price(3.75))

# Тестування обробки помилок
try:
    invalid_price = Price.from_string(100)
except ValueError as e:
    print("Error:", e)

try:
    invalid_price2 = Price.from_string("abc")
except ValueError as e:
    print("Error:", e)

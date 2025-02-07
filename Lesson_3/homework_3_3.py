class Person:
    """
    Клас, що представляє людину з ім'ям та віком.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Ініціалізує об'єкт класу Person.
        """
        self.name = name
        self.age = age

    def __lt__(self, other: "Person") -> bool:
        """
        Порівнює вік поточного об'єкта з іншим об'єктом.
        """
        return self.age < other.age

    def __eq__(self, other: "Person") -> bool:
        """
        Перевіряє рівність віку двох об'єктів.
        """
        return self.age == other.age

    def __gt__(self, other: "Person") -> bool:
        """
        Порівнює вік поточного об'єкта з іншим об'єктом.
        """
        return self.age > other.age

    def __repr__(self) -> str:
        """
        Повертає рядкове представлення об'єкта.
        """
        return f"{self.name} ({self.age} years)"


# Створення списку об'єктів Person
people = [
    Person("Alice", 25),
    Person("Bob", 30),
    Person("Charlie", 22),
    Person("David", 35),
    Person("Eve", 28)
]

# Сортування списку за віком
sorted_people = sorted(people)

# Виведення результату
print("Sorted by age:")
for person in sorted_people:
    print(person)

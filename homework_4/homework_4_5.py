from typing import Generator


class EvenNumberGenerator:
    """Генератор для створення нескінченної послідовності парних чисел."""

    def __init__(self):
        self.current = 0

    def __iter__(self) -> Generator[int, None, None]:
        """Метод для ітерації по нескінченній послідовності парних чисел."""
        while True:
            yield self.current
            self.current += 2

    def save_to_file(self, count: int, filename: str) -> None:
        """Зберігає перші 'count' парних чисел у файл."""
        with open(filename, 'w') as file:
            even_gen = iter(self)  # Створюємо генератор
            for _ in range(count):
                file.write(f"{next(even_gen)}\n")

    def __enter__(self):
        """Метод для менеджера контексту (початок використання)."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Метод для менеджера контексту (завершення використання)."""
        pass

    @staticmethod
    def generate_and_save(limit: int, filename: str) -> None:
        """Функція для генерації та збереження чисел у файл через менеджер контексту."""
        with EvenNumberGenerator() as gen:
            gen.save_to_file(limit, filename)


# Використання менеджера контексту для обмеження кількості чисел
if __name__ == "__main__":
    try:
        # Генерація та збереження парних чисел до 100 у файл
        EvenNumberGenerator.generate_and_save(100, 'even_numbers.txt')
        print("Парні числа збережено у файл 'even_numbers.txt'")
    except Exception as e:
        print(f"Сталася помилка: {e}")

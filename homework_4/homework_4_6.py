import os
from typing import Iterator, Tuple


class DirectoryFileIterator:
    """Ітератор для перебору всіх файлів у заданому каталозі."""

    def __init__(self, directory: str):
        """Ініціалізація ітератора з вказаним каталогом.

        :param directory: шлях до каталогу, в якому потрібно перебирати файли.
        """
        self.directory = directory
        self.files = os.listdir(directory)  # Отримуємо список усіх файлів і папок
        self.index = 0  # Індекс для ітерації

    def __iter__(self) -> Iterator[Tuple[str, int]]:
        """Метод ітерації через файли в каталозі.

        :return: кортеж, що містить ім'я файлу та його розмір.
        """
        return self

    def __next__(self) -> Tuple[str, int]:
        """Повертає наступний файл з його ім'ям та розміром.

        :return: кортеж (ім'я файлу, розмір файлу в байтах).
        :raises StopIteration: коли файли закінчуються.
        """
        while self.index < len(self.files):
            file_name = self.files[self.index]
            file_path = os.path.join(self.directory, file_name)

            # Перевіряємо, чи є це файл (ігноруємо папки)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)  # Отримуємо розмір файлу
                self.index += 1
                return (file_name, file_size)
            self.index += 1  # Якщо це не файл, йдемо до наступного елемента

        raise StopIteration


# Використання ітератора для виведення всіх файлів у каталозі
if __name__ == "__main__":
    directory_path = '/Users/anton01.16.23/Desktop/03.02.25'  # Замініть на шлях до вашого каталогу
    try:
        file_iterator = DirectoryFileIterator(directory_path)

        # Ітеруємо через всі файли в каталозі
        for file_name, file_size in file_iterator:
            print(f"Файл: {file_name}, Розмір: {file_size} байт")
    except Exception as e:
        print(f"Сталася помилка: {e}")

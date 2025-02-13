from typing import Iterator


class ReverseFileIterator:
    """
    Ітератор для зчитування файлу у зворотному порядку рядок за рядком.
    """

    def __init__(self, filename: str, encoding: str = "utf-8") -> None:
        """
        Ініціалізація ітератора.
        """
        self.filename = filename
        self.encoding = encoding

    def __iter__(self) -> Iterator[str]:
        """
        Метод для отримання ітератора.
        """
        with open(self.filename, 'rb') as file:
            file.seek(0, 2)  # Переміщуємося в кінець файлу
            position = file.tell()
            buffer = bytearray()

            while position > 0:
                file.seek(position - 1)
                char = file.read(1)

                if char == b'\n':
                    if buffer:
                        yield buffer[::-1].decode(self.encoding, errors='ignore')
                        buffer = bytearray()
                else:
                    buffer += char

                position -= 1

            if buffer:
                yield buffer[::-1].decode(self.encoding, errors='ignore')


# Створення тестового файлу
filename = "example.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write("Перший рядок\n")
    file.write("Другий рядок\n")
    file.write("Третій рядок\n")

# Приклад використання:
if __name__ == "__main__":
    for line in ReverseFileIterator(filename, encoding="utf-8"):
        print(line)

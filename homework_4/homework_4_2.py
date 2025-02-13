import uuid
from typing import Iterator


class UniqueIDIterator:
    """
    Ітератор для генерації унікальних ідентифікаторів на основі UUID4.
    """

    def __init__(self, count: int) -> None:
        """
        Ініціалізація ітератора.
        """
        self.count = count
        self.generated = 0

    def __iter__(self) -> Iterator[str]:
        """
        Метод для отримання ітератора.
        """
        while self.generated < self.count:
            self.generated += 1
            yield str(uuid.uuid4())


# Приклад використання:
if __name__ == "__main__":
    id_iterator = UniqueIDIterator(5)
    for unique_id in id_iterator:
        print(unique_id)

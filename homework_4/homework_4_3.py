import os
import csv
from typing import Iterator, Tuple
from PIL import Image


class ImageMetadataIterator:
    """
    Ітератор для зчитування метаданих зображень у вказаному каталозі.
    """

    def __init__(self, directory: str, output_csv: str) -> None:
        """
        Ініціалізація ітератора.
        """
        self.directory = directory
        self.output_csv = output_csv
        self.files = [f for f in os.listdir(directory) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
        self.index = 0

    def __iter__(self) -> Iterator[Tuple[str, Tuple[int, int], str]]:
        """
        Метод для отримання ітератора.
        """
        with open(self.output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Файл", "Розмір", "Формат"])

            while self.index < len(self.files):
                file_name = self.files[self.index]
                file_path = os.path.join(self.directory, file_name)

                try:
                    with Image.open(file_path) as img:
                        metadata = (file_name, img.size, img.format)
                        writer.writerow(metadata)
                        yield metadata
                except Exception as e:
                    print(f"Помилка з файлом {file_name}: {e}")

                self.index += 1


# Приклад використання:
if __name__ == "__main__":
    directory = "/Users/anton01.16.23/Desktop/photo"  # Змініть на вашу папку з зображеннями
    output_csv = "image_metadata.csv"

    for metadata in ImageMetadataIterator(directory, output_csv):
        print(metadata)

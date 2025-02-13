import zipfile
import os
from typing import List


class ZipArchiver:
    """
    Менеджер контексту для архівування файлів та директорій за допомогою модуля zipfile.
    При створенні архіву менеджер автоматично додає файли та директорії, а після завершення блоку with –
    завершує архівування та закриває архів.
    """

    def __init__(self, archive_name: str):
        """
        Ініціалізує менеджер контексту з вказаним ім'ям архіву.
        """
        self.archive_name = archive_name
        self.archive = None

    def __enter__(self) -> "ZipArchiver":
        """
        Відкриває архів на запис та повертає сам менеджер.
        """
        self.archive = zipfile.ZipFile(self.archive_name, 'w', zipfile.ZIP_DEFLATED)
        return self

    def add_files(self, files: List[str]) -> None:
        """
        Додає файли до архіву. Якщо передано директорію, то архівуються всі файли всередині.
        """
        for file in files:
            if os.path.isdir(file):
                # Якщо це директорія, додаємо всі файли в ній
                for root, dirs, files_in_dir in os.walk(file):
                    for file_in_dir in files_in_dir:
                        self.archive.write(os.path.join(root, file_in_dir),
                                           os.path.relpath(os.path.join(root, file_in_dir), start=file))
            else:
                self.archive.write(file)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Закриває архів після завершення блоку with.
        """
        if self.archive:
            self.archive.close()


# Приклад використання менеджера контексту:
if __name__ == "__main__":
    # Вказуємо директорії для архівування та для збереження архіву
    directory_to_archive = "/Users/anton01.16.23/Desktop/untitled folder"
    save_directory = "/Users/anton01.16.23/Desktop"

    # Перевіряємо, чи існує директорія для архівування
    if os.path.isdir(directory_to_archive):
        # Перевіряємо, чи існує директорія для збереження архіву, якщо ні, створюємо її
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # Формуємо ім'я архіву та шлях до нього
        archive_name = f"{os.path.basename(directory_to_archive)}.zip"
        archive_path = os.path.join(save_directory, archive_name)

        # Архівуємо директорію
        with ZipArchiver(archive_path) as archiver:
            archiver.add_files([directory_to_archive])

        print(f"Directory '{directory_to_archive}' has been successfully archived to '{archive_path}'.")
    else:
        print("The specified directory for archiving does not exist.")

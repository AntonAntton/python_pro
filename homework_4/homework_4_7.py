import re
from typing import Generator
import os


class LogFileParser:
    """Парсер для аналізу лог-файлів веб-сервера та фільтрації рядків з помилками."""

    def __init__(self, log_file: str):
        """Ініціалізація парсера для вказаного лог-файлу."""
        self.log_file = log_file

    def _parse_line(self, line: str) -> bool:
        """Перевіряє, чи містить рядок помилку (статус 4XX або 5XX)."""
        # Використовуємо регулярний вираз для пошуку коду статусу (4XX або 5XX)
        match = re.search(r'\s(\d{3})\s', line)
        if match:
            status_code = int(match.group(1))
            return status_code >= 400 and status_code < 600
        return False

    def read_errors(self) -> Generator[str, None, None]:
        """Генерує рядки з помилками з лог-файлу."""
        with open(self.log_file, 'r') as file:
            for line in file:
                if self._parse_line(line):
                    yield line

    def save_errors(self, output_file: str) -> None:
        """Зберігає всі рядки з помилками в окремий файл."""
        with open(output_file, 'w') as file:
            for error_line in self.read_errors():
                file.write(error_line)

    @staticmethod
    def create_sample_log_file(file_path: str) -> None:
        """Створює тестовий лог-файл з різними HTTP статусами."""
        log_entries = [
            '127.0.0.1 - - [12/Feb/2025:10:24:36 +0000] "GET /index.html HTTP/1.1" 200 2326',
            '127.0.0.1 - - [12/Feb/2025:10:25:00 +0000] "GET /about.html HTTP/1.1" 404 2326',
            '127.0.0.1 - - [12/Feb/2025:10:25:30 +0000] "GET /contact.html HTTP/1.1" 500 2326',
            '127.0.0.1 - - [12/Feb/2025:10:26:00 +0000] "GET /index.html HTTP/1.1" 200 2326',
            '127.0.0.1 - - [12/Feb/2025:10:26:30 +0000] "GET /page-not-found HTTP/1.1" 404 2326',
            '127.0.0.1 - - [12/Feb/2025:10:27:00 +0000] "POST /login HTTP/1.1" 403 1324',
            '127.0.0.1 - - [12/Feb/2025:10:27:30 +0000] "GET /admin HTTP/1.1" 502 5231',
            '127.0.0.1 - - [12/Feb/2025:10:28:00 +0000] "GET /index.html HTTP/1.1" 200 1234'
        ]

        with open(file_path, 'w') as file:
            for entry in log_entries:
                file.write(entry + "\n")

    @staticmethod
    def save_log_file(file_path: str) -> None:
        """Зберігає лог-файл окремо."""
        if os.path.exists(file_path):
            print(f"Лог-файл збережено за адресою: {file_path}")
        else:
            print(f"Не вдалося зберегти лог-файл: {file_path}")


# Використання парсера для зчитування та збереження помилок
if __name__ == "__main__":
    log_file_path = './server_log.txt'  # Шлях до тестового лог-файлу
    output_file_path = './errors.txt'  # Файл для збереження помилок

    try:
        # Створити тестовий лог-файл
        LogFileParser.create_sample_log_file(log_file_path)

        # Зберегти лог-файл окремо
        LogFileParser.save_log_file(log_file_path)

        # ініціалізуємо парсер
        parser = LogFileParser(log_file_path)

        # Збереження помилок в окремий файл
        parser.save_errors(output_file_path)
        print(f"Помилки збережено у файл '{output_file_path}'")
    except Exception as e:
        print(f"Сталася помилка: {e}")

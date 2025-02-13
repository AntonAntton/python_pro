from typing import Iterator


def filter_lines(file_path: str, keyword: str) -> Iterator[str]:
    """
    Генератор для зчитування великого файлу та фільтрації рядків за ключовим словом.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if keyword in line:
                    yield line.strip()
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")


def save_filtered_lines(input_file: str, output_file: str, keyword: str) -> None:
    """
    Зберігає відфільтровані рядки у новий файл.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for line in filter_lines(input_file, keyword):
                file.write(line + '\n')
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")


# Приклад використання
if __name__ == "__main__":
    input_file = "large_text_file.txt"  # Задайте шлях до великого файлу
    output_file = "filtered_text_file.txt"  # Файл для збереження відфільтрованих рядків
    keyword = "ERROR"  # Ключове слово для пошуку

    save_filtered_lines(input_file, output_file, keyword)
    print(f"Фільтрація завершена. Результати збережено у {output_file}")
    
import json
import os
from typing import Union


class ConfigManager:
    """
    Контекстний менеджер для роботи з конфігураційними файлами у форматі .json.
    """

    def __init__(self, file_path: str):
        """
        Ініціалізація менеджера з файлом конфігурації.
        """
        self.file_path = file_path
        self.config_data: Union[dict, None] = None
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """
        Перевіряє існування файлу конфігурації та створює його, якщо він відсутній.
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump({}, file, indent=4, ensure_ascii=False)

    def __enter__(self):
        """
        Зчитує конфігурацію з файлу при вході в контекст.
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            self.config_data = json.load(file)

        return self.config_data

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Записує конфігурацію у файл після виходу з контексту.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.config_data, file, indent=4, ensure_ascii=False)

        self.config_data = None
        

# Робота з JSON
with ConfigManager("/Users/anton01.16.23/Desktop/sample1.json") as config:
    print("Data before modification:", config)
    if "settings" not in config:
        config["settings"] = {}
    config["settings"]["theme"] = "Dark"
    print("Data after modification:", config)

import inspect
import importlib
from typing import List, Optional


def analyze_module(module_name: str) -> None:
    """
    Аналізує заданий модуль, виводячи його функції та класи.
    """
    try:
        # Завантажуємо модуль за допомогою importlib
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Модуль '{module_name}' не знайдений.")
        return

    # Отримуємо функції (включаючи викликаються об'єкти) з модуля
    functions: List[object] = [obj for name, obj in inspect.getmembers(module) if
                               inspect.isfunction(obj) or callable(obj)]
    # Отримуємо класи з модуля
    classes: List[type] = [obj for name, obj in inspect.getmembers(module, inspect.isclass)]

    print("Функції:")
    if functions:
        for func in functions:
            try:
                # Виводимо підпис кожної функції
                signature = inspect.signature(func)
                print(f"- {func.__name__}{signature}")
            except (ValueError, TypeError):
                print(f"- {func.__name__} (підпис недоступний)")
    else:
        print("- Функції не знайдені в модулі.")

    print("\nКласи:")
    if classes:
        for cls in classes:
            print(f"- {cls.__name__}")
    else:
        print("- Класи не знайдені в модулі.")


# Приклад використання
if __name__ == "__main__":
    module_name = input("Введіть назву модуля: ")
    analyze_module(module_name)

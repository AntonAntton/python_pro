from typing import Type


def analyze_inheritance(cls: Type) -> None:
    """
    Аналізує ієрархію наслідування наданого класу та виводить методи, які 
    успадковані, але не переозначені в класі.
    """
    print(f'Class {cls.__name__} inherent:')

    base_methods = {}
    for base in cls.__bases__:
        for attr in dir(base):
            if callable(getattr(base, attr)) and not attr.startswith("__"):
                base_methods[attr] = base.__name__

    inherited_methods = []
    for method, base_name in base_methods.items():
        # Перевірка, чи метод не переозначений в поточному класі
        if method not in cls.__dict__:
            inherited_methods.append(method, base_name)

    if inherited_methods:
        for method, base_name in inherited_methods:
            print(f'- {method} with {base_name}')
    else:
        print('Class does not inherent any methods.')
         


# Приклад використання
class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


analyze_inheritance(Child)

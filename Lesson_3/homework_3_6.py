import re


class User:
    """
    Клас, що представляє користувача з атрибутами:
    - first_name (ім'я)
    - last_name (прізвище)
    - email (електронна пошта)
    Доступ до атрибутів здійснюється через декоратор @property.
    """

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        """
        Конструктор класу User.
        Перевіряє коректність введених даних.
        """
        self.first_name = first_name
        self.last_name = last_name
        self._email = None
        self.email = email

    @property
    def first_name(self) -> str:
        """Повертає ім'я користувача."""
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """Встановлює ім'я користувача, перевіряючи його на порожнє значення."""
        if not value.strip():
            raise ValueError("First name cannot be empty.")
        self._first_name = value.strip()

    @property
    def last_name(self) -> str:
        """Повертає прізвище користувача."""
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """Встановлює прізвище користувача, перевіряючи його на порожнє значення."""
        if not value.strip():
            raise ValueError("Last name cannot be empty.")
        self._last_name = value.strip()

    @property
    def email(self) -> str:
        """Повертає email користувача."""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """
        Встановлює email користувача, перевіряючи його правильність.
        Використовує регулярний вираз для перевірки формату email.
        """
        if not self._is_valid_email(value):
            raise ValueError("Invalid email format.")
        self._email = value.lower()

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """
        Перевіряє, чи відповідає email правильному формату.
        Використовує регулярний вираз.
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def __str__(self) -> str:
        """Повертає рядкове представлення користувача."""
        return f"{self.first_name} {self.last_name} <{self.email}>"


# Приклад використання
try:
    user = User("John", "Doe", "john.doe@example.com")
    print(user)

    user.email = "new.email@domain.com"
    print(user.email)

    user.email = "invalid-email"

except ValueError as e:
    print(e)

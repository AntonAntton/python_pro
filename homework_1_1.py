import math

def calculate_circle_area(radius: float) -> float:
    """Розраховує і повертає площу кола за заданним радіусом"""
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    return math.pi * radius ** 2

# Запрос радіуса від користувача
try:
    radius = float(input("Enter your radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is {area:.2f}")
except ValueError as e:
    print(f"Invalid input: {e}")

from typing import Iterable, Any
import unittest


class MyLen:
    """
    Клас для реалізації власної версії функції len().
    """

    @staticmethod
    def len(obj: Any) -> int:
        """
        Повертає кількість елементів у послідовності або ітераторі.
        """
        if hasattr(obj, '__len__'):
            return obj.__len__()

        count = 0
        try:
            iterator = iter(obj)
            while True:
                next(iterator)
                count += 1
        except StopIteration:
            return count


class MySum:
    """
    Клас для реалізації власної версії функції sum().
    """

    @staticmethod
    def sum(iterable: Iterable[int], start: int = 0) -> int:
        """
        Повертає суму елементів у послідовності, починаючи зі start.
        """
        total = start
        for item in iterable:
            total += item
        return total


class MyMin:
    """
    Клас для реалізації власної версії функції min().
    """

    @staticmethod
    def min(iterable: Iterable[int]) -> int:
        """
        Повертає мінімальний елемент у послідовності.
        """
        iterator = iter(iterable)
        try:
            min_value = next(iterator)
            for item in iterator:
                if item < min_value:
                    min_value = item
            return min_value
        except StopIteration:
            raise ValueError("min() arg is an empty sequence")


# Тестування
class TestMyFunctions(unittest.TestCase):
    def test_len(self):
        self.assertEqual(MyLen.len([1, 2, 3]), 3)
        self.assertEqual(MyLen.len("hello"), 5)
        self.assertEqual(MyLen.len({1, 2, 3, 4}), 4)
        self.assertEqual(MyLen.len([]), 0)

    def test_sum(self):
        self.assertEqual(MySum.sum([1, 2, 3]), 6)
        self.assertEqual(MySum.sum([1, 2, 3], 10), 16)
        self.assertEqual(MySum.sum([]), 0)
        self.assertEqual(MySum.sum([10]), 10)

    def test_min(self):
        self.assertEqual(MyMin.min([3, 1, 2]), 1)
        self.assertEqual(MyMin.min([10, 5, 7]), 5)
        self.assertEqual(MyMin.min([-1, -5, 0]), -5)
        with self.assertRaises(ValueError):
            MyMin.min([])


if __name__ == "__main__":
    unittest.main()


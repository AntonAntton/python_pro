import unittest


class BinaryNumber:
    """
    Клас, що представляє двійкове число та підтримує двійкові операції AND, OR, XOR і NOT.
    """

    def __init__(self, value: str):
        """
        Ініціалізація двійкового числа.
        """
        if not all(c in '01' for c in value):
            raise ValueError("BinaryNumber must contain only '0' and '1'")
        self.value = value

    def __str__(self) -> str:
        """
        Повертає рядкове представлення двійкового числа.
        """
        return self.value

    def __and__(self, other: 'BinaryNumber') -> 'BinaryNumber':
        """
        Виконує побітову операцію AND між двома двійковими числами.
        """
        max_len = max(len(self.value), len(other.value))
        a = self.value.zfill(max_len)
        b = other.value.zfill(max_len)
        result = ''.join(str(int(x) & int(y)) for x, y in zip(a, b))
        return BinaryNumber(result)

    def __or__(self, other: 'BinaryNumber') -> 'BinaryNumber':
        """
        Виконує побітову операцію OR між двома двійковими числами.
        """
        max_len = max(len(self.value), len(other.value))
        a = self.value.zfill(max_len)
        b = other.value.zfill(max_len)
        result = ''.join(str(int(x) | int(y)) for x, y in zip(a, b))
        return BinaryNumber(result)

    def __xor__(self, other: 'BinaryNumber') -> 'BinaryNumber':
        """
        Виконує побітову операцію XOR між двома двійковими числами.
        """
        max_len = max(len(self.value), len(other.value))
        a = self.value.zfill(max_len)
        b = other.value.zfill(max_len)
        result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
        return BinaryNumber(result)

    def __invert__(self) -> 'BinaryNumber':
        """
        Виконує побітову операцію NOT (інверсію бітів).
        """
        result = ''.join('1' if x == '0' else '0' for x in self.value)
        return BinaryNumber(result)


# Тестування функціоналу
class TestBinaryNumberOperations(unittest.TestCase):

    def test_and(self):
        a = BinaryNumber("1101")
        b = BinaryNumber("1011")
        self.assertEqual(str(a & b), "1001")

    def test_or(self):
        a = BinaryNumber("1101")
        b = BinaryNumber("1011")
        self.assertEqual(str(a | b), "1111")

    def test_xor(self):
        a = BinaryNumber("1101")
        b = BinaryNumber("1011")
        self.assertEqual(str(a ^ b), "0110")

    def test_not(self):
        a = BinaryNumber("1101")
        self.assertEqual(str(~a), "0010")

    def test_different_length(self):
        a = BinaryNumber("101")
        b = BinaryNumber("11")
        self.assertEqual(str(a & b), "001")
        self.assertEqual(str(a | b), "111")
        self.assertEqual(str(a ^ b), "110")


if __name__ == "__main__":
    unittest.main()

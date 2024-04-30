import unittest

# 定義一個簡單的類
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# 單元測試類，繼承自 unittest.TestCase
class TestCalculator(unittest.TestCase):
    # 測試 add 方法
    def test_add(self):
        calc = Calculator()
        result = calc.add(3, 4)
        self.assertEqual(result, 7)

    # 測試 subtract 方法
    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(7, 4)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()

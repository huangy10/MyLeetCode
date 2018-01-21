import unittest
import random

class Solution(object):

    def intToRoman(self, num):
        def f(num, symbols, digits, prefix):
            if len(symbols) <= 1:
                return prefix + num * symbols[0]

            ten, fiv, one = digits[0: 3]
            sten, sfiv, sone = symbols[0:3]

            digit_ten = num / ten
            if digit_ten > 0:
                num -= digit_ten * ten
                prefix += digit_ten * sten
            digit_one = num / one

            if digit_one == 9:
                prefix += sone + sten
                num -= ten - one
            elif digit_one == 4:
                prefix += sone + sfiv
                num -= fiv - one
            elif digit_one > 4:
                prefix += sfiv + sone * (digit_one - 5)
                num -= fiv + (digit_one - 5) * one

            return f(num, symbols[2:], digits[2:], prefix)

        return f(num, "MDCLXVI", [1000, 500, 100, 50, 10, 5, 1], "")

    def simple_one(self, num):
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10]


class TestSolution(unittest.TestCase):

    def test_roman(self):
        s = Solution()
        res = s.intToRoman(9)
        self.assertEqual(res, "IX")

    def test_with_simple_one(self):
        s = Solution()
        test_number = random.randint(0, 4000)
        self.assertEqual(s.intToRoman(test_number), s.intToRoman(test_number))


if __name__ == "__main__":
    unittest.main()
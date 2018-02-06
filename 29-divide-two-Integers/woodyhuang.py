# https://leetcode.com/problems/divide-two-integers/description/
import unittest


class Solution(object):

    def divide(self, dividend, divisor):
        if divisor == 0 or (dividend == - 1 << 31 and divisor == -1):
            return (1 << 31) - 1
        sign = -1 if (dividend > 0) != (divisor > 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        remaining = dividend
        digits = []
        while remaining >= divisor:
            digit_level = 1
            while divisor << digit_level <= remaining:
                digit_level += 1
            digits.append(digit_level - 1)
            remaining -= divisor << (digit_level - 1)
        res = sum([1 << x for x in digits])
        return res if sign > 0 else -res


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        print s.divide(-2147483648, -1)


if __name__ == '__main__':
    unittest.main()

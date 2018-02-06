# coding=utf-8
import unittest
import re


class Solution(object):
    def myAtoi(self, str):
        """ change string into int
         - remove whitespace characters automatically
         - the string can contain additional characters after valid integer number


        :type str: str
        :rtype: int
        """
        res = re.match(r"^([+\-]?\d+).*$", str.strip())
        if res is None:
            return 0
        return min(max(int(res.group(1)), -2147483648), 2147483647)


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        self.assertEqual(s.myAtoi("1"), 1)
        self.assertEqual(s.myAtoi("+1"), 1)
        self.assertEqual(s.myAtoi("-1"), -1)
        self.assertEqual(s.myAtoi("  +1"), 1)
        self.assertEqual(s.myAtoi("+1a1"), 1)
        self.assertEqual(s.myAtoi("+a1"), 0)
        self.assertEqual(s.myAtoi("+1a"), 1)
        self.assertEqual(s.myAtoi(""), 0)
        self.assertEqual(s.myAtoi("2147483648"), 2147483647)
        self.assertEqual(s.myAtoi("-2147483649"), -2147483648)


if __name__ == '__main__':
    unittest.main()

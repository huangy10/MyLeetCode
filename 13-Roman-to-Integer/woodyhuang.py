# https://leetcode.com/problems/roman-to-integer/description/
import unittest


class Solution(object):

    def romanToInt(self, s):
        num = 0
        mapping = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for idx, symb in enumerate(s):
            if idx < len(s) - 1 and mapping[s[idx + 1]] > mapping[symb]:
                num -= mapping[symb]
            else:
                num += mapping[symb]
        return num


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        res = s.romanToInt("DCXXI")
        self.assertEqual(res, 621)


if __name__ == '__main__':
    unittest.main()

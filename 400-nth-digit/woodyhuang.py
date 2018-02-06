# https://leetcode.com/problems/nth-digit/description/
import unittest


class Solution(object):
    def findNthDigit(self, n):
        if n == 0:
            return ""

        def find_with_level(nn, level, unit):
            # print nn, level
            next_unit = 10 * unit
            digit_cur_level = level * (next_unit - unit)
            if nn < digit_cur_level:
                x = nn / level
                y = nn % level
                # print x, y, nn
                return str(x + unit)[y]
            return find_with_level(nn - digit_cur_level, level + 1, next_unit)

        return find_with_level(n - 1, 1, 1)


class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        for i in range(200):
            res = s.findNthDigit(i)
            print res,


if __name__ == '__main__':
    unittest.main()
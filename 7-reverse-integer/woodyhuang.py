import unittest


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = abs(x) / x if x != 0 else 1
        rev = int(repr(sign * x)[::-1])
        return sign * rev * (rev < 2**31)


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        self.assertEqual(s.reverse(123), 321)
        self.assertEqual(s.reverse(-123), -321)
        self.assertEqual(s.reverse(0), 0)
        self.assertEqual(s.reverse(2**33), 0)


if __name__ == '__main__':
    unittest.main()

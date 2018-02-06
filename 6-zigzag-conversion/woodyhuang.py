import unittest
from operator import itemgetter


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        tmp, res, period = [], [], numRows - 1
        for (idx, ele) in enumerate(s):
            tmp.append((ele, abs(idx % (2 * period) - period)))
        for r in range(numRows)[::-1]:
            res.append(filter(lambda x: x[1] == r, tmp))
        return "".join([item[0] for sublist in res for item in sublist])

    def import_efficiency(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        res, period = [], numRows - 1
        for (idx, ele) in enumerate(s):
            res.append((ele, abs(idx % (2 * period) - period)))
        res = sorted(res, key=itemgetter(1), reverse=True)
        return "".join([x[0] for x in res])


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(Solution().import_efficiency("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")


if __name__ == '__main__':
    unittest.main()

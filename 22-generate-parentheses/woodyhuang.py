# https://leetcode.com/problems/generate-parentheses/description/
import unittest


class Solution(object):

    def generateParentheses(self, n):
        def generate(m):
            if m == 0:
                return {}
            if m == 1:
                return {"()"}
            buf = generate(m - 1)
            res = set()
            for i in buf:
                res.add("({})".format(i))
                res.add("(){}".format(i))
                res.add("{}()".format(i))
            return res
        return list(generate(n))

    def generateParentheses2(self, n):
        buf = []

        def generate(m):
            if m == 0:
                return {}
            if m == 1:
                return {"()"}
            # build query buffer
            for i in range(len(buf), m):
                buf.append(generate(i))
            res = {"({})".format(x) for x in buf[m - 1]}
            for i in range(1, m):
                res = res.union({x + y for x in buf[i] for y in buf[m - i]})
            return res

        return list(generate(n))

class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        print s.generateParentheses2(4)


if __name__ == '__main__':
    unittest.main()
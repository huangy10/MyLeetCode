# https://leetcode.com/problems/implement-strstr/description/
import unittest


class Solution(object):

    def strStr(self, haystack, needle):
        for idx in range(len(haystack) - len(needle) + 1):
            if haystack[idx: idx + len(needle)] == needle:
                return idx
        return -1


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        print s.strStr("abcd", "d")


if __name__ == '__main__':
    unittest.main()

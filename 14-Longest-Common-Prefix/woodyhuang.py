# https://leetcode.com/problems/longest-common-prefix/description/

import unittest


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix_len = 0
        flag = True
        while flag and prefix_len <= len(strs[0]):
            prefix_len += 1
            for s in strs[1:]:
                if s[0:prefix_len] != strs[0][0:prefix_len]:
                    flag = False
                    break
        return strs[0][0:prefix_len - 1]


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["a", "b"]), "")
        self.assertEqual(s.longestCommonPrefix([]), "")
        self.assertEqual(s.longestCommonPrefix(["", ""]), "")

if __name__ == '__main__':
    unittest.main()
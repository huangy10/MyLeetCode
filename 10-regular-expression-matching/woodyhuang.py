import unittest


class Solution(object):

    def isMatch(self, s, p):
        if len(s) > 0 and len(p) > 0 and p[0] in [s[0], "."]:
            if len(p) > 1 and p[1] == "*":
                if len(p) > 2:
                    return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                return self.isMatch(s[1:], p)
            else:
                return self.isMatch(s[1:], p[1:])
        elif len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:])
        return len(s) == 0 and len(p) == 0
    

class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        t = s.isMatch
        self.assertFalse(t("aa", "a"))
        self.assertTrue(t("aa", "aa"))
        self.assertFalse(t("aaa", "aa"))
        self.assertTrue(t("aa", "a*"))
        self.assertTrue(t("aa", ".*"))
        self.assertTrue(t("ab", ".*"))
        self.assertTrue(t("abba", "ab*a"))
        self.assertTrue(t("abba", "ab*a*"))
        self.assertTrue(t("aab", "c*a*b"))
        self.assertFalse(t("abcd", "d*"))
        self.assertTrue(t("aaa", "ab*a*c*a"))


if __name__ == '__main__':
    unittest.main()

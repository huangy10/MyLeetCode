# https://leetcode.com/problems/valid-parentheses/description/
import unittest


class Solution(object):

    def isValid(self, s):
        buf = []
        for item in s:
            if item in "{([":
                buf.append(item)
            elif len(buf) == 0:
                return False
            else:
                left = buf.pop(-1)
                if left + item not in ["{}", "()", "[]"]:
                    return False
        return len(buf) == 0


class TestSolution(unittest.TestCase):

    def test_valid_parentheses(self):
        s = Solution()
        self.assertTrue(s.isValid("{}()[]"))

    def test_invalid_parentheses(self):
        s = Solution()
        self.assertFalse(s.isValid("{{}"))

    def test_right_parentheses_only(self):
        s = Solution()
        self.assertFalse(s.isValid("}}}"))

    def test_complicated_input(self):
        s = Solution()
        self.assertTrue(s.isValid("{[()[()()]()]}"))


if __name__ == '__main__':
    unittest.main()

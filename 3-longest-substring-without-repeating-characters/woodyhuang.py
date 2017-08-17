import unittest


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head, tail, l = 0, 0, 0
        while tail < len(s):
            print head, tail
            tmp = s[head: tail]
            if s[tail] in tmp:
                head = head + tmp.index(s[tail]) + 1
            else:
                l = max(l, tail - head + 1)
            tail += 1
        return l


class TestSolution(unittest.TestCase):

    def test_string_with_same_character(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("bbb"), 1)

    def test_normal_string(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring("pwwkew"), 3)

    def test_empty_string(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(""), 0)


if __name__ == '__main__':
    unittest.main()

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

import unittest


class Solution(object):

    def letterCombination(self, digits):
        if len(digits) == 0:
            return []
        mapping = {"0": " ", "1": "", "2": "abc", "3": "def", "4": "ghi",
                   "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = [""]
        for d in digits:
            res = [b + a for a in mapping[d] for b in res]
        return res

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
import unittest


class Solution(object):

    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        idx = 0
        pre_val = nums[0]
        for n in nums:
            if n == pre_val:
                continue
            idx += 1
            nums[idx] = n
            pre_val = n
        return idx + 1


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        data = [1, 1, 2, 3, 3, 5, 5, 5, 5, 5, 6]
        res = s.removeDuplicates(data)
        print res, data


if __name__ == '__main__':
    unittest.main()

# https://leetcode.com/problems/3sum-closest/description/

import unittest


class Solution(object):
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        res = None
        res_err = None
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                err = abs(target - s)

                print nums[i], nums[j], nums[k], s, err
                if res_err is None or err < res_err:
                    res_err = err
                    res = s
                    print res
                if target > s:
                    j += 1
                elif target < s:
                    k -= 1
                else:
                    return target
        return res


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        res = s.threeSumClosest([-1, 2, 1, -4], 1)
        self.assertEqual(res, 2)

    def test_solution_2(self):
        s = Solution()
        res = s.threeSumClosest([-1, 2, 1, -4], 10)
        self.assertEqual(res, 2)

    def test_solution_3(self):
        s = Solution()
        res = s.threeSumClosest([-55, -24, -18, -11, -7, -3, 4, 5, 6, 9, 11, 23, 33], 0)
        self.assertEqual(res, 0)

    def test_solution_4(self):
        s = Solution()
        res = s.threeSumClosest([1, 1, 1, 0], -100)
        self.assertEqual(res, 2)


if __name__ == '__main__':
    unittest.main()

import unittest


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_v = 0
        pre_m_i_h = 1
        for i in range(len(height) - 1):
            if height[i] < pre_m_i_h:
                continue
            j = len(height) - 1
            min_j = i + max_v / height[i]
            while j > min_j:
                v = (j - i) * min(height[i], height[j])
                # print i, j, height[i], height[j], max_v, v
                if max_v < v:
                    max_v = v
                    pre_m_i_h = height[i]
                    min_j = i + max_v / height[i]
                j -= 1
        return max_v


class TestSolution(unittest.TestCase):

    def test_solution(self):
        print Solution().maxArea(list(range(15000, 0, -1)))


if __name__ == '__main__':
    unittest.main()

import unittest
import random

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i, j = 0, 0
        new_array = []
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                new_array.extend(nums2[j:])
                break
            elif j == len(nums2):
                new_array.extend(nums1[i:])
                break

            if nums1[i] <= nums2[j]:
                new_array.append(nums1[i])
                i += 1

            else:
                new_array.append(nums2[j])
                j += 1

        total_len = len(nums1) + len(nums2)
        if total_len % 2:
            return new_array[total_len / 2]
        else:
            return float(new_array[(total_len + 1) / 2] + new_array[(total_len - 1) / 2]) / 2

    def findMedianSortedArraysFaster(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        half_length = (m + n + 1) / 2

        i_left, i_right = 0, m
        while i_left <= i_right:
            i = (i_left + i_right) / 2
            j = half_length - i
            print i, j

            if (i > 0 and nums1[i - 1] > nums2[j]) or j < 0:
                # i is too big
                i_right = i - 1
            elif i < m and nums1[i] < nums2[j - 1]:
                # i is too small
                i_left = i + 1
            else:
                inf = float('inf')
                max_of_left = max(nums1[i-1] if i > 0 else -inf, nums2[j-1] if j > 0 else -inf)
                if (m + n) % 2 == 1:
                    return max_of_left
                min_of_right = min(nums1[i] if i < m else inf, nums2[j] if j < n else inf)
                return float(max_of_left + min_of_right) / 2


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        nums1 = sorted([random.randint(-1000, 1000) for _ in range(10)])
        nums2 = sorted([random.randint(-1000, 1000) for _ in range(8)])
        print nums1
        print nums2
        print "========"
        self.assertEqual(
            s.findMedianSortedArrays(nums1, nums2),
            s.findMedianSortedArraysFaster(nums1, nums2)
        )


if __name__ == '__main__':
    unittest.main()

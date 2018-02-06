# https://leetcode.com/problems/merge-k-sorted-lists/#/description
import unittest
import copy
import random
from Queue import PriorityQueue

# Definition for singly-linked list.


class ListNode(object):

    def __repr__(self):
        res = repr(self.val)
        node = self.next
        while node is not None:
            res = "%s, %s" % (res, node.val)
            node = node.next
        return res

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = filter(lambda x: x is not None, lists)
        tail = ListNode(None)
        res = tail
        while len(lists) > 0:
            idx, val = self.find_min_idx(lists)
            tail.next = lists[idx]
            tail = tail.next
            if tail.next is None:
                del lists[idx]
            else:
                lists[idx] = tail.next
        return res.next

    def mergeKLists_discuss_solution(self, lists):
        # using priority queue
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next

    def find_min_idx(self, lists):
        if len(lists) == 0:
            return None, None
        idx = 0
        val = lists[0].val
        for i, node in enumerate(lists):
            if node.val < val:
                idx = i
                val = node.val
        return idx, val


class TestSolution(unittest.TestCase):

    def setUp(self):
        print "\n==== %s" % self._testMethodName
        lists = []
        print "The test data is: "
        for _ in range(4):
            sample_list = sorted(random.sample(range(100), 10))
            prev = None
            node = None
            for val in sample_list[::-1]:
                node = ListNode(val)
                node.next = prev
                prev = node
            lists.append(node)
            print node
        self.lists = lists

    def test_solution(self):
        res = Solution().mergeKLists(self.lists)
        print "Result is"
        print res

    def test_discuss_solution(self):
        res = Solution().mergeKLists_discuss_solution(self.lists)
        print "Result is"
        print res

    def test_cross_check(self):
        lists = copy.deepcopy(self.lists)
        self.assertNotEqual(lists, self.lists)
        solution = Solution()

        res1 = solution.mergeKLists(self.lists)
        res2 = solution.mergeKLists_discuss_solution(lists)
        hook = res1
        while res1 is not None or res2 is not None:
            self.assertEquals(res1.val, res2.val)
            res1 = res1.next
            res2 = res2.next
        print hook


if __name__ == '__main__':
    unittest.main()


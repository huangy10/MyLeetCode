# https://leetcode.com/problems/swap-nodes-in-pairs/description/
import unittest


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swapPairs(self, head):
        root = ListNode(None)
        root.next = head
        head = root
        while head is not None:
            if head.next is None or head.next.next is None:
                break
            # head -> a -> b -> b.next
            a = head.next
            b = a.next
            a.next = b.next
            head.next = b
            b.next = a
            head = a
        return root.next


class TestSolution(unittest.TestCase):

    @staticmethod
    def list_to_linked_list(l):
        root = ListNode(None)
        tail = root
        for i in l:
            tail.next = ListNode(i)
            tail = tail.next
        return root.next

    @staticmethod
    def linked_list_to_list(l):
        res = []
        while l is not None:
            res.append(l.val)
            l = l.next
        return res

    def test_solution(self):
        s = Solution()
        data = self.list_to_linked_list([1, 2])
        res = s.swapPairs(data)
        print self.linked_list_to_list(res)


if __name__ == '__main__':
    unittest.main()

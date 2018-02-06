# https://leetcode.com/problems/merge-two-sorted-lists/description/
import unittest


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        tail = head
        while l1 is not None or l2 is not None:
            if l1 is None:
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        return head.next


class TestSolution(unittest.TestCase):

    @staticmethod
    def list_to_linked_list(l):
        head = ListNode(0)
        tail = head
        for item in l:
            tail.next = ListNode(item)
            tail = tail.next
        return head.next

    @staticmethod
    def linked_list_to_list(l):
        res = []
        while l is not None:
            res.append(l.val)
            l = l.next
        return res

    def test_solution(self):
        s = Solution()
        res = s.mergeTwoLists(
            self.list_to_linked_list([1, 2, 4]), self.list_to_linked_list([1, 3, 4])
        )
        self.assertEqual(self.linked_list_to_list(res), [1, 1, 2, 3, 4, 4])


if __name__ == '__main__':
    unittest.main()

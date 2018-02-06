# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
import unittest


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseKGroup(self, head, k):
        root = ListNode(None)
        root.next = head
        last_end = root
        tail = root
        end = last_end.next
        while True:
            for _ in range(k):
                if tail.next is None:
                    return root.next
                tail = tail.next
            a = last_end
            b = a.next
            c = b.next
            for idx in range(k - 1):
                b.next = a
                a = b
                b = c
                c = c.next
            last_end.next = b
            b.next = a
            end.next = c
            last_end = end
            tail = end
            end = c


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
        data = self.list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        res = s.reverseKGroup(data, 4)
        print self.linked_list_to_list(res)


if __name__ == '__main__':
    unittest.main()


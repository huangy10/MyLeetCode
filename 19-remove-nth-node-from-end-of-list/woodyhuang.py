# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        if head is None or head.next is None:
            return None

        def remove(h):
            if h.next is None:
                return 1
            res = remove(h.next)
            if res == n:
                h.next = h.next.next
                return None
            elif res is None:
                return None
            else:
                return res + 1
        if remove(head) is not None:
            return head.next
        else:
            return head

    def removeNthFromEnd_nonrecursive(self, head, n):
        if head is None:
            return None
        buf = [head]
        while buf[-1].next is not None:
            if len(buf) > n:
                buf.pop(0)
            buf.append(buf[-1].next)
        if len(buf) == n:
            return head.next
        else:
            buf[0].next = buf[1].next
            return head


class TestSolution(unittest.TestCase):

    @staticmethod
    def linked_list_to_list(head):
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res

    def test_solution(self):
        data = []
        for i in range(5):
            data.append(ListNode(i + 1))
        for i in range(4):
            data[i].next = data[i + 1]
        s = Solution()
        # res = s.removeNthFromEnd(data[0], 1)
        res = s.removeNthFromEnd_nonrecursive(data[0], 2)
        self.assertEqual(self.linked_list_to_list(res), [1, 2, 3, 5])

    def test_solution_remove_head(self):
        data = []
        for i in range(5):
            data.append(ListNode(i + 1))
        for i in range(4):
            data[i].next = data[i + 1]
        s = Solution()
        # res = s.removeNthFromEnd(data[0], 1)
        res = s.removeNthFromEnd_nonrecursive(data[0], 5)
        self.assertEqual(self.linked_list_to_list(res), [2, 3, 4, 5])

    def test_solution_with_empty_input(self):
        s = Solution()
        self.assertIsNone(s.removeNthFromEnd_nonrecursive(None, 0))

    def test_solution_with_one_node(self):
        s = Solution()
        self.assertIsNone(s.removeNthFromEnd_nonrecursive(ListNode(1), 1))

if __name__ == '__main__':
    unittest.main()

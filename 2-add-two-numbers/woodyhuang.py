# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x, y = l1, l2
        res = ListNode(0)
        head = res
        cout = 0
        while x or y:
            cal = (x or head).val + (y or head).val + cout
            cout = cal / 10
            cal = cal - cout * 10
            res.next = ListNode(cal)
            res = res.next
            x = x.next if x is not None else None
            y = y.next if y is not None else None
        if cout != 0:
            res.next = ListNode(cout)
        return head.next

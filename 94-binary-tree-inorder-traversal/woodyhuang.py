# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        if root is None:
            return []
        buf = [root]
        res = []
        while len(buf) > 0:
            node = buf.pop(-1)
            if node.left is None and node.right is None:
                res.append(node.val)
                continue
            if node.right is not None:
                buf.append(node.right)
                node.right = None
            buf.append(node)
            if node.left is not None:
                buf.append(node.left)
                node.left = None
        return res


class TestSolution(unittest.TestCase):

    def test_solution(self):
        tree = {}
        for i in "abcdefg":
            tree[i] = TreeNode(i)
        tree["a"].left = tree["b"]
        tree["a"].right = tree["c"]
        tree["b"].left = tree["d"]
        tree["b"].right = tree["f"]
        tree["d"].right = tree["e"]
        tree["f"].left = tree["g"]
        s = Solution()
        print s.inorderTraversal(tree["a"])


if __name__ == '__main__':
    unittest.main()

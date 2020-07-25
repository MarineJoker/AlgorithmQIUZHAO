# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:


    # iteratively
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right



    def inorderTraversal(self, root):
        self.ans = []
        if root:
            self.find_next(root)
        return self.ans


    def find_next(self, root):
        if root.left:
            self.find_next(root.left)
        self.ans.append(root.val)
        if root.right:
            self.find_next(root.right)

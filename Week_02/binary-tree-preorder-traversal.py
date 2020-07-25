# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], deque([])
        if not root: return res
        # 栈模拟递归
        stack.appendleft(root)
        while stack:
            tmp = stack.popleft()
            res.append(tmp.val)
            if tmp.right:
                stack.appendleft(tmp.right)
            if tmp.left:
                stack.appendleft(tmp.left)
        return res

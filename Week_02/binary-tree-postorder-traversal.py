# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:

    def find_level(self, root):
        if root.left:
            self.find_level(root.left)
        if root.right:
            self.find_level(root.right)
        self.ans_list.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans_list = []
        if root: self.find_level(root)
        return self.ans_list


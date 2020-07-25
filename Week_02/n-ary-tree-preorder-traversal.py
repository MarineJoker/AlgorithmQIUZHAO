"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ans_list = []
        if root:
            self.ans_list.append(root.val)
            self.find_next(root)
        return self.ans_list

    def find_next(self, node):
        if node.children:
            for t in node.children:
                self.ans_list.append(t.val)
                self.find_next(t)

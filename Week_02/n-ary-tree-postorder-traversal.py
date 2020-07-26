"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:

    def find_level(self, root):
        if root.children:
            for tmp in root.children:
                self.find_level(tmp)
                self.ans_list.append(tmp.val)


    def postorder(self, root: 'Node') -> List[int]:
        self.ans_list = []
        if root:
            self.find_level(root)
            self.ans_list.append(root.val)
        return self.ans_list

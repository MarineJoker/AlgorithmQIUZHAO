# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 单纯的操作指针,自己想复杂了
# 国际版优秀解法
class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 自己的挫解法

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 哈希
        # 1.判重后处理方案跳过该节点直接指向后面的节点
        # 2.双链表(简单)
        # init
        if head is None:
            return head
        self.duplicate_map = { head.val:1 }
        self.traverse(head.next, head)
        return head

    # 快慢指针
    def traverse(self, node1, node2):
        node1.next = node1.next.next
        traverse(node1.next)

        # print(node1.val)
        if node1 is None:
            node2.next =None
            return
        if node1.val not in self.duplicate_map:
            self.duplicate_map[node1.val] = 1 #放入过滤器
            node2.next = node1 #慢指针同步
            self.traverse(node1.next, node1)
        else:
            self.traverse(node1.next, node2)

# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        You are given the head of a singly linked-list. The list can be represented as:

        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        You may not modify the values in the list's nodes. Only nodes themselves may be changed.
        
        Approach: Have a list where index maps to position of the node.
        Take 2 pointers walking from front and end of the list, and start interleaving the nodes
        
        dummyHead -> [L0, L1, L2, L3, L4, L5, L6]
        lo = L0
        hi = LN
        L0 -> L5 -> L1 -> L4 -> L2 -> L3
        """
        node_list = []
        n = 0
        while head:
            node_list.append(head)
            n += 1
            head = head.next
        
        dummy_head = ListNode()
        curr = dummy_head
        lo, hi = 0, n-1
        while lo <= hi:
            
            if lo == hi:
                curr.next = node_list[lo]
                break
            else:
                curr.next = node_list[lo]
                node_list[lo].next = node_list[hi]
                curr = node_list[hi]
                lo += 1
                hi -= 1
        
        node_list[lo].next = None
        return dummy_head.next
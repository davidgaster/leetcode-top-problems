# https://leetcode.com/problems/reverse-linked-list/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
        return prev
        
    def recursive(self, prev, curr):
        if not curr:
            return prev

        tmp = curr.next
        curr.next = prev
        return helper(curr, tmp)
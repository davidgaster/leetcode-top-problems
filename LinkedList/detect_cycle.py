# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    Approach: One faster pointer and one slow pointer. If the fast pointer catches the slow one,
    there is a cycle. If the slow one makes it to the end, there is no cycle.
    O(N)
    '''
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            
            if fast == slow:
                return True
            
            slow = slow.next
            fast = fast.next.next
        
        return False
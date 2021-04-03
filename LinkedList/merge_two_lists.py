# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Two pointer approach, walk the pointer forward that has the lesser element.
    Return the new list.
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        dummyHead = ListNode()
        curr = dummyHead
        while l1 or l2:
            
            if l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
            elif l1:
                curr.next = l1
                l1 = l1.next
            elif l2:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        return dummyHead.next
    '''
    1 -> 2 -> 5 -> 6
    3 -> 4 -> 8

    Take the lower valued node, set its next pointer to be the merging of the rest of that list with
    the other list.
    '''
    def recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        if l1.val < l2.val:
            l1.next = self.recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.recursive(l1, l2.next)
            return l2
        
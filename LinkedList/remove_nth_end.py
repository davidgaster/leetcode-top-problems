# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Approach 1: Done in 1 pass. O(N) space
    Maintain a list where the index maps to the node.
    Delete the node at len(list) - n
    
    Approach 2: Done in 2 passes. Get the length of the list.
    In the second pass, go len(list) - n places forward and delete that node.
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        
        node_list = []
        i = 0
        while head:
            node_list.append(head)
            i += 1
            head = head.next
        
        # only 1 node
        if i == 0 or i == 1:
            return None
        
        # deleting front of list
        if n == i:
            return node_list[1]
        
        pos = i - n
        prev = node_list[pos-1]
        curr = node_list[pos]
        prev.next = curr.next
        curr.next = curr = None
        return node_list[0]
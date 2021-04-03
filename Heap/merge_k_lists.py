import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Approach 1: Divide and Conquer (Merge sort)
    Call merge two lists on all the lists, one after the other. 
    Make sure not to re-merge already merged lists as to not reprocess the same elements
    a redundant number of times during merges.
    
    i  [
    0     1 -> 2 -> 5 -> 6 -> 8 -> 9 -> 17  
    1     3 -> 6                                      
    2     2 -> 8 -> 9         
    3     5 -> 9 -> 10
    4     8 -> 9 -> 17
       ]
    start = 0
    end = 2
    mid = 1
    '''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.mergeSort(lists, 0, len(lists)-1)
    
    def mergeSort(self, lists: List[ListNode], start: int, end: int) -> ListNode:
        if start == end:
            return lists[start]

        if start < end:
            mid = start + (end - start) // 2
            l1 = self.mergeSort(lists, start, mid)
            l2 = self.mergeSort(lists, mid+1, end)
            return self.merge2Lists(l1, l2)
        else:
            return None


    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        if l1.val < l2.val:
            l1.next = self.merge2Lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge2Lists(l1, l2.next)
            return l2
                    
    # Approach 2: Heap Sort
    # Add all the elements to a heap. Pop every element off of the heap and build the list.
    # This is known as heap sort. MUCH FASTER (no recursion stack call slow down)           
    def heap_sort(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        
        dummy_head = ListNode()
        head = dummy_head
        while heap:
            val = heapq.heappop(heap)
            head.next = ListNode(val)
            head = head.next
        
        return dummy_head.next
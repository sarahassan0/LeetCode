# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        ls1, ls2 = list1, list2

        while ls1 or ls2:

            if ls1:
                if a == 1:
                    prev = ls1
                if b == 0:
                    ls1_tail = ls1.next
        
                ls1 = ls1.next
        
            if ls2: 
                if not ls2.next:
                    ls2_tail = ls2
        
                ls2 = ls2.next
    
            a -= 1
            b -=1

        prev.next = list2
        ls2_tail.next = ls1_tail

        return list1
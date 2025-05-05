# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        left = 0

        dummy = node = ListNode()

        while l1 or l2 or left:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            v = v1 + v2 + left
            left = v // 10
            node.next = ListNode(v % 10)
            
            if l1: l1 = l1.next 
            if l2: l2 = l2.next 
            node = node.next

        return dummy.next




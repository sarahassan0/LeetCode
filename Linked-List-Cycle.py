# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

#---------------- Solution using slow & fast pointers --------

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#------------------ Solution using exter space --------
        # seen = []
    
        # while head:
        #     if head in seen:
        #         return True
        #     seen.append(head)
        #     head = head.next
        
        # return False

        
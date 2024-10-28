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

            fast = fast.next.next

            if slow == fast:
                return True

            slow = slow.next

        return False

#------------------ Solution using exter space --------

        # tmp = head
        # nodes = []
    
        # while tmp:
        #     if tmp in nodes:
        #         return True
        #     nodes.append(tmp)
        #     tmp = tmp.next
        
        # return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:\

    #------------- iterative solution ------------------
        curr, prev = head, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        return prev
    #------------- recursive solution ------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#----------------Two pointers solution -------

        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp

        return prev


#---------------- Stack solution --------------
        # stack = []
        # cur = head

        # while cur:
        #     stack.append(cur)
        #     cur = cur.next

        # head = stack.pop() if stack else None
        # cur = head

        # while stack:
        #     cur.next = stack.pop()
        #     cur = cur.next

        # if cur:
        #     cur.next = None

        # return head
        
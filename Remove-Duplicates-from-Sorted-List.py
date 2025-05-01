# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head

        while curr and curr.next :
            if curr.val == curr.next.val:
               curr.next = curr.next.next
            else:
                curr = curr.next
          
        return head

#_______________________________________________________________________________

        # if not head or not head.next:
        #     return head

        # arr = []
        
        # curr = head 
        # while(curr):
        #     if curr.val not in arr:
        #         arr.append(curr.val)
        #     curr = curr.next


        # curr = head
        # for i in arr:
        #     curr.val = i
        #     if i != arr[-1]:
        #         curr = curr.next

        # curr.next = None
        
        # return head

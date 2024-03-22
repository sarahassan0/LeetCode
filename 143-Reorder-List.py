# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        stack = []
        tmp = head
        while tmp:
            stack.append(tmp)
            tmp = tmp.next


        left, right = 0, len(stack)-1
        while left <= right:
            node1 = stack[left]
            left += 1

            node2 = stack[right]
            right -= 1

            node1.next, node2.next = node2, node1.next

        node2.next = None


# -------------------------Brute force Solution 
      

        # stack = []
        # tmp = head
        # while tmp:
        #     stack.append(tmp)
        #     tmp = tmp.next

        # length = len(stack) 
        # for i in range(length):
        #     if i % 2 == 0 :
        #         node = stack.pop(0)
        #     else:
        #         node = stack.pop()
            
        #     if i == 0 :
        #         tmp = node

        #     tmp.next = node
        #     tmp = tmp.next  

        #     if i == length -1 :
        #         tmp.next = None

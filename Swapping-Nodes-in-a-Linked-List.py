# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, second, tmp = head, head, head

        while tmp.next:
            tmp = tmp.next
            if k - 1:
                first = tmp
                k -= 1
            else:
                second = second.next

        first.val, second.val = second.val, first.val 
        return head


    #------------------------------
        # nodes = []
        # current = head
        # while current:
        #     nodes.append(current)
        #     current = current.next
        
        # nodes[k - 1].val, nodes[-k].val = nodes[-k].val, nodes[k - 1].val
        
        # return head
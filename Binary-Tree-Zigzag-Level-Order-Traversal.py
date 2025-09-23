from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue = deque([root])
        result = []
        order = -1

        while queue:
            order *= -1
            level_size = len(queue)
            curr_level = []

            for _ in range(level_size):
                curr = queue.popleft()
                curr_level.append(curr.val)
            
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(curr_level[::order])

        return result

#---- Using Queue, more effeciant than level[::order] because it copy and rewrite the arr --------

        if not root:
            return []
        
        queue = deque([root])
        result = []
        order = -1

        while queue:
            order *= -1
            level_size = len(queue)
            curr_level = deque()

            for _ in range(level_size):
                curr = queue.popleft()

                if order == 1:
                    curr_level.append(curr.val)
                else:
                    curr_level.appendleft(curr.val)
            
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(list(curr_level))
            
        return result
        
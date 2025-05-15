from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        queue = deque([root])
        result = []
        order = -1

        while queue:
            level_size = len(queue) 
            order *= -1 
            level = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(level[::order])

        return result


#---- Using Queue, more effeciant than level[::order] because it copy and rewrite the arr --------

        if root is None:
            return []
        queue = deque([root])
        result = []
        order = -1

        while queue:
            level_size = len(queue) 
            order *= -1 
            level = deque()
            
            for _ in range(level_size):
                curr = queue.popleft()

                if order == 1:
                    level.append(curr.val)
                else:
                    level.appendleft(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            result.append(list(level))
        return result
        
        
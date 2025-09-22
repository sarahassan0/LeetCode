# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

       
        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            curr_level = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                curr_level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(curr_level)

        return result[::-1]
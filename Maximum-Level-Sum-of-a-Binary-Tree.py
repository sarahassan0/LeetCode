# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        maxi = [float('-inf'), 0]
        level = 0

        while queue:
            level_size = len(queue)
            level_sum = 0
            level += 1 

            for _ in range(level_size):
                curr = queue.popleft()
                level_sum += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            if level_sum > maxi[0]:
                maxi = [level_sum, level]
                
        return maxi[1]
    
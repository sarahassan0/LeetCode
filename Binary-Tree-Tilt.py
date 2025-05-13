# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt = 0
        
        def dfs(root):
            
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            self.tilt += abs(left - right)

            return left + right + root.val
        
        dfs(root)
        return self.tilt


            

        
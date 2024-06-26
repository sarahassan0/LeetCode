# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], path_sum="") -> int:
    
        if not root:
            return 0

        path_sum = path_sum + str(root.val)
    
        if not root.left and not root.right:
            return int(path_sum)


        return self.sumNumbers(root.left,path_sum) + self.sumNumbers(root.right,path_sum)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], is_left=False) -> int:

        if not root:
            return 0
        
        if not root.left and not root.right and is_left:
            return root.val

        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)

        






        
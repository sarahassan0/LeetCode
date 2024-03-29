# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode], result=None) -> List[int]:

        if result is None:
            result = []

        if root:
            if root.left:
                self.postorderTraversal(root.left, result)

            if root.right:
                self.postorderTraversal(root.right, result)  
            
            result.append(root.val)

        return result
        
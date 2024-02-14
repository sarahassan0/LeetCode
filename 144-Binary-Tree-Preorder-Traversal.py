# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode], result=[]) -> List[int]:
        if not result:
            result = []

        if root:
            result.append(root.val)  
            if root.left:
                self.preorderTraversal(root.left, result)  # Recursively traverse left subtree
            if root.right:
                self.preorderTraversal(root.right, result)  # Recursively traverse right subtree
        return result
            

        # return result
        
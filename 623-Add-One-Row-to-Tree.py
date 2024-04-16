# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int, cur_depth=1) -> Optional[TreeNode]:


        if not root:
            return None

        if depth == 1:
            tree = TreeNode(val=val, left=root)
            return tree


        if cur_depth == depth - 1:
            leftTree = TreeNode(val=val, left=root.left)
            rightTree = TreeNode(val=val, right=root.right)
            root.left = leftTree
            root.right = rightTree
            return root

        

        self.addOneRow(root.left, val, depth, cur_depth + 1)
        self.addOneRow(root.right, val, depth, cur_depth + 1)

        return root

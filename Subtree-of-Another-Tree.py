class Solution:
    def isIdentical(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        # didnt return isIdentical() directly because multiple nodes in the tree might match
        # the subRoot.val, and isSubtree should try all of them, even if one match fails.
        if root.val == subRoot.val and self.isIdentical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        

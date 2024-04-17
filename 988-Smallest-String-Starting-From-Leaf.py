class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode],path="") -> str:
     
        if not root:
            return '~' # '~' represents a large value string in lexicographical comparison
        
        path += chr(ord('a') + root.val)
        
        if not root.left and not root.right :
            return path[::-1] 
        
        left_path = self.smallestFromLeaf(root.left, path) 
        right_path= self.smallestFromLeaf(root.right, path) 

        return min(left_path, right_path)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        max_ = 0

        while queue:
            level_size = len(queue)
            _, leftPos = queue[0]
            _, rightPos = queue[level_size-1]

            for i in range(level_size):
                curr, pos = queue.popleft()
                
                if curr.left:
                    queue.append((curr.left, 2 * pos))
                if curr.right:
                    queue.append((curr.right, 2 * pos + 1))

            max_ = max(max_, (rightPos - leftPos + 1))

        return max_

        
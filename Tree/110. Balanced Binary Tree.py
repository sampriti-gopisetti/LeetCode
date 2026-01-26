# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.balanced = True
        def maxdepth(root):
            if root is None:
                return 0
            left = maxdepth(root.left)
            right = maxdepth(root.right)
            if abs(left - right) > 1:
                self.balanced = False
            return 1 + max(left, right)
        maxdepth(root)
        return self.balanced

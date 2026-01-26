# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maximum = 0
        def maxdepth(root):
            if root is None:
                return 0
            leftdepth = maxdepth(root.left)
            rightdepth = maxdepth(root.right)
            if leftdepth + rightdepth > self.maximum:
                self.maximum = leftdepth + rightdepth
            return 1 + max(leftdepth, rightdepth)
        depth = maxdepth(root)
        return self.maximum

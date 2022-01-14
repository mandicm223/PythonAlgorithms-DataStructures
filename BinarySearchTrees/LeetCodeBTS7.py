'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left , root.right)
    
    def isMirror(self , leftroot , rightroot):
        if leftroot and rightroot:
            return (leftroot.val == rightroot.val) and self.isMirror(leftroot.right , rightroot.left) and self.isMirror(leftroot.left , rightroot.right)
        return leftroot == rightroot
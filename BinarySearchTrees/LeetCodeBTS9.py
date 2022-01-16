# Definition for a binary tree node.
'''
Given the root of a Binary Search Tree (BST),
return the minimum absolute difference between the values of any two different nodes in the tree.
'''


class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None
        
        inorder = []
        
        self.fill_inorder(root , inorder)
        
        min_diff = float('inf')
        
        for i in range(1 , len(inorder)):
            min_diff = min(min_diff , inorder[i] - inorder[i-1])
        return min_diff        
    def fill_inorder(self , root , inorder):
        if root is None:
            return []
        return (self.fill_inorder(root.left , inorder) ,
               inorder.append(root.val) ,
               self.fill_inorder(root.right , inorder))
        
        
        
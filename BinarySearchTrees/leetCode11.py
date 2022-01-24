import collections
'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            lenQ = len(q)
            level = []
            
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
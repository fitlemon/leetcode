'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    '''
    
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = set()
        def dfs(node, lvl):
            if not node:
                return
            depth.add(lvl)
            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)
        if not root:
            return 0
        dfs(root, 1)    
        return max(depth)
    
    
# Good Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def dfs(root, depth):
        #     if not root:
        #         return depth
        
        #     return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        # return dfs(root, 0)
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0
        
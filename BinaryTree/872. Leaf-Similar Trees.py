'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
'''
'''
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []
        def fill_leaves_list(root: Optional[TreeNode], lst: list) -> list:
            if not root:
                return
            result = not root.left and not root.right

            if not root.left and not root.right:
                lst.append(root.val)
            fill_leaves_list(root.left, lst)
            fill_leaves_list(root.right, lst)
            return lst

        if fill_leaves_list(root1, leaves1) == fill_leaves_list(root2, leaves2):
            return True
        else:
            return False
        

l1_2 = TreeNode(2)
l1_3 = TreeNode(3)
root1 = TreeNode(1, l1_2, l1_3)
root2 = TreeNode(1, l1_3, l1_2)

sl = Solution()
print(sl.leafSimilar(root1, root2))
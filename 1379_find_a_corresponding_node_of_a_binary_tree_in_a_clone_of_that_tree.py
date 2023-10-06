# Given two binary trees original and cloned and given a reference to a node target in the original tree.
#
# The cloned tree is a copy of the original tree.
#
# Return a reference to the same node in the cloned tree.
#
# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference
# to a node in the cloned tree.

# Definition for a binary tree node.
from copy import deepcopy


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
    
    def __str__(self):
        return f'{self.val}'


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def checker(n, t, c):
            if n is None:
                return
            if n is t:
                return c
            output = checker(n.left, t, c.left)
            if output:
                return output
            return checker(n.right, t, c.right)
        
        return checker(original, target, cloned)


if __name__ == '__main__':
    target = TreeNode(3,
                      TreeNode(6),
                      TreeNode(19)
                      )
    original = TreeNode(7,
                        TreeNode(4),
                        target,
                        )
    
    clone = deepcopy(original)
    
    s = Solution().getTargetCopy(original, clone, target)
    print(s)

# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the
# others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes
# overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as
# the node of the new tree.
#
# Return the merged tree.
#
# Note: The merging process must start from the root nodes of both trees.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def merge_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    node = None
    if root1 and root2:
        node = TreeNode(root1.val + root2.val)
        node.left = merge_trees(root1.left, root2.left)
        node.right = merge_trees(root1.right, root2.right)
    elif root1:
        node = TreeNode(root1.val)
        node.left = merge_trees(root1.left, None)
        node.right = merge_trees(root1.right, None)
    elif root2:
        node = TreeNode(root2.val)
        node.left = merge_trees(None, root2.left)
        node.right = merge_trees(None, root2.right)

    return node


if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    t2 = TreeNode(2,
                  TreeNode(1, None, TreeNode(4)),
                  TreeNode(3, None, TreeNode(7)))

    res = merge_trees(t1, t2)
    print(res)

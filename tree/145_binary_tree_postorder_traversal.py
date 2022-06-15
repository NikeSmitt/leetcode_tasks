# Given the root of a binary tree, return the postorder traversal of its nodes' values.
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: TreeNode, acc: list):
            if node is not None:
                dfs(node.left, acc)
                dfs(node.right, acc)
                acc.append(node.val)
            return acc
        
        return dfs(root, [])


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(1,
                    left=None,
                    right=TreeNode(
                        2,
                        left=TreeNode(3)
                    ))
    print(s.postorderTraversal(tree))

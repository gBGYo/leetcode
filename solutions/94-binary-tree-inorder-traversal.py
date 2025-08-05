from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return traverse_rec(root)
        return traverse_iter(root)


# Recursive solution
def traverse_rec(root: Optional[TreeNode]):
    if root == None:
        return []
    l = []
    if root.left != None:
        l += traverse_rec(root.left)
    l += [root.val]
    if root.right != None:
        l += traverse_rec(root.right)
    return l


# Iterative solution using stack
def traverse_iter(root: Optional[TreeNode]):
    l = []
    s = []
    cur = root
    while s or cur:
        while cur:
            s.append(cur)
            cur = cur.left
        cur = s.pop()
        l.append(cur.val)
        cur = cur.right
    return l


if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    sol = Solution()
    print(sol.inorderTraversal(root))

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return compare_rec(p, q)


is_exclusive_none = lambda p, q: q == None and p != None or q != None and p == None


# Recursive comparison
def compare_rec(p: Optional[TreeNode], q: Optional[TreeNode]):
    if p == None and q == None:
        return True

    if is_exclusive_none(p, q):
        return False

    assert p != None and q != None
    p_val = p.val
    q_val = q.val

    if p_val != q_val:
        return False

    if compare_rec(p.left, q.left) and compare_rec(p.right, q.right):
        return True
    return False


# Iterative comparison
def compare_iter(p: Optional[TreeNode], q: Optional[TreeNode]):
    sp = []
    sq = []
    curp = p
    curq = q
    while sp or sq or curp or curq:
        while curp or curq:
            if is_exclusive_none(curp, curq):
                return False
            sp.append(curp)
            curp = curp.left
            sq.append(curq)
            curq = curq.left
        curp = sp.pop()
        curq = sq.pop()
        if curp.val != curq.val:
            return False
        curp = curp.right
        curq = curq.right
    return True


if __name__ == "__main__":
    p = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    q = TreeNode(1, None, TreeNode(2, TreeNode(1)))
    # p = None
    # q = None
    # p = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    # q = TreeNode(1, TreeNode(5), TreeNode(2, TreeNode(1)))
    sol = Solution()
    print(sol.isSameTree(p, q))

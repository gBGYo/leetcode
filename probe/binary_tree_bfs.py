from queue import Queue
from typing import Self


class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right

    def bfs(self):
        q = Queue()
        q.put(self)
        while not q.empty():
            level_size = q.qsize()
            for i in range(level_size):
                cur = q.get()
                print(cur.val, end=" ")
                if cur.left != None:
                    q.put(cur.left)
                if cur.right != None:
                    q.put(cur.right)
            print()


if __name__ == "__main__":
    root = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
    )
    root.bfs()

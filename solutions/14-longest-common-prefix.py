from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return run1(strs)


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_terminal: bool = False


class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_terminal = True

    def common_prefix(self):
        prefix = []
        cur = self.root
        # NOTE for future me:
        # i failed at ["", "b"] since "" does not
        # add anything to the Trie, but "b" does.
        # At the same time "" is already a terminal.
        # So it is wise to check if current node is already a terminal,
        # and if it is --- stop the iteration
        # -----------
        # Also another example ["dog", "dogdog"].
        # If we does not check that current node is a terminal
        # we will end up in a situation where LCP is dogdog,
        # because length of current dictionary in fact will be 1
        # for each node of the Trie
        # (since "dog" is in "dogdog" and there will be no branching)
        while len(cur.children) == 1 and cur.is_terminal == False:
            c, cur = next(iter(cur.children.items()))
            prefix.append(c)
        return "".join(prefix)


def debug_trie(node, indent=0):
    pad = "  " * indent
    print(f"{pad}Node(end={node.is_terminal})")
    for char, child in node.children.items():
        print(f"{pad}  '{char}':")
        debug_trie(child, indent + 2)


def run1(strs):
    trie = Trie()
    for word in strs:
        trie.insert(word)
    debug_trie(trie.root)
    return trie.common_prefix()


if __name__ == "__main__":
    words = ["flower", "flow", "flight"]
    words = ["dog", "racecar", "car"]
    words = ["", "b"]
    words = ["dog", "dogdog"]
    sol = Solution()
    ret = sol.longestCommonPrefix(words)
    print(ret)

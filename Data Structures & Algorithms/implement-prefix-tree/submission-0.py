from typing import Optional

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        node = self._find_match_node(word)
        return node and node.word

    def startsWith(self, prefix: str) -> bool:
        return self._find_match_node(prefix) is not None

    def _find_match_node(self, s: str) -> Optional[TrieNode]:
        cur = self.root
        for c in s:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur

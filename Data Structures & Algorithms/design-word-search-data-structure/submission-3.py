class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(root, index):
            curr = root

            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:   
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_word

        return dfs(self.root, 0)
                

from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def remove(self, word: str) -> None:
        self._remove(self.root, word, 0)

    def _remove(self, node: TrieNode, word: str, i: int) -> None:
        if i == len(word):
            node.is_word = False
            return

        ch = word[i]
        if ch not in node.children:
            return

        child = node.children[ch]
        self._remove(child, word, i + 1)

        if not child.children and not child.is_word:
            del node.children[ch]


t = Trie()

t.insert("abc")
t.insert("ab")
t.insert("ad")
t.insert("xy")

t.remove("abc")

print(t)

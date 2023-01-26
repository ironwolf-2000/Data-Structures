from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    """
    n = number of added words
    W = sum(len(words[i])), 0 <= i < n
    -------------
    Space: O(W)
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        N = len(word)
        -------------
        Time: O(N)
        """
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        N = len(word)
        -------------
        Time: O(N)
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        N = len(prefix)
        -------------
        Time: O(N)
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def remove(self, word: str) -> None:
        """
        N = len(word)
        -------------
        Time: O(N)
        Extra Space: O(N)
        """
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


trie = Trie()

trie.insert("abc")
trie.insert("ab")
trie.insert("ad")
trie.insert("xy")

# Removes the letter "c" from the trie but keeps "a" and "b" because "b" is the end of the word "ab".
trie.remove("abc")

# Removes both "x" and "y" from the trie.
trie.remove("xy")

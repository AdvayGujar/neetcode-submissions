class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class PrefixTree:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        node = self.head

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.head

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.head

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
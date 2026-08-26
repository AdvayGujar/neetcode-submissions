class TrieNode:
    def __init__(self, data = None):
        self.value = data
        self.isWord = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        node = self.head

        for i in range(len(word)):
            if word[:i+1] in node.children:
                node = node.children[word[:i+1]]
            else:
                newNode = TrieNode(word[:i+1])
                node.children[word[:i+1]] = newNode
                node = newNode
        
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.head

        for i in range(len(word)):
            if word[:i+1] not in node.children:
                return False
            else:
                node = node.children[word[:i+1]]
        
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.head

        for i in range(len(prefix)):
            if prefix[:i+1] not in node.children:
                return False
            else:
                node = node.children[prefix[:i+1]]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
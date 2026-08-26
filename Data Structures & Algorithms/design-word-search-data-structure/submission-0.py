class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.head

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.isWord = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            for i in range(index, len(word)):
                char = word[i]
                
                if char == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            
            return node.isWord
        
        return dfs(0, self.head)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
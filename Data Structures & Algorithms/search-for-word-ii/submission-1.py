class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
        self.refs = 0

    def addWord(self, word):
        curr = self
        curr.refs += 1

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
            
            curr.refs += 1
        
        curr.isWord = True

    def removeWord(self, word):
        curr = self
        curr.refs -= 1

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = TrieNode()

        for w in words:
            head.addWord(w)

        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                (r, c) in visited or 
                board[r][c] not in node.children or 
                node.children[board[r][c]].refs <= 0
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                node.isWord = False
                res.append(word)
                head.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        res = []
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, head, "")

        return res
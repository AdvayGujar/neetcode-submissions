import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        beginSet = {beginWord}
        endSet = {endWord}
        visited = set()
        steps = 1
        
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            nextSet = set()
            
            for word in beginSet:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c == word[i]:
                            continue
                        
                        newWord = word[:i] + c + word[i+1:]
                        
                        if newWord in endSet:
                            return steps + 1
                        
                        if newWord in wordSet and newWord not in visited:
                            visited.add(newWord)
                            nextSet.add(newWord)
            
            beginSet = nextSet
            steps += 1
        
        return 0
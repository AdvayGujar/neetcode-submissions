class FoundMatchingString(Exception):
    pass

class Solution:
    def search(self, board, currRow, currColumn, word, traversed):
        if (currRow, currColumn) in traversed:
            return

        if word[0] == board[currRow][currColumn]:
            if word[1:] == "":
                raise FoundMatchingString()

            traversed.add((currRow, currColumn))

            #North
            if currRow > 0 :
                self.search(board, currRow - 1, currColumn, word[1:], traversed)

            #West
            if currColumn > 0:
                self.search(board, currRow, currColumn - 1, word[1:], traversed)
            
            #East
            if currColumn < len(board[0]) - 1:
                self.search(board, currRow, currColumn + 1, word[1:], traversed)

            #South
            if currRow < len(board) - 1:
                self.search(board, currRow + 1, currColumn, word[1:], traversed)

            traversed.remove((currRow, currColumn))
        else:
            return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []

        for word in words:
            try:
                for row in range(len(board)):
                    for column in range(len(board[0])):
                        traversed = set()
                        self.search(board, row, column, word, traversed)
            except FoundMatchingString:
                result.append(word)

        return result
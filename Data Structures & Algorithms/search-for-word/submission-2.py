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


    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False

        try:
            for row in range(len(board)):
                for column in range(len(board[0])):
                    if board[row][column] == word[0]:
                        traversed = set()
                        self.search(board, row, column, word, traversed)
            
            return False
        except FoundMatchingString:
            return True
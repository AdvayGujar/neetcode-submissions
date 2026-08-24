class FoundMatchingString(Exception):
    pass

class Solution:
    def search(self, board, currRow, currColumn, word, incoming):
        if word[0] == board[currRow][currColumn]:
            if word[1:] == "":
                raise FoundMatchingString()

            #North
            if currRow > 0 and incoming != "North":
                self.search(board, currRow - 1, currColumn, word[1:], "South")

            #West
            if currColumn > 0 and incoming != "West":
                self.search(board, currRow, currColumn - 1, word[1:], "East")
            
            #East
            if currColumn < len(board[0]) - 1 and incoming != "East":
                self.search(board, currRow, currColumn + 1, word[1:], "West")

            #South
            if currRow < len(board) - 1 and incoming != "South":
                self.search(board, currRow + 1, currColumn, word[1:], "North")
        else:
            return


    def exist(self, board: List[List[str]], word: str) -> bool:
        try:
            for row in range(len(board)):
                for column in range(len(board[0])):
                    self.search(board, row, column, word, "")
            
            return False
        except FoundMatchingString:
            return True
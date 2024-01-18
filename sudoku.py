class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        unique = set()

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    b = "("+board[i][j]+")"
                    row = str(i)+b
                    col = b+str(j)
                    box = str(i/3) + b + str(j/3)
                    if row in unique or col in unique or box in unique:
                        return False
                    unique.add(row)
                    unique.add(col)
                    unique.add(box)
        return True
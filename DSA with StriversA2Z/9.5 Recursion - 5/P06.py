def solveSuduku(board):
    def isSafe(r,c,num):
        for i in range(9):
            if board[r][i]==num:
                return False
            if board[i][c]==num:
                return False
        newrow =(r//3)*3
        newcol = (c//3)*3
        for i in range(newrow,newrow+3):
            for j in range(newcol,newcol+3):
                if board[i][j]==num:
                    return False
        return True
    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    for num in "123456789":
                        if isSafe(r,c,num):
                            board[r][c]=num
                            if backtrack():
                                return True 
                            board[r][c]="."
                    return False
        return True
    backtrack()
    return board
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(solveSuduku(board))
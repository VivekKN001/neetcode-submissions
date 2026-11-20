class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(row, col, board, n):
            dumRow, dumCol = row, col
            # Upper Part
            while(row>=0 and col>=0):
                if board[row][col] == 'Q':
                    return False
                row-=1
                col-=1
            # Middle Part
            row, col = dumRow, dumCol
            while (col>=0):
                if board[row][col] == 'Q':
                    return False
                col-=1
            # Lower Part
            row, col = dumRow, dumCol
            while(row<n and col>=0):
                if board[row][col] == 'Q':
                    return False
                row+=1
                col-=1
            return True
        
        def solve_n_queens(col, board, ans, n):
            if (col>=n):
                ans.append([''.join(row) for row in board])
                return
            for row in range(n):
                if (isSafe(row, col, board, n)):
                    board[row][col] = 'Q'
                    solve_n_queens(col+1, board, ans, n)
                    board[row][col] = '.'
            return ans

        board = []
        col = 0
        for i in range(n):
            board.append(['.'] * n)
        ans = []
        ans = solve_n_queens(col, board, ans, n)
        return ans
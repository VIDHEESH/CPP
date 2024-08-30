#User function Template for python3
class Solution:
    def nQueen(self, n):
        # code here
        def is_safe(board,row,col):
            for i in range(row):
                if board[i]==col or board[i]-i==col-row or board[i]+i==col+row:
                    return False
            return True
        def solve_n_queens(n,row,board,result):
            if row==n:
                result.append(board[:])
                return
            for col in range(n):
                if is_safe(board,row,col):
                    board[row]=col
                    solve_n_queens(n,row+1,board,result)
        result=[]
        solve_n_queens(n,0,[0]*n,result)
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j]+=1
        return result

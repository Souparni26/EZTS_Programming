def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

   
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queen_util(board, col, n):
   
    if col >= n:
        return True

    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  

            
            if solve_n_queen_util(board, col + 1, n):
                return True

            board[i][col] = 0  

    return False
def solve_n_queen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queen_util(board, 0, n):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True
n = 6
solve_n_queen(n)
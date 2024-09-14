# Backtracking

# Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, 
# one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.

# Backtracking can be thought of as a selective tree/graph traversal method. The tree is built as the algorithm runs, 
# and branches that fail to meet the constraints are pruned.

# Key concepts:
# 1. Choice: At each step, we make a choice from the available options.
# 2. Constraints: We check if our choice satisfies the given constraints.
# 3. Goal: We check if we've reached the desired solution.

# Here's a general template for backtracking:

# def backtrack(candidate):
#     if find_solution(candidate):
#         output(candidate)
#         return
    
#     for next_candidate in list_of_candidates:
#         if is_valid(next_candidate):
#             place(next_candidate)
#             backtrack(next_candidate)
#             remove(next_candidate)

# Let's implement a classic backtracking problem: N-Queens

# N-Queens is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
# This means that no two queens can be in the same row, column, or diagonal.
# The solution requires us to find all possible configurations of the queens on the board.

# The backtracking algorithm works by placing a queen on the board and then recursively trying to place the next queen in a safe position.
# If a queen cannot be placed in a safe position, the algorithm backtracks and tries a different position.
# This process continues until all queens are placed on the board, or until it is determined that no safe configuration is possible.
# The algorithm is efficient and works well for small values of N.

def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        return True

    def backtrack(board, col):
        if col >= n:
            result.append([''.join(row) for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                backtrack(board, col + 1)
                board[i][col] = '.'  # Backtrack

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return result

# Example usage:
n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()

# Another example: Subset Sum Problem

def subset_sum(numbers, target, partial=None):
    if partial is None:
        partial = []
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print(f"Sum({partial})={target}")
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])

# Example usage:
print("Subset Sum Problem:")
subset_sum([3, 34, 4, 12, 5, 2], 9)

# Backtracking is powerful for solving combinatorial problems, puzzles, and optimization tasks.
# It's used in various applications like:
# - Sudoku solvers
# - Path finding in mazes
# - Constraint satisfaction problems
# - Combinatorial optimization
# Remember that while backtracking can solve many problems, it may have exponential time complexity 
# in the worst case, so it's important to consider the problem size and constraints.

#!/usr/bin/python3
"""Solve the N-Queens problem using backtracking."""


import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen in the given position.

    Args:
        board (list): The chessboard represented as a 2D list.
        row (int): The row index.
        col (int): The column index.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_board(board, N):
    """
    Print the current state of the chessboard.

    Args:
        board (list): The chessboard represented as a 2D list.
        N (int): The size of the chessboard.
    """
    for i in range(N):
        print("".join(["Q" if board[i][j] else "." for j in range(N)]))
    print()

def solve_nqueens(N):
    """
    Solve the N-Queens problem and print the solutions.

    Args:
        N (int): The size of the chessboard.

    Raises:
        SystemExit: If N is less than 4, print an error message and exit.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_util(board, 0, N)

def solve_util(board, col, N):
    """
    Helper function to recursively solve the N-Queens problem.

    Args:
        board (list): The chessboard represented as a 2D list.
        col (int): The current column index.
        N (int): The size of the chessboard.
    """
    if col == N:
        print_board(board, N)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_util(board, col + 1, N)
            board[i][col] = 0

def main():
    """
    Main function to parse command line arguments and initiate the solution.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

if __name__ == "__main__":
    main()

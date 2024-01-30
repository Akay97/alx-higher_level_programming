#!/usr/bin/python3
"""
Solves the N-queens puzzle by determining all possible solutions for placing N non-attacking queens on an NxN chessboard.

Usage: ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): 2D list representing the chessboard.
    solutions (list): List of queen positions, each in the format [row, column].

Example:
    $ ./101-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
"""
import sys

def init_board(n):
    """
    Initializes an `n`x`n` chessboard with 0's.

    Args:
        n (int): Size of the chessboard.

    Returns:
        list: Initialized chessboard.
    """
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def board_deepcopy(board):
    """
    Returns a deepcopy of a chessboard.

    Args:
        board (list): Chessboard.

    Returns:
        list: Deepcopy of the chessboard.
    """
    return [row.copy() for row in board]

def get_solution(board):
    """
    Returns the list of queen positions from a solved chessboard.

    Args:
        board (list): Chessboard.

    Returns:
        list: Queen positions in the format [row, column].
    """
    return [[r, c] for r in range(len(board)) for c in range(len(board)) if board[r][c] == 'Q']

def xout(board, row, col):
    """
    Marks spots on the chessboard where queens cannot be placed.

    Args:
        board (list): Current working chessboard.
        row (int): Row where a queen was last placed.
        col (int): Column where a queen was last placed.
    """
    for c in range(col + 1, len(board)): board[row][c] = 'x'
    for c in range(col - 1, -1, -1): board[row][c] = 'x'
    for r in range(row + 1, len(board)): board[r][col] = 'x'
    for r in range(row - 1, -1, -1): board[r][col] = 'x'
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board): break
        board[r][c] = 'x'
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0: break
        board[r][c] = 'x'
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board): break
        board[r][c] = 'x'
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0: break
        board[r][c] = 'x'
        c -= 1

def recursive_solve(board, row, queens, solutions):
    """
    Recursively solves an N-queens puzzle.

    Args:
        board (list): Current working chessboard.
        row (int): Current working row.
        queens (int): Current number of placed queens.
        solutions (list): List of lists of solutions.

    Returns:
        list: List of queen positions for each solution.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == ' ':
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = 'Q'
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        print("Usage: nqueens N (N must be an integer greater than or equal to 4)")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)

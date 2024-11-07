#!/usr/bin/env python3
"""
N-Queens solver using backtracking
"""

import sys


def print_usage_and_exit():
    """Prints usage info and exits with status 1"""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_args():
    """Validates command-line arguments and returns integer N"""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at board[row][col]
    Queens are non-attacking if:
    - No other queens are in the same column
    - No other queens are in the same major diagonal
    - No other queens are in the same minor diagonal
    """
    for r in range(row):
        if board[r] == col or \
           board[r] - r == col - row or \
           board[r] + r == col + row:
            return False
    return True


def solve_nqueens(N, row=0, board=[]):
    """
    Solves N-Queens puzzle using backtracking.
    Prints each solution as a list of [row, col] positions.
    """
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(N, row + 1, board)
            board.pop()


if __name__ == "__main__":
    N = validate_args()
    solve_nqueens(N)

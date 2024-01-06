#!/usr/bin/python3
"""
    A program that solves the N queens problem.
    The N queens puzzle is the challenge of placing N non-attacking
    queens on an N×N chessboard.
"""

import sys


def set_board(dimension):
    """creates and sets chess board N x N to 0"""
    return [[0 for column in range(dimension)] for row in range(dimension)]


def get_solution(chess_board, N):
    """gets the solution and stores it in a matrix"""
    solution = []
    for row in range(N):
        for column in range(N):
            if chess_board[row][column]:
                solution.append([row, column])
                break
    return solution


def check_safety(chess_board, row, column, N):
    """checks if the current position is safe for a Queen
    """
    # checks from beginning of row to current Queen's position
    for i in range(column):
        if chess_board[row][i]:
            return False

    # checks from current Queen's position diagonally to left top
    j = column - 1
    for i in range(row - 1, -1, -1):
        if chess_board[i][j]:
            return False
        j -= 1

    # checks from current Queen's position diagonally to left bottom
    j = column - 1
    for i in range(row + 1, N, 1):
        if chess_board[i][j]:
            return False
        j -= 1

    return True


def solve_N_Queen(chess_board, column, N, solutions):
    """solves the solution for the N Queens"""
    # base case
    if column == N:
        solutions.append(get_solution(chess_board, N))
        solutions.sort()
        return

    for row in range(N):
        if check_safety(chess_board, row, column, N):
            chess_board[row][column] = 1
            solve_N_Queen(chess_board, column + 1, N, solutions)
            chess_board[row][column] = 0  # backtrack

    return


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]
if not N.isdigit():
    print("N must be a number")
    sys.exit(1)

N = int(N)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

chess_board = set_board(N)
solutions = []
solve_N_Queen(chess_board, 0, N, solutions)
[print(solution) for solution in solutions]

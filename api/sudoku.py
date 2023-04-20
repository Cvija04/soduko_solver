from sudoku import Sudoku


def generate_board():
    sudoku = Sudoku(3).difficulty(0.9)
    board = sudoku.board
    return board

def solve_board(board):
    if not isinstance(board, list) or len(board) != 9 or any(len(row) != 9 for row in board):
        raise ValueError("Not a valid board, must input some parameters")
    sudoku = Sudoku(3, board=board)
    solver = sudoku.solve()
    solved_board = solver.board
    return solved_board

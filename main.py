from CSP.Solver import Solver
from SecretSanta.SecretSantaProblem import SecretSantaProblem
from States.StatesProblem import StatesProblem
from Sudoku.SudokuProblem import SudokuProblem

#
# states = StatesProblem()
# s = Solver(states, use_forward_check=True)
# s.solve()
# states.print_assignments()
#
#
# secret_santa = SecretSantaProblem(['arman', 'alice', 'nader', 'bob', 'sarah', 'iman'])
# secret_santa = SecretSantaProblem([str(i) for i in range(100)])
# # secret_santa.assign_givers_and_receivers()
# s = Solver(secret_santa)
# s.solve()
# secret_santa.print_assignments()
# #

grid = [
    [2, 0, 0, 3, 0, 0, 0, 0, 0],
    [8, 0, 4, 0, 6, 2, 0, 0, 3],
    [0, 1, 3, 8, 0, 0, 2, 0, 0],

    [0, 0, 0, 0, 2, 0, 3, 9, 0],
    [5, 0, 7, 0, 0, 0, 6, 2, 1],
    [0, 3, 2, 0, 0, 6, 0, 0, 0],

    [0, 2, 0, 0, 0, 9, 1, 4, 0],
    [6, 0, 1, 2, 5, 0, 8, 0, 9],
    [0, 0, 0, 0, 0, 1, 0, 0, 2]
]

grid1 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],

    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],

    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

grid2 = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],

    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],

    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]

grid3_ex = [
    [0, 1, 0, 0, 0, 6, 4, 0, 0],
    [0, 9, 0, 4, 5, 0, 0, 2, 0],
    [5, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0],
    [9, 0, 0, 1, 8, 0, 7, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 3],
    [8, 0, 0, 9, 4, 0, 1, 0, 0],
    [0, 0, 9, 6, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 7, 0]
]

grid4_ex = [
    [6, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 5, 6, 0, 0, 8],
    [0, 3, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 6, 0, 7, 8, 0, 0, 5],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 1],
    [4, 0, 0, 0, 1, 7, 0, 8, 0],
    [0, 0, 7, 2, 0, 0, 0, 0, 0]
]

grid5_ex = [
    [0, 6, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 3, 0, 0, 0, 0, 2, 0],
    [0, 0, 7, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 9, 0, 4, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 7],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 9, 0, 8]
]

sudoku = SudokuProblem(grid3_ex)
s = Solver(sudoku, use_mrv=True, use_lcv=True)
s.solve()
sudoku.print_assignments()

# state = StatesProblem()
# s = Solver(state)
# s.solve()
# state.print_assignments()

# secret = SecretSantaProblem()
# s = Solver(secret)
# s.solve()
# secret.print_assignments()

# from CSP.Solver import Solver
from SecretSanta.SecretSantaProblem import SecretSantaProblem
from States.StatesProblem import StatesProblem
from Sudoku.SudokuProblem import SudokuProblem
from King.KingProblem import KingProblem
from CSP.Solver import Solver

# states = StatesProblem()
# s = Solver(states, use_lcv=True, use_mrv=False, use_forward_check=False)
# s.solve()
# states.print_assignments()

# secret_santa = SecretSantaProblem(['arman', 'alice', 'nader', 'bob', 'sarah', 'iman'])
# secret_santa = SecretSantaProblem([str(i) for i in range(100)])
# s = Solver(secret_santa, use_lcv=False, use_mrv=True, use_forward_check=False)
# s.solve()
# secret_santa.print_assignments()

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


# sudoku = SudokuProblem(grid)
# s = Solver(sudoku,use_lcv=True,use_mrv=True,use_forward_check=False)
# s.solve()
# sudoku.print_assignments()

#
king = KingProblem()
s = Solver(king ,use_lcv=False,use_mrv=True,use_forward_check=False)
s.solve()
king.print_assignments()

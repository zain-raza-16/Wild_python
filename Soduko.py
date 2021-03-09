from copy import deepcopy


class Solution:

    def __init__(self):
        self.row = None
        self.column = None
        self.answer = None
        self.original_board = None

    def find_last_incomplete_spot(self, bo):
        for i in range(8, 0, -1):
            for j in range(8, 0, -1):
                if bo[i][j] == ".":
                    self.row = i
                    self.column = j
                    return

    def not_in_row_colomn_box(self, grid, pos, number):
        if grid[self.row][self.column] == '.':
            # Check row
            for i in range(9):
                if grid[pos[0]][i] == str(number):  # and pos[1] != i:
                    return False

            # Check column
            for i in range(9):
                if grid[i][pos[1]] == str(number):  # and pos[0] != i:
                    return False

            # Check box
            box_x = pos[1] // 3
            box_y = pos[0] // 3

            for i in range(box_y * 3, box_y * 3 + 3):
                for j in range(box_x * 3, box_x * 3 + 3):
                    if grid[i][j] == str(number) and (i, j) != pos:
                        return False
            return True

    def move_to_next_step(self, current_position):
        if current_position[1] != 8:
            current_position[1] = current_position[1] + 1
            return current_position
        else:
            current_position[0] = current_position[0] + 1
            current_position[1] = 0
            return current_position

    def move_onestep_back(self, current_position):
        if current_position[1] != 0:
            current_position[1] = current_position[1] - 1
            return current_position
        else:
            current_position[0] = current_position[0] - 1
            current_position[1] = 8
            return current_position

    def move_forward(self, grid, current_position):

        if grid[self.row][self.column] != '.':
            if self.answer is None:
                self.answer = grid
            return

        if grid[current_position[0]][current_position[1]] == ".":
            for i in range(1, 10):
                if grid[self.row][self.column] == '.' and self.not_in_row_colomn_box(grid, current_position, i):
                    grid[current_position[0]][current_position[1]] = str(i)
                    current_position = self.move_to_next_step(current_position)
                    self.move_forward(grid, current_position)

            if grid[self.row][self.column] == '.':  # This statement is used to to end loops
                # BackTracking
                current_position = self.move_onestep_back(current_position)
                while self.original_board[current_position[0]][current_position[1]] != '.':
                    current_position = self.move_onestep_back(current_position)
                grid[current_position[0]][current_position[1]] = '.'

        else:
            current_position = self.move_to_next_step(current_position)
            self.move_forward(grid, current_position)

    def solveSudoku(self, board):
        self.original_board = deepcopy(board)
        self.find_last_incomplete_spot(board)
        self.move_forward(board, [0, 0])
        return self.answer


given = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
adam = Solution()
print(adam.solveSudoku(given))
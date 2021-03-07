board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


answer = [['5', '3', '1', '2', '7', '6', '4', '9', '8'],
          ['6', '7', '4', '1', '9', '8', '3', '5', '2'],
          ['2', '9', '8', '3', '4', '5', '7', '6', '1'],
          ['1', '2', '5', '8', '6', '3', '9', '4', '7'],
          ['7', '4', '6', '9', '5', '1', '8', '2', '3'],
          ['3', '8', '9', '7', '2', '4', '5', '1', '6'],
          ['9', '1', '2', '5', '3', '7', '6', '8', '4'],
          ['8', '6', '7', '4', '1', '9', '2', '3', '5'],
          ['4', '5', '3', '6', '8', '2', '1', '7', '9']]

cp = [0, 0]


def print_board(bo):
    for i in range(8):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(8):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def not_in_row_colomn_box(grid, pos, number):
    # Check row
    for i in range(9):
        if grid[pos[0]][i] == str(number): #and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if grid[i][pos[1]] == str(number):#and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == str(number) and (i, j) != pos:
                return False

    return True


def move_to_next_step(current_position):
    if current_position[1] != 8:
        current_position[1] = current_position[1] + 1
        return current_position
    else:
        current_position[0] = current_position[0] + 1
        current_position[1] = 0
        return current_position


def move_onestep_back(current_position):
    if current_position[1] != 0:
        current_position[1] = current_position[1] - 1
        return current_position
    else:
        current_position[0] = current_position[0] - 1
        current_position[1] = 8
        return current_position


def move_forward(grid, current_position):
    if grid[8][6] != '.':
        print(grid)
        return grid

    if grid[current_position[0]][current_position[1]] == ".":
        for i in range(1,10):
            if not_in_row_colomn_box(grid, current_position, i):
                grid[current_position[0]][current_position[1]] = str(i)
                current_position = move_to_next_step(current_position)
                move_forward(grid, current_position)

        current_position = move_onestep_back(current_position)
        grid[current_position[0]][current_position[1]] = '.'

    else:
        current_position = move_to_next_step(current_position)
        move_forward(grid, current_position)

print(move_forward(board,cp))


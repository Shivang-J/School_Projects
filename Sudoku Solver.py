def find_empty_cell(sudoku):
    
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == 0:
                return row, column

    return None, None 

def validity(sudoku, guess, row, column):
    
    row_vals = sudoku[row]
    if guess in row_vals:
        return False 

    column_vals = [sudoku[i][column] for i in range(9)]
    if guess in column_vals:
        return False

    row_start = (row // 3) * 3
    column_start = (column // 3) * 3

    for row in range(row_start, row_start + 3):
        for column in range(column_start, column_start + 3):
            if sudoku[row][column] == guess:
                return False

    return True

def sudoku_solver(sudoku):
    
    row, column = find_empty_cell(sudoku)

    if row is None: 
        return True 

    for guess in range(1, 10):
        if validity(sudoku, guess, row, column):
            sudoku[row][column] = guess
            if sudoku_solver(sudoku):
                return True
        
        sudoku[row][column] = 0

if __name__ == '__main__':
    example_board = [
        [0,9,0,5,0,0,0,0,0],
        [2,0,1,0,0,0,0,4,5],
        [0,0,0,0,2,6,0,0,0],

        [3,4,0,0,0,0,7,0,0],
        [0,0,9,8,0,7,2,0,0],
        [0,0,6,0,0,0,0,1,8],

        [0,0,0,9,4,0,0,0,0],
        [1,8,0,0,0,0,4,0,3],
        [0,0,0,0,0,1,0,2,0]
    ]
    print(sudoku_solver(example_board))
    for i in range(0,9):
        print(example_board[i])


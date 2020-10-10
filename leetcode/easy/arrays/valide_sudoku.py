import logging

BOX_JUMPS = [0, 3, 6]
def validate_sudoku(sudoku):
    return all((validate_rows(sudoku), validate_cols(sudoku), validate_box(sudoku)))
    

def validate_rows(board):
    rows = []
    for row in board:
        rows.append(checkers(row))
    return all(rows)


def validate_cols(board):
    valid_cols = []
    for row in range(len(board)):
        cols = []
        for co in range(len(board)):
            cols.append(board[co][row])
        valid_cols.append(checkers(cols))
    return all(valid_cols)

def validate_box(board):
    valid_box = []
    for i in BOX_JUMPS:
        one, two, three = [], [], []
        for idx in range(i, i+3):
            for ji in range(0, 3):
                one.append(board[idx][ji])
            for ji in range(3, 6):
                two.append(board[idx][ji])
            for ji in range(6, 9):
                three.append(board[idx][ji])
        print(one, two, three)
        for box in [one, two, three]:
            valid_box.append(checkers(box))
    return all(valid_box)

def checkers(vals):
    checker = set()
    for v in vals:
        try:
            integer = int(v)
            if integer > 9 or integer < 1:
                return False
            if integer in checker:
                return False 
            checker.add(integer)
        except ValueError:
            logging.exception("Exception occurred.")
    return True


if __name__ == "__main__":
    BOARD = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    BOARD2 = [
        [".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
    print(validate_sudoku(BOARD2))


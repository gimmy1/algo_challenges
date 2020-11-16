def search_in_sorted_matrix(matrix, target):
    row, col = 0, 0
    while row < len(matrix) and col < len(matrix[0]):
        print(row, col)
        print(matrix[row][col])
        if matrix[row][col] < target:
            col += 1
        elif matrix[row][col] > target:
            col -= 1
            row += 1
        else:
            return [row, col]
    return [-1, -1]

if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ]
    print(search_in_sorted_matrix(matrix, 35))
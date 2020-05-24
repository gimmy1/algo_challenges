def spiral_traverse(arr):
    result = []

    s_row, e_row = 0, len(arr) - 1
    s_col, e_col = 0, len(arr[0]) - 1

    while s_row <= e_row and s_col <= e_col:
        # Iterate over perimeters
        for col in range(s_col, e_col + 1): # top row
            result.append(arr[s_row][col])

        for row in range(s_row + 1, e_row + 1): # right column
            result.append(arr[row][e_col])
        
        for col in reversed(range(s_col, e_col)): # bottom row
            if s_row == e_row:
                break
            result.append(arr[e_row][col])

        for row in reversed(range(s_row + 1, e_row)): # left column
            if s_col == e_col:
                break
            result.append(arr[row][s_col])
        
        # change values
        s_row += 1
        e_row -= 1
        s_col += 1
        e_col -= 1

    return result

if __name__ == "__main__":
    arr1 = [
           [1, 2, 3, 4], # 0
           [12, 13, 14, 5], # 1
           [11, 16, 15, 6], # 2
           [20, 21, 22, 23] # 2
          ]
    
    print(spiral_traverse(arr1))

    
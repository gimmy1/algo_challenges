def kadanes(array):
    max_ending_at_idx = array[0]
    max_so_far = array[0]
    kadanes = array[1:]
    for num in kadanes:
        max_ending_at_idx = max(num, max_ending_at_idx + num)
        max_so_far = max(max_so_far, max_ending_at_idx)
    return max_so_far

if __name__ == "__main__":
    print(kadanes([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))

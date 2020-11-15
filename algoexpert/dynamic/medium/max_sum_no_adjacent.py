def max_sum_non_adjacency(array):
    sums = array
    if not len(array): return array
    if len(array) <= 2: return max(array[0], array[-1])
    
    sums[0] = array[0]
    sums[1] = max(array[0], array[1])
    idx = 2
    while idx < len(array):
        print(sums[idx-1], array[idx] + array[idx-2])
        sums[idx] = max(sums[idx-1], array[idx] + array[idx-2])
        idx += 1
    return sums[-1]

if __name__ == "__main__":
    print(max_sum_non_adjacency([75, 105, 120, 75, 90, 135]))
    print(max_sum_non_adjacency([75]))

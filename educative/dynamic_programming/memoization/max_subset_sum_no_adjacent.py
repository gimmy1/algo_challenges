def max_subset_sum(array, idx, memo = {}):
    if len(array) == 0:
        return 0
    if idx == 0:
        return array[0]
    if idx == 1:
        return max(array[0], array[1])
    
    if idx in memo:
        return memo[idx]
    
    memo[idx] = max(max_subset_sum(array, idx-1, memo),
                    array[idx] + max_subset_sum(array, idx-2, memo))
    
    return memo[idx]



if __name__ == "__main__":
    array = [75, -105, -120, -75, -90, 135] # 210
    
    idx = len(array) - 1
    print(max_subset_sum(array, idx))
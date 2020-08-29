from collections import defaultdict

def subarray_sort(arr):
    index_dict = defaultdict(int)
    minimum = float("inf")
    maximum = float("-inf")
    index_dict[arr[0]] = 0

    i = 1

    # import pdb; pdb.set_trace()
    if len(arr) == 2:
        if sorted(arr) == arr: 
            return [-1,-1]
        else:
            return [0,1]
    while i < len(arr):
        if arr[i] < arr[i-1]:
            value = arr[i]
            iterate = True
            while iterate:
                if value in index_dict:
                    minimum = min(minimum, index_dict[value] + 1) if arr[i] > 0 else min(minimum, index_dict[value])
                    maximum = max(maximum, i+1)
                    iterate = False
                value = value - 1 if arr[i] > 0 else value + 1
        index_dict[arr[i]] = i
        i += 1
    
    return [minimum, maximum]


    

if __name__ == "__main__":
    print(subarray_sort([2, 1]))
    print(subarray_sort([1, -2]))
    print(subarray_sort([1, 2]))
    print(subarray_sort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]))
    print(subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
    print(subarray_sort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]))
    
    print(subarray_sort([1, 2, 3, 4, 5, 6, 18, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19]))
    # HOW DID I THINK OF IT
    # as you iterate over it -- create a dictionary
    # iterate until arr[i] > arr[i-1]
    # jump into a while loop
    # while arr[i] > 0
    # if it equals value in dictionary
    # find_min_index equals the index
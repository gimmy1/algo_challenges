from collections import defaultdict

def subarray_sort(arr):
    index_dict = defaultdict(int)
    minimum = float("inf")
    maximum = float("-inf")

    i = 1
    while i < len(arr):
        if arr[i] < arr[i-1]:
            value = arr[i]
            # import pdb; pdb.set_trace()
            while value > 0:
                # import pdb; pdb.set_trace()
                if value in index_dict:
                    minimum = min(minimum, index_dict[value] + 1)
                    maximum = max(maximum, i+1)
                    break
                value -= 1
        index_dict[arr[i]] = i
        i += 1
    
    return [minimum, maximum]


    

if __name__ == "__main__":
    print(subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
    # HOW DID I THINK OF IT
    # as you iterate over it -- create a dictionary
    # iterate until arr[i] > arr[i-1]
    # jump into a while loop
    # while arr[i] > 0
    # if it equals value in dictionary
    # find_min_index equals the index
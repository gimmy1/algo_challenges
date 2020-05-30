def longest_peak(arr):
    i = 0
    count = 0
    max_peak = float("-inf")
    while i < len(arr) - 1:
        if i < len(arr) - 1 and arr[i+1] > arr[i]:
            while i < len(arr) - 1 and arr[i+1] > arr[i]:
                count += 1
                i += 1
        
        if i < len(arr) - 1 and arr[i+1] < arr[i-1]:
            while i < len(arr) - 1 and arr[i+1] > arr[i]:
                count += 1
                i += 1
        
        if count > max_peak and count > 3:
            max_peak = count
        i = i - 1
    return max_peak


if __name__ == "__main__":
    print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
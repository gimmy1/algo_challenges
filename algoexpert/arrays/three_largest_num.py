def find_three_largest(arr):
    # find 3 largest numbers in an array that are not sorted
    largest = [float("-inf")] * 3
    i = 0
    while i < len(arr):
        if arr[i] > largest[2]:
            largest[0] = largest[1]
            largest[1] = largest[2]
            largest[2] = arr[i]
        elif arr[i] > largest[1]:
            largest[0] = largest[1]
            largest[1] = arr[i]
        elif arr[i] > largest[0]:
            largest[0] = arr[i]
        i += 1
    return sum(largest)

if __name__ == "__main__":
    print(find_three_largest([10, 12, 9, -1, 25, 30]))
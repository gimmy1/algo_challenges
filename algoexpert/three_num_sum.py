def three_num(arr, target):
    triplets = []
    arr.sort()
    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return triplets


if __name__ == "__main__":
    # [3, 6, 10, 17, 19, 24, 90]
    print(three_num([17, 19, 24, 7, 6, 3, 100, 10], 51))
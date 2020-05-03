def smallest_subarray_with_given_sum(arr, k):
    """Given an array of positive numbers and a positive number ‘S’, 
       find the length of the smallest contiguous subarray whose sum 
       is greater than or equal to ‘S’. 
       Return 0, if no such subarray exists."""
    left, right = 0, 0
    length_of_sum = 0
    total = arr[left]
    while right < len(arr) - 1:
        if total >= k:
            curr_length = right - left + 1
            length_of_sum = min(length_of_sum, curr_length)
            total -= arr[left]
            left += 1
        else:
            right += 1
            total += arr[right]
    return length_of_sum

if __name__ == "__main__":
    print(smallest_subarray_with_given_sum([3, 4, 1, 1, 6], 8))
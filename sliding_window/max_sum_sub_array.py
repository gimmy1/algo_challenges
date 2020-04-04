"""
Given an array of positive numbers and a positive number ‘k’,
find the maximum sum of any contiguous subarray of size ‘k’.
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9

Explanation: Subarray with maximum sum is [5, 1, 3].
"""
def max_sum_sub_array_sum(arr, k):
    right = 0
    sub_sum = 0
    sub_sums = list()
    while right < k:
        sub_sum += arr[right]
        right += 1
    
    left = 1
    sub_sums.append(sub_sum)
    while right < len(arr):
        sub_sums.append(sub_sums[-1] - arr[left-1] + arr[right])

        left += 1
        right += 1
    
    return max(sub_sums)

if __name__ == "__main__":
    print(max_sum_sub_array_sum([2, 1, 5, 1, 3, 2], 3))
    print(max_sum_sub_array_sum([2, 3, 4, 1, 5], 2))







    

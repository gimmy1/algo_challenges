from collections import Counter

def intersection_arrays(nums1, nums2):
    """
    nums1 = [4,9,5],
    nums2 = [9,4,9,8,4]
    ans = [9, 4]
    """
    if len(nums1) != len(nums2):
        greater_list = max(nums1, nums2, key=len)
        smaller_list = min(nums1, nums2, key=len)
    else:
        greater_list = nums1
        smaller_list = nums2

    greater_dict = Counter(greater_list)
    intersection_set = set()
    for val in smaller_list:
        if val in greater_dict:
            intersection_set.add(val)
        
    return intersection_set

if __name__ == "__main__":
    print(intersection_arrays([1,2], [1,1]))

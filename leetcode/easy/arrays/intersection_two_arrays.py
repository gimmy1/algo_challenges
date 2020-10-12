from collections import defaultdict
import logging
def intersection_of_two_arrays(L1, L2):
    if len(L1) < len(L2):
        L1, L2 = L2, L1
    
    indexed_list = defaultdict(int)
    intersection = []

    # import pdb; pdb.set_trace()
    for _, val in enumerate(L1):
        indexed_list[val] += 1
    
    # import pdb; pdb.set_trace()
    for val in L2:
        if val in indexed_list and indexed_list[val]:
            indexed_list[val] -= 1
            intersection.append(val)
    
    return intersection

        

        

if __name__ == "__main__":
    print(intersection_of_two_arrays([1,2,2,1], [2,2]))
    print(intersection_of_two_arrays([5,4,9,5,6,11], [9,4,9,8,4]))
    print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))
    print(intersection_of_two_arrays([1], [1]))
    print(intersection_of_two_arrays([1,2], [1,1]))
    print(intersection_of_two_arrays([1,2], [2,1]))

# [3,1,1,2,2]
# [4,2,2]
# Output: [2,2]

# [5,4,9,4,5,6,11]
# [9,4,9,8,4]
# Output: [4,9]
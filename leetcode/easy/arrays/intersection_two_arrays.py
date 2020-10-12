from collections import defaultdict
import logging
def intersection_of_two_arrays(L1, L2):
    larger_list = max(L1, L2, key=len)
    shorter_list = min(L1, L2, key=len)
    indexed_list = defaultdict(list)
    intersection = []
    for idx, val in enumerate(larger_list):
        indexed_list[val].append(idx)
    
    for idx, val in enumerate(shorter_list):
        if val in indexed_list and len(indexed_list[val]) > 0:
            try:
                idx_val = indexed_list[val].pop(0)
                current_size = []
                for v1, v2 in zip(larger_list[idx_val:], shorter_list[idx:]):
                    # import pdb; pdb.set_trace()
                    if v1 != v2:
                        break
                    else:
                        current_size.append(v1)
                        try:
                            idx_val = indexed_list[v1].pop(0)
                        except IndexError:
                            logging.exception("Exception occurred.")
            except IndexError:
                logging.exception("Exception occurred.")
            
            if len(current_size) > len(intersection):
                intersection = current_size
    return intersection

        

if __name__ == "__main__":
    # print(intersection_of_two_arrays([1,2,2,1], [2,2]))
    # print(intersection_of_two_arrays([5,4,9,5,6,11], [9,4,9,8,4]))
    # print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))
    # print(intersection_of_two_arrays([1], [1]))
    print(intersection_of_two_arrays([1,2], [1,1]))

# [3,1,1,2,2]
# [4,2,2]
# Output: [2,2]

# [5,4,9,4,5,6,11]
# [9,4,9,8,4]
# Output: [4,9]
def binary_search(List, target):
    return binary_search_helper(List, target, 0, len(List) - 1)

def binary_search_helper(List, target, left, right):
    if left > right: return -1
    middle_idx = (left + right) // 2
    if len(List) == 1 and List[0] != target:
        return -1
    if List[middle_idx] == target:
        return middle_idx
    if target < List[middle_idx]:
        return binary_search_helper(List, target, left, middle_idx - 1)
    else:
        return binary_search_helper(List, target, middle_idx + 1, right)
    

if __name__ == "__main__":
    print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))

    
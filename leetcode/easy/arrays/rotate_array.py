def rotate_array(List, k):
    """
    Given an array, rotate the array to the right by k steps, where k is non-negative.
    """
    Length = len(List)
    rotated = [False] * Length  
    if k < 0:
        raise ValueError("Value less than zero")
    
    for idx, v in enumerate(List):
        rotated_idx = (idx + k) % Length
        rotated[rotated_idx] = v
    return rotated


def rotate_array_2(List, k):
    count = 0
    start = 0
    while count < len(List):
        curr = start
        prev = List[curr]
        while True:
            idx = (curr + k) % len(List)
            List[idx], prev = prev, List[idx]
            curr = idx
            count += 1
            if start == curr:
                break
        start += 1
    return List

if __name__ == "__main__":
    print(rotate_array_2([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]
    # print(rotate_array([-1,-100,3,99], 2)) # [3,99,-1,-100]
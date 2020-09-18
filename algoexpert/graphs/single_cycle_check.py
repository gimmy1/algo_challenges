def hasSingleCycle(List):
    cycle_length = len(List)
    if List[:(cycle_length//2)] == List[(cycle_length//2):]: return False

    cycle_check = [False] * len(List)
    for idx, val in enumerate(List):
        _jmp = (idx + val) % cycle_length
        cycle_check[_jmp] = List[_jmp]
    return cycle_check == List

if __name__ == "__main__":
    hasSingleCycle([2, 3, 1, -4, -4, 2])
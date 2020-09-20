def hasSingleCycle(List):
    cycle_length = len(List)
    if List[:(cycle_length//2)] == List[(cycle_length//2):]: return False

    cycle_check = [False] * len(List)
    for idx, val in enumerate(List):
        _jmp = (idx + val) % cycle_length
        cycle_check[_jmp] = List[_jmp]
    return cycle_check == List

def hasSingleCycle2(List):
    visited = [False] * len(List)
    _DFS(0, visited, List, 1) # pass in idx, visited, List
    return all(visited)

def _DFS(idx, visited, List, count):
    if count > len(List): return False
    visited[idx] = True
    _jmp = (idx + List[idx]) % len(List)
    if not visited[_jmp]:
        count += 1
        _DFS(_jmp, visited, List, count)


    

if __name__ == "__main__":
    print(hasSingleCycle2([2, 3, 1, -4, -4, 2]))
    print(hasSingleCycle2([1, -1, 1, -1]))
    print(hasSingleCycle([1, 1, 1, 1, 2]))

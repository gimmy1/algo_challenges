# [0,1,0,3,12]
# [1,0,0,3,6,0]
def move_zeroes(List):
    idx = 0
    while idx < len(List):
        if List[idx] == 0:
            jdx = idx + 1
            while jdx < len(List) and List[jdx] == 0:
                jdx += 1

            try:
                List[idx], List[jdx] = List[jdx], List[idx]
            except IndexError:
                return List
        idx += 1
    return List

if __name__ == "__main__":
    print(move_zeroes([0,1,0,3,12]))
    print(move_zeroes([1,0,0,3,6,0]))

def insertion_sort(List):
    idx = 1
    while idx < len(List):
        if List[idx] < List[idx - 1]:
            jdx = idx
            while jdx > 0 and List[jdx] < List[jdx - 1]:
                List[jdx], List[jdx - 1] = List[jdx - 1], List[jdx]
                jdx -= 1
        idx += 1
    return List

if __name__ == "__main__":
    print(insertion_sort([8,5,2,9,5,6,3]))



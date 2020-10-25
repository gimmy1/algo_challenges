def bubble_sort(List):
    """
    How does Bubble Sort work?
    [8,5,2,9,5,6,3]
    """
    idx = 0
    swap = True
    while swap:
        swap = False
        for idx in range(len(List)-1):
            if List[idx] > List[idx + 1]:
                List[idx], List[idx + 1] = List[idx+1], List[idx]
                swap = True
    return List

if __name__ == "__main__":
    print(bubble_sort([8,5,2,9,5,6,3]))



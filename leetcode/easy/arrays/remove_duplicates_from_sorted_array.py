def remove_duplicates(List):
    """
    Given a sorted array, remove all duplicates
    [0,1,1,1,1,2,2,3,3,4]
    """
    jdx = 1
    length = len(List)
    for idx in range(1, length):
        if List[idx] != List[idx-1]:
            List[jdx] = List[idx]
            jdx += 1
    return List[:jdx]

if __name__ == "__main__":
    print(remove_duplicates([0,1,1,1,1,2,2,3,3,4]))
    print(remove_duplicates([1,1,2]))
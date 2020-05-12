def moveElementToEnd(array, toMove):
    idx = 0
    jdx = len(array)-1

    while idx < jdx:
        while idx < jdx and array[jdx] == toMove:
            jdx -= 1
        
        if array[idx] == toMove:
            array[idx], array[jdx] = array[jdx], array[idx]
        
        idx += 1
    return array
        

if __name__ == "__main__":
    print(moveElementToEnd([1, 2, 3, 4, 6, 5, 5, 5, 9, 10, 11, 12, 5, 5], 5))


def isValidSubsequence(array, sequence):
    ix = 0
    jx = 0
    count = 0
    while ix < len(array) and jx < len(sequence):
        while array[ix] != sequence[jx]:
            ix += 1
    
        if array[ix] == sequence[jx]:
            jx += 1
            count += 1
        ix += 1
    return count == len(sequence)




if __name__ == "__main__":
    print(isValidSubsequence([1, 1, 1, 1, 1], [1,1,1]))
    
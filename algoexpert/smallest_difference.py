def smallest_difference(arr1, arr2):
    sarr1 = sorted(arr1)
    sarr2 = sorted(arr2)
    a1 = 0
    a2 = 0
    small = float("inf")
    difference = []
    while a1 < len(arr1) or a1 < len(arr2):
        import pdb; pdb.set_trace()
        val = abs(sarr1[a1] - sarr2[a2])
        if val < small:
            small = val
            try:
                difference.pop()
                difference.append((sarr1[a1], sarr2[a2]))
            except:
                difference.append((sarr1[a1], sarr2[a2]))

        if sarr1[a1] < sarr2[a2]:
            a1 += 1
        elif sarr1[a1] > sarr2[a2]:
            a2 += 1
        else:
            return [sarr1[a1], sarr2[a2]]
    
    return difference



if __name__ == "__main__":
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]
    print(smallest_difference(arrayOne, arrayTwo))

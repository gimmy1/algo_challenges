def merge_lists(a1, a2):
    i = 0
    ji = 0
    merged = []
    while i < len(a1) and ji < len(a2):
        if a1[i] < a2[ji]:
            merged.append(a1[i])
            i += 1
        else:
            merged.append(a2[ji])
            ji += 1
    if i > ji:
        merged.extend(a2[ji:])
    else:
        merged.extend(a1[i:])
    return merged

if __name__ == "__main__":
    print(merge_lists([1,1,1,1], [2,2,2]))

        

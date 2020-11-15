def levenshtein_distance(str1, str2):
    # abc
    # yabd
    edits = []
    for i in range(len(str1) + 1):
        inner = []
        for j in range(len(str2)):
            if j == 0 and i != 0:
                inner.append(i)
            else:
                inner.append(j)
        edits.append(inner)
    
    
    for i in range(1, len(str2) + 1):
        for j in range(len(str1) + 1):
            if str2[i-1] != str1[j-1]:
                edits[i][j] = edits[i-1][j-1]
            else:
                edits[i][j] = 1 + min(edits[i-1][j-1], edits[i-1][j], edits[i][j-1])
    return edits[-1][-1]

if __name__ == "__main__":
    print(levenshtein_distance("abc", "yabd"))
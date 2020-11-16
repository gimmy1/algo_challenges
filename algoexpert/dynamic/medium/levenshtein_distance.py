def levenshtein_distance(str1, str2):
    # abc
    # yabd
    edits = []
    for i in range(len(str2) + 1):
        inner = []
        for j in range(len(str1) + 1):
            if j == 0 and i != 0:
                inner.append(i)
            else:
                inner.append(j)
        edits.append(inner)

    
    for i in range(1, len(str2) + 1):
        for jx in range(1, len(str1) + 1):
            if str2[i-1] == str1[jx-1]:
                edits[i][jx] = edits[i-1][jx-1]
            else:
                edits[i][jx] = 1 + min(edits[i-1][jx-1], edits[i-1][jx], edits[i][jx-1])
    return edits[-1][-1]

if __name__ == "__main__":
    print(levenshtein_distance("abc", "yabd"))
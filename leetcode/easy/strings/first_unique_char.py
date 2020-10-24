from collections import defaultdict
def first_unique_char_string(S):
    unique = defaultdict(int)
    for idx, st in enumerate(S):
        if st in unique:
            unique[st] = -1
        else:
            unique[st] = idx
    
    min_val = [float("inf"), float("inf")] # val, idx
    for key, val in unique.items():
        if val != -1:
            if val < min_val[1]:
                min_val = [key, val]
    
    return min_val[1] if min_val[0] != float("inf") else -1

if __name__ == "__main__":
    print(first_unique_char_string("leetcode"))
    print(first_unique_char_string("loveleetcode"))

            

    
def parts_sums(ls):
    # your code
    i = len(ls) - 1
    sums = [0] * (len(ls) + 1)
    ji = len(sums) - 1
    while ji > 0:
        parts = ls[i] + sums[ji]
        sums[i] = parts
        i -= 1
        ji -= 1
    return sums
        
if __name__ == "__main__":
    print(parts_sums([0, 1, 3, 6, 10]))

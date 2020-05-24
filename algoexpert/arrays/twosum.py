from collections import defaultdict

def twosum(arr, target):
    sums = defaultdict(int)

    for a in arr:
        if (target - a) in sums:
            return [a, target - a]
        else:
            sums[a] = True
    
    return []

if __name__ == "__main__":
    print(twosum([3, 5, -4, 8, 11, 1, -1, 6], 10))
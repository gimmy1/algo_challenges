from operator import itemgetter, xor
from functools import reduce
import heapq
from collections import Counter

def stray_1(arr):
    counter = Counter(arr)
    least_common = heapq.nsmallest(1, counter.items(), key=itemgetter(1))[0] # get second value
    return itemgetter(0)(least_common)

def stray_2(arr):
    return reduce(xor, arr)



if __name__ == "__main__":
    print(stray_1([1, 1, 1, 1, 1, 1, 2]))
    print(stray_2([1, 1, 1, 1, 1, 1, 2]))
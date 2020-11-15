def num_of_ways_to_make_change(coins, target):
    ways = [0 if amount != 0 else 1 for amount in range(target+1)]
    for coin in coins:
        for way in range(1, len(ways)):
            # 1, 1, 1, 3, 4, 2, 6 (1,2,3,4,5,6)
            if coin <= way:
                ways[way] += ways[way - coin]
    return ways[-1]




if __name__ == "__main__":
    num_of_ways_to_make_change([1, 5], 6)
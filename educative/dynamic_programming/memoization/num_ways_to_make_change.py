def number_of_ways_to_make_change(target, coins, memo = {}):
    if target == 0: return 1
    if target < 0: return 0
    
    if (target, len(coins)) in memo: return memo[(target, len(coins))]

    else:
        total = 0
        # import pdb; pdb.set_trace()
        for idx, coin in enumerate(coins):
            if coin > target:
                continue
            else:
                remainder = target - coin
                total += number_of_ways_to_make_change(remainder, coins[idx:], memo)
        memo[(target, len(coins))] = total
        return total




if __name__ == "__main__":
    array = [1, 3]
    print(number_of_ways_to_make_change(4, array))
def min_number_of_coins_for_change(target, coins):
    result = min_number_of_coins_for_change_helper(target, coins, {})
    return result

def min_number_of_coins_for_change_helper(target, coins, memo):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    shortest_combination = None
    for idx, coin in enumerate(coins):
        remainder = target - coin
        remainder_combination = min_number_of_coins_for_change_helper(remainder, coins, memo)
        if remainder_combination is not None:
            remainder_combination.append(coin)
            combination = remainder_combination
            if shortest_combination:
                shortest_combination = min(combination, shortest_combination, key=len)
            else:
                shortest_combination = combination
    
    memo[target] = shortest_combination
    return shortest_combination
            


if __name__ == "__main__":
    print(min_number_of_coins_for_change(8, [2,3,5]))
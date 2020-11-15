def min_num_of_coins(coins, target):
    num_of_coins = [float("inf") if amount != 0 else 0 for amount in range(target+1)]
    for coin in coins:
        for amount in range(target+1):
            if coin <= amount:
                # 0, 1, 2, 3, 4, 5, 6, 7
                num_of_coins[amount] = min(num_of_coins[amount],
                                            num_of_coins[amount-coin] + 1)
    
    return num_of_coins[target] if num_of_coins[target] != float("inf") else -1


if __name__ == "__main__":
    print(min_num_of_coins([1,5,10],7))
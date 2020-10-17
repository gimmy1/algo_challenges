def best_time_to_buy_sell(List):
    # [7,1,5,3,6,4]
    slow = 0
    sell_stock = 0
    while slow < len(List):
        # import pdb; pdb.set_trace()
        fast = slow + 1
        while fast < len(List) and List[fast] > List[fast-1]:

            fast += 1
        
        stock_value = List[fast-1] - List[slow]
        if stock_value > 0:
            sell_stock += stock_value
        
        slow = fast
    return sell_stock

if __name__ == "__main__":
    print(best_time_to_buy_sell([7,1,5,3,6,4]))
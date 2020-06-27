def largest_range(arr):
    range_dict = {a: False for a in arr}
    current_minimum = float("inf")
    current_maximum = float("-inf")
    _range = [0, 0]
    
    for a in arr:
        if range_dict[a] == False:
            subtract = a
            while subtract in range_dict:
                range_dict[subtract] = True
                current_minimum = subtract
                subtract -= 1
            
            addition = a
            while addition in range_dict:
                range_dict[addition] = True
                current_maximum = addition
                addition += 1
            

            _range = max([current_minimum, current_maximum], 
                          _range, key=lambda x: abs(x[0] - x[1]))
            
            print(_range)
    
    return _range
    

if __name__ == "__main__":
    print(largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
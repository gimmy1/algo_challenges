def add_digits(num):
    str_num = str(num)
    if len(str_num) < 2:
        return str_num

    _sum = 0
    for nu in str_num:
        _sum += int(nu)
    
    if len(str(_sum)) == 1:
        return _sum
    else:
        return add_digits(_sum)
    
    return _sum
    
    
    


if __name__ == "__main__":
    print(add_digits(38))
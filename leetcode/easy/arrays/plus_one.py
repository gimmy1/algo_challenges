def plus_one(List):
    result = []
    str_digits = ''.join(str(i) for i in List)
    int_digits = int(str_digits) + 1
    str_digits = str(int_digits)
    for i in str_digits:
        result.append(int(i))
    return result

    
def string_to_integer():
    pass
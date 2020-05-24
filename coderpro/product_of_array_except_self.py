import functools
def product_of_array_with_division(arry):
    product = functools.reduce(lambda a,b: a*b, arry)

    return [product//v for i, v in enumerate(arry)]

def product_of_array_without_division(arry):
    size = len(arry)
    left = [1] * size
    right = [1] * size
    parry = []

    for i in range(size - 1):
        left[i+1] *= arry[i]*left[i]
    
    for i in range(size-1, 0, -1): # step backwards
        right[i-1] *= arry[i] * right[i]
    
    for i in range(size):
        parry.append(left[i] * right[i])
    
    return parry

    
if __name__ == "__main__":
    print(product_of_array_with_division([2,3,4,5,6,7]))
    print(product_of_array_without_division([2,3,4,5,6,7]))
    
def product_sum(arr, product = 1):
    _sum = 0
    for a in arr:
        if isinstance(a, list):
            _sum += product_sum(a, product + 1)
        else:
            _sum += a
    return _sum * product

if __name__ == "__main__":
    # 5 + 2 + 2 * (7-1)+ 3 + 2 * (6 + 3 * (-13 + 8) + 4)
    print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
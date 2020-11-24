def array_of_products(array):
    products = [1] * len(array)
    left_products = [1] * len(array)
    right_products = [1] * len(array)

    left_running = 1
    for idx in range(len(array)):
        left_products[idx] = left_running
        left_running *= array[idx]
    
    right_running = 1
    for idx in reversed(range(len(array))):
        right_products[idx] = right_running
        right_running *= array[idx]
    
    for idx in range(len(array)):
        import pdb; pdb.set_trace()
        products[idx] = left_products[idx] * right_products[idx]
    
    return products

if __name__ == "__main__":
    print(array_of_products([5,1,4,2]))

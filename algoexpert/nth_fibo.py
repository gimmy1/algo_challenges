def fibonacci_iter(num):
    if num == 0 or num == 1: return 0
    previous = 0
    fibo = 1
    i = 1
    while i < num - 1:
        tmp = fibo
        fibo += previous
        previous = tmp
        i += 1
    return fibo

def fibonacci_recur(num):
    if num == 2: return 1
    if num == 1: return 0
    return fibonacci_recur(num - 1) + fibonacci_recur(num - 2)

if __name__ == "__main__":
    print(fibonacci_iter(9))
    print(fibonacci_recur(9))

    



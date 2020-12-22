def fibonnaci_function(n):
    if n <= 2: return 1
    # import pdb; pdb.set_trace()
    return fibonnaci_function(n-1) + fibonnaci_function(n-2)

if __name__ == "__main__":
    print(fibonnaci_function(7))

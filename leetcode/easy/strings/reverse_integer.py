def reverse_integer(V):
    if V == 0 or V > 2 ** 31: return 0
    modify = ""
    pos_neg = V // abs(V)
    V *= pos_neg
    while V >= 10:
        val = V % 10
        V //= 10
        if len(modify) == 0 and val == 0:
            print("Dropping Zero")
        else:
            modify += str(val)
    
    modify += str(V)
    return pos_neg * int(modify)

if __name__ == "__main__":
    # print(reverse_integer(-123))
    # print(reverse_integer(120))
    # print(reverse_integer(0))
    print(reverse_integer(1534236469))
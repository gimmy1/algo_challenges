def balanced_brackets(bracket):
    brackets = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    balance = []
    for bi in bracket:
        # import pdb; pdb.set_trace()
        if bi in brackets and (len(balance) > 0 and brackets[bi] == balance[-1]):
            balance.pop()
        else:
            balance.append(bi)
    
    return len(balance) == 0

if __name__ == "__main__":
    # print(balanced_brackets("([])(){}(())()()"))
    # print(balanced_brackets("()[]{}{"))
    print(balanced_brackets(")[]}"))


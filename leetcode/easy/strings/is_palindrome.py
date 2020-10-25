def is_palindrome(S):
    left, right = 0, len(S) - 1
    while left < right:
        # import pdb; pdb.set_trace()
        try:
            if not S[left].isalnum():
                while not S[left].isalnum():
                    left += 1
            if not S[right].isalnum():
                while not S[right].isalnum():
                    right -= 1
        except:
            return False
        print(S[left], S[right])
        if S[left].lower() != S[right].lower():
            return False
        left += 1
        right -= 1
    
    return True
        
if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: PPanama"))
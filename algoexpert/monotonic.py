def monotonic_array(arr):
    # find if negative or positive
    # -1, -10, -11, -12, -15
    if len(arr) <= 2: return True
    
    i = 0
    direction = 0
    while i < len(arr)-1:
        mono = arr[i] - arr[i+1]
        if mono != 0:
            if arr[i+1] > arr[i]:
                direction = 1
                break
            else:
                direction = -1
                break
        i += 1
        
    if direction == 0: return True
    
    while i < len(arr) - 1:
        if not same_direction(arr[i], arr[i+1], direction):
            return False
        i += 1
    return True

def same_direction(one, two, direction):
    if two > one and direction < 0:
        return False
    elif two < one and direction > 0:
        return False
    return True
    

if __name__ == "__main__":
    print(monotonic_array([5,7,6]))
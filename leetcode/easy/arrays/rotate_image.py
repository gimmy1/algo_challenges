def rotate_array(List):
    """
    Given an array, rotate the array to the right by k steps, where k is non-negative.
    """
    Length = len(List)
    Half = Length // 2
    for layer in range(Half):
        for col in range(layer, Length - layer - 1):
            temp = List[layer][col]
            List[layer][col] = List[Length - col - 1][layer]
            List[Length - col - 1][layer] = matrix[][Length - col - 1]



    return List

            

if __name__ == "__main__":
    print(rotate_array(
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]))
    # print(rotate_array([[7, 8, 9], [4, 5, 6], [1, 2, 3]]))

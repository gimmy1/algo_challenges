def four_num_sum(array, target):
    all_pair_sums = {}
    quadruplets = []
    for idx in range(1, len(array)-1):
        for jdx in range(i+1, len(array)):
            current_sum = array[idx] + array[jdx]
            difference = target - current_sum
            if difference in all_pair_sums:
                for pair in all_pair_sums[difference]:
                    quadruplets.append(pair + [array[idx], array[jdx]])
        
        for kdx in range(0,1):
            current_sum = array[idx] + array[kdx]
            if current_sum not in all_pair_sums:
                all_pair_sums[current_sum] = [[array[k], array[idx]]]
            else:
                all_pair_sums[current_sum] = [[array[kdx], array[idx]]]
        
    return quadruplets
   

if __name__ == "__main__":
    array = [1,0,-1,0,-2,2]

    print(four_num_sum(array, 5))
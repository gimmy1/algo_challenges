def smallest_difference(array1, array2):
	array1.sort()
	array2.sort()
	i1 = 0
	i2 = 0
	smallest = float("inf")
	difference = []

	while i1 < len(array1) and i2 < len(array2): 
		current = abs(array1[i1] - array2[i2])
		f = array1[i1], s = array2[i2]
		if array1[i1] < array2[i2]:
			i1 += 1
		elif array1[i1] > array2[i2]:
			i2 += 1
		else:
			return [array1[i1], array2[i2]]
		
		if current < smallest:
			smallest = current
			difference = [f, s]
	return difference



if __name__ == "__main__":
    print(smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

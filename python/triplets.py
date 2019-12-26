
## Time Complexity O(n^3)
def triplets(arr, sum):
	result = False
	size = len(arr)
	for i in range(size):
		for j in range(i+1, size):
			for k in range(j+1, size):
				if arr[i] + arr[j] + arr[k] == sum:
					print ("Triplets Found are {} {} and {}".format(arr[i], arr[j], arr[k]))
					result = True

	return result


## Time Complexity O(n^2)
def triplets_set(arr, sum):
	result = False
	size = len(arr)
	for i in range(size - 1):	
		tmp_set = set()
		for j in range(i + 1, size):
			tmp_sum = arr[i] + arr[j]
			if (sum - tmp_sum) in tmp_set:
				print ("Set Triplets Found are {} {} and {}".format(arr[i], arr[j], sum - tmp_sum))
				result = True
			tmp_set.add(arr[j])	
	return result		


arr = [0, -1, -2, -3, 3, 4, 5, -7, -9, 2]	
sum = 0
result = triplets(arr, sum)
print result

set_result = triplets_set(arr, sum)
print set_result


--------------------------------Result-------------------------------------------
Triplets Found are 0 -2 and 2
Triplets Found are 0 -3 and 3
Triplets Found are -1 -2 and 3
Triplets Found are -1 -3 and 4
Triplets Found are -2 -3 and 5
Triplets Found are 3 4 and -7
Triplets Found are 4 5 and -9
Triplets Found are 5 -7 and 2
True
Set Triplets Found are 0 3 and -3
Set Triplets Found are 0 2 and -2
Set Triplets Found are -1 3 and -2
Set Triplets Found are -1 4 and -3
Set Triplets Found are -2 5 and -3
Set Triplets Found are 3 -7 and 4
Set Triplets Found are 4 -9 and 5
Set Triplets Found are 5 2 and -7
True
-----------------------------------------------------------------------------------
def triplets(arr,sum):
	size = len(arr)
	for i in range(size):
		for j in range(i+1, size):
			for k in range(j+1, size):
				if arr[i] + arr[j] + arr[k] == sum:
					print ("Triplets Found are {} {} and {}".format(arr[i], arr[j], arr[k]))
					# return True

	return False


def triplets_set(arr, sum):
	size = len(arr)
	
	for i in range(size - 1):	
		tmp_set = set()
		for j in range(i + 1, size):
			tmp_sum = arr[i] + arr[j]
			if (sum - tmp_sum) in tmp_set:
				print ("Set Triplets Found are {} {} and {}".format(arr[i], arr[j], sum - tmp_sum))
				# return True
			tmp_set.add(arr[j])	
	return False		

arr = [0, -1, -2, -3, 3, 4, 5, -7, -9, 2]	
sum = 0
result = triplets(arr, sum)
print result

set_result = triplets_set(arr, sum)
print set_result
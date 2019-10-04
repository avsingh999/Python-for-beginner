/* Contribution by @akshat157 */
def selection_sort(arr):
	
	for i in range(len(arr)-1):
		for j in range(i+1, len(arr)):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]
	
	return arr
	
arr = [10, 100, 2, 50, 75, 256, 49, 8, 25]
selection_sort(arr)
print(arr)

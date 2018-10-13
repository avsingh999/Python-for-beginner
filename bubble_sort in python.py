# Bubble sort in python

# List to sort
L = [5, 3 ,2 ,1 ,6]

def bubble_sort(List):
	COMPLETED = False
	while not COMPLETED:
		COMPLETED = True
		for i in range(len(L) - 1):
			if List[i] > List[i+1]:
				COMPLETED = False
				List[i], List[i+1] = List[i+1], List[i]
	return List

print(bubble_sort(L))
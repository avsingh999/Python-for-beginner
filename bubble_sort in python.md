## Bubble sort in python

### Description

Bubble sort just iterate through the array at least n times (n is the number of the elements of the array to sort) and compares eache pair of asjacent items and swaps them if they are in the wrong order.

__Worst Case Complexity: n^2^__

### Code

```python
# List to sort
L = [5, 3, 2, 1, 6]

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
```
## Heap Sort

### Description

The heapsort algorithm can be divided into two parts.

In the first step, a heap is built out of the data. The heap is often placed in an array with the layout of a complete binary tree. The complete binary tree maps the binary tree structure into the array indices; each array index represents a node; the index of the node's parent, left child branch, or right child branch are simple expressions. For a zero-based array, the root node is stored at index 0; if *i* is the index of the current node, then

```python
iParent(i) = floor((i-1) / 2) # where floor functions map a real number to the smallest leading integer.
iLeftChild(i) = 2*i + 1
iRightChild(i) = 2*i + 2
```

In the second step, a sorted array is created by repeatedly removing the largest element from the heap (the root of the heap), and inserting it into the array. The heap is updated after each removal to maintain the heap property. Once all objects have been removed from the heap, the result is a sorted array.

Heapsort can be performed in place. The array can be split into two parts, the sorted array and the heap. The storage of heaps as arrays is diagrammed here. The heap's invariant is preserved after each extraction, so the only cost is that of extraction.

__Worst Case Complexity: n * log(n)__

### Code
```python
def heapify(arr, n, i):
	# Find largest among root and children
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2 
	
	if l < n and arr[i] < arr[l]:
		largest = l
	
	if r < n and arr[largest] < arr[r]:
		largest = r
	
	# If root is not largest, swap with largest and continue heapifying
	if largest != i:
		arr[i], arr[largest] = arr[largest],arr[i]
		heapify(arr, n, largest)
	
def heapSort(arr):
	n = len(arr)
	
	# Build max heap
	for i in range(n, 0, -1):
		heapify(arr, n, i)
	
	
	for i in range(n-1, 0, -1):
		# swap
		arr[i], arr[0] = arr[0], arr[i]  
		
		#heapify root element
		heapify(arr, i, 0)
	 

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
	print ("%d" %arr[i])
```

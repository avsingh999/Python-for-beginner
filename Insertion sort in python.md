# Insertion Sort

## Description
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.

__Worst Case Complexity: n^2^__

## Code

	def insertionSort(alist):
	   for index in range(1,len(alist)):

	     currentvalue = alist[index]
	     position = index

	     while position>0 and alist[position-1]>currentvalue:
	         alist[position]=alist[position-1]
	         position = position-1

	     alist[position]=currentvalue

	alist = [54,26,93,17,77,31,44,55,20]
	insertionSort(alist)
	print(alist)
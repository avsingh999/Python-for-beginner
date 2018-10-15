{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # QuickSort algorithm\
\
## Description:\
\
Going to sort a list of 9 integers in the format [17,41,5,22,54,6,29,3,13] in Python\
\
1. Find the Pivot. Pivot is the item that we used for comparing every number two, so we are going to compare each number in turn to the pivot. Smaller numbers value will be on the left of the pivot and larger numbers value will be on the right of the pivot. We will use the median of three to find the pivot. I choose the first value (17), the middle value (54), and the last value (13). So, 17 is the median of these three values. \
2. Move the pivot value into the first position (0th position)\
3. Start doing the comparisons. We will have a border value (41).  We will swap the current number value with the border value every time in case it is smaller than the border. Therefore, every numbers that are smaller than the pivot will be on the left of the border, and numbers are larger than pivot will be on the right of border.\
4. Swap the 17 into where the border value (13) was. Therefore, the pivot number is in the middle now.\
5. Do the quick sort for numbers that are smaller than pivot as the above instruction.\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 6. Do the quick sort for numbers that are larger than pivot as the above instruction.\
\
## Summary:\
. QuickSort is recursive (method that calls itself)\
. Divide-and-Conquer algorithm\
. Very efficient for large data sets\
. Average case is O(n log n)\
. Performance depends largely on Pivot selection.\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 ## Code:\
\
// list user input (D) and then call the recursive quick-sort2\
def quick_sort(D) :\
	quick_sort2(D, 0, len(D) - 1)\
\
// recursive function\
def quick_sort2 (D, low, high):\
	if low < high:    //more than one item to be sorted\
		p = partition(D, low, high)     // return the pivot around which where we partitioned the list\
		quick_sort2(D, low, p - 1)     // sort left partition\
		quick_sort2(D, p + 1, high)   // sort right partition\
\
// getting the pivot\
def get_pivot(D, low, high):\
	mid = (high + low) / / 2\
	pivot = high\
	if D[low] < D[mid]:\
		if D[mid] < D[high]:\
			pivot = mid\
	elif D[low] < D[high]:\
		pivot = low\
	return pivot\
\
// partition function\
def partition(D, low, high):\
	pivotIndex = get_pivot(D, low, high)\
	pivotValue = D[pivotIndex]\
	D[pivotIndex], D[low] = D[low], D[pivotIndex]   //swap the pivot value into the leftmost position of our list\
	border = low                                                     // set border to the lowest item \
\
	for i in range(low, high + 1):\
		if D[ i ]  <  pivotValue:\
		border += 1\
		D[ i ], D[border] = D[border], D[ i ]\
	D[low], D[border] = D[border], D[low]\
\
	return (border)                                                  // return the index for the pivot\
\
\
\
}
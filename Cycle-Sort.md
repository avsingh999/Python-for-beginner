### Cycle Sort!

Cycle sort is an **in-place sorting** Algorithm, **unstable sorting** algorithm, a comparison sort that is theoretically optimal in terms of the total number of writes to the original array.

 - It is based on the idea that array to be sorted can be divided into
   cycles. Cycles can be visualized as a graph. We have n nodes and an
   edge directed from node i to node j if the element at i-th index must
   be present at j-th index in the sorted array.

#### Example

    arr[] = {10, 5,  2,  3}
    index =  0   1   2   3
    cycle_start = 0 
    **item** = 10 = arr[0]
    
Find position where we put the item  
   

     pos = cycle_start
        while (arr[i] < item)  
            pos++;
        
We put 10 at arr[3] and change item to 
old value of arr[3].

    arr[] = {10, 5, 2, **_10_**} 
    **item** = 3 
    
Again rotate rest cycle that start with **index '0'** 
Find position where we put the item = 3 
we swap item with element at arr[1] now 
    
    arr[] = {10, **_3_**, 2, **_10_**} 
    **item** = 5

Again rotate rest cycle that start with index '0' and item = 5 
we swap item with element at arr[2].
    
    arr[] = {10, **_3_**, **_5_**, **_10_** } 
    **item** = 2
    
Again rotate rest cycle that start with index '0' and item = 2
    
    arr[] = {**_2_**, **_3_**, ** _5_**, **_10_**}  
    
Above is one iteration for cycle_stat = 0.
Repeat above steps for cycle_start = 1, 2, ..n-2

### Code


    def cycleSort(array): 
    writes = 0
    	
    
    for cycleStart in range(0, len(array) - 1): 
    	item = array[cycleStart] 
    	
    	# Find where to put the item. 
    	pos = cycleStart 
    	for i in range(cycleStart + 1, len(array)): 
    	if array[i] < item: 
    		pos += 1
    	
    	# If the item is already there, this is not a cycle. 
    	if pos == cycleStart: 
    	continue
    	
    	# Otherwise, put the item there or right after any duplicates. 
    	while item == array[pos]: 
    	pos += 1
    	array[pos], item = item, array[pos] 
    	writes += 1
    	
    	# Rotate the rest of the cycle. 
    	while pos != cycleStart: 
    		
    	# Find where to put the item. 
    	pos = cycleStart 
    	for i in range(cycleStart + 1, len(array)): 
    		if array[i] < item: 
    		pos += 1
    		
    	# Put the item there or right after any duplicates. 
    	while item == array[pos]: 
    		pos += 1
    	array[pos], item = item, array[pos] 
    	writes += 1
    	
    return writes 
    	
    # driver code 
    arr = [1, 8, 3, 9, 10, 10, 2, 4 ] 
    n = len(arr) 
    cycleSort(arr) 
    
    print("After sort : ") 
    for i in range(0, n) : 
    	print(arr[i], end = ' ') 

#### References

 1. https://en.wikipedia.org/wiki/Cycle_sort
 2.  https://www.geeksforgeeks.org/cycle-sort/


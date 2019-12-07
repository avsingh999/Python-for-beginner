'''HeapSort'''

def Heapify(arr, n, i): 
    large = i # Initialize largest as root 
    l = 2 * i + 1     # left node
    r = 2 * i + 2     # right node
  
    if l < n and arr[i] < arr[l]: 
        large = l

    if r < n and arr[large] < arr[r]: 
        large = r 

    if large!= i: 
        arr[i],arr[large] = arr[large],arr[i]  #swap 
  
        # Heapify the root. 
        Heapify(arr, n, large) 
  
def HeapSort(arr): 
    n = len(arr) 
  
    # Building a maxheap. 
    for i in range(n, -1, -1): #(n//2) will be the last leaf node
        Heapify(arr, n, i) 
  
    # Extracting the min element one by one 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        Heapify(arr, i, 0) 
  
#Taking some random Array 
arr = [ 1, 2, 13, 5,3,4,6,8,1,1, 6,2,4,0, 7] 
HeapSort(arr)
print(*arr)


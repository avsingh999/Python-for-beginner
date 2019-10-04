#define your array to be sorted
arr = [10,80,30,19,8,12,17]

#printing your original array
print("Original array:",arr)

#bubble sorting algorithm
for i in range(len(arr)-1):
    for j in range(len(arr)-1-j):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp 

#printing sorted array
print("Sorted array:",arr)

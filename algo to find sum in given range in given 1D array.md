# Algorithm to find sum in given range in given 1D array
1. Store an array of integers to a variable called, arr
1. Input the range upto which you want to perform the sum
1. Initialize a new variable called index to 0
1. Make a variable called sum and assign it 0
1. Check if variable index is < specified range, if it is true go to step 6 or go to step 9
1. assign the addition of variable sum with the index<sup>th</sup> index of array to the variable sum
1. increment the index by 1
1. go to step 5
1. print the value of sum

# Code:
arr = [1,2,3,4,5] <br>
range = 3 <br>
index = 0 <br>
sum = 0 <br>
while(index < range): <br>
  &nbsp;&nbsp;&nbsp;&nbsp;sum = sum + arr[index] <br>
  &nbsp;&nbsp;&nbsp;&nbsp;index = index + 1 <br>
print(sum) 

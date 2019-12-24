### Algorithm to find sum in given range in given 1D array

1. Store an array of integers to a variable called, arr
2. Input the range upto which you want to perform the sum
3. Initialize a new variable called index to 0
4. Make a variable called sum and assign it 0
5. Check if variable index is < specified range, if it is true go to step 6 or go to step 9
6. Assign the addition of variable sum with the index<sup>th</sup> index of array to the variable sum
7. Increment the index by 1
8. Go to step 5
9. Print the value of sum

### Code:

```python
arr = [1, 2, 3, 4, 5]
range = 3
index = 0
sum = 0

while(index < range):
  sum = sum + arr[index]
  index = index + 1

print(sum) 
```

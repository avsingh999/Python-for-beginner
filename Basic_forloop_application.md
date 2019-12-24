### Prints out the numbers `0, 1, 2, 3, 4`

```python
for x in range(5):
   print(x)
```

### Prints out `3, 4, 5`

```python
for x in range(3, 6):
    print(x)
```

### Prints out `3, 5, 7`

```python
for x in range(3, 8, 2):
    print(x)
```
    
### example

- Program to find the sum of all numbers stored in a list

- List of numbers

```python
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
```
- variable to store the sum

```python
sum = 0
```

- iterate over the list

```python
for val in numbers:
   sum = sum+val
```
- Output: The sum is `48`

```python
print("The sum is", sum)
```

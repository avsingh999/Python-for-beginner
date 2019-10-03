# How to print random number in a range python


For this we use the inbuilt `random` module to generate random numbers.
From the `random` module we import the method `randint` that generates a random integer value.

# `randint()` Parameters

The `randint()` method takes a two argument:

**a** & **b**.


The syntax for `randint()` is
```python
randint(a, b)
```

# Return value from `randint()`

Returns a random integer N such that a <= N <= b.

# Example

```python
# importing the `randint` method from `random` module
from random import randint

# generate a random integer 
num = randint(1, 100)

# print the randomly generated number
print('The randomly generated number i is:', num)

# since the value will change on each execution, my randomly generated number will obviously be different than your output
```

The output of this code for me was:

```bash
The randomly generated number is: 6
```

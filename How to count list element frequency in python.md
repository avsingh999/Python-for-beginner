# How to count list element frequency in python
In simple terms, `count()` method counts how many times an element has occurred in a list and returns it.

# `count()` Parameters
The `count()` method takes a single argument:

* **element** - element whose count is to be found.

# Return value from `count()`
The `count()` method returns the number of occurrences of an element in a list.

# Example

```python
def countX(lst, x):
    count = 0
    for element in lst:
        if (element == x):
            count = count + 1
    return count
 
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))
```

When you run the program, the output will be:

```bash
8 has occurred 5 times
```

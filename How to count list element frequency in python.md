# How to count list element frequency in python

In simple terms, `count()` method counts how many times an element has occurred in a list and returns it.

The syntax of `count()` method is:

```python
list.count(element)
```

# `count()` Parameters

The `count()` method takes a single argument:

* **element** - element whose count is to be found.

# Return value from `count()`

The `count()` method returns the number of occurrences of an element in a list.

# Example

```python
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)
```

When you run the program, the output will be:

```bash
The count of i is: 2
The count of p is: 0
```
# Find index of element in python list

In simple terms, `index()` method finds the given element in a list and returns its position.

However, if the same element is present more than once, `index()` method returns its smallest/first position.

**Note**: Index in Python starts from `0` not `1`.

The syntax of `index()` method for list is:

```python
list.index(element)
```

# `index()` Parameters

The index method takes a single argument:
* **element** - element that is to be searched.

# Return value from `index()`

The `index()` method returns the index of the element in the list.

If not found, it raises a ValueError exception indicating the element is not in the list.

# Example

```python
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# element 'e' is searched
index = vowels.index('e')

# index of 'e' is printed
print('The index of e:', index)

# element 'i' is searched
index = vowels.index('i')

# only the first index of the element is printed
print('The index of i:', index)
```

When you run the program, the output will be:

```bash
The index of e: 1
The index of i: 2
```
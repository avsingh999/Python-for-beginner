### How to clone list in python

A list can be copied with = operator. For example:

```python
old_list = [1, 2, 3]
new_list = old_list
```

The problem with copying the list in this way is that if you modify the new_list, the old_list is also modified.

### Example

```python
old_list = [1, 2, 3]
new_list = old_list

# add element to list
new_list.append('a')

print('New List:', new_list )
print('Old List:', old_list )
```

When you run the program, the output will be:

```bash
Old List: [1, 2, 3, 'a']
New List: [1, 2, 3, 'a']
```

However, if you need the original list unchanged when the new list is modified, you can use copy() method. This is called shallow copy.

The syntax of copy() method is:

```python
new_list = list.copy()
```

### Example

```python
# mixed list
list = ['cat', 0, 6.7]

# copying a list
new_list = list.copy()

# Adding element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List: ', list)
print('New List: ', new_list)
```

When you run the program, the output will be:

```python
Old List: ['cat', 0, 6.7]
New List: ['cat', 0, 6.7, 'dog']
```
# How to add two lists in python?

List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.

Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ].

```python
>>> a = [1, 2.2, 'python']
```

we can add two lists together in python using the following method

# Example

```python
a = [1, 2.2, 'python']
b = [1, 2.3, 'example']

#print list together
#output: [1, 2.2, 'python', 1, 2.3, 'example']
a + b
```
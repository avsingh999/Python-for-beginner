# How to join in python

A list can be joined using together as a string using the stynax:

```python
a_list = [1,2,3]
a_string = " ".join(a_list)
print("A string:", a_string)
```

Which will output:

```sh
A string: 1 2 3
```

Looking at how *split* works in Python, `a_string.split(delimiter)`, 
and how *join* works in other languages like JavaScript it's easy to confuse it as working in Python as `list.join(delimiter)`.
A way to help rationalize this syntax is to not think of *join* as transforming a list into a string, 
but rather as a function that places the delimiter string in-between elements of a list.

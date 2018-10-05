# String example in python?

String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes, ''' or """.

```python
>>> s = "This is a string"
>>> s = '''a multiline
```

Like list and tuple, slicing operator [] can be used with string. Strings are immutable.

# Example

```python
s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
s[5] ='d'
```
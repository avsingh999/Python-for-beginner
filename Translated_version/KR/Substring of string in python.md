# Substring of string in Python 

We can get substring from string (slicing) by following different ways: 

1. Specifying start and end index. a[startIndex: endIndex]
2. Specifying just end index. a[:endIndex]
3. Specifying just start index. a[startIndex:]

Specifying negative index will be equivalent to that index starting from end of the string. 

## Example

```python
myVar = "Hello World"
hello = myVar[0:5]
world = myVar[6:11]
sub1 = myVar[2:]
sub2 = myVar[:-3]
```

The output will be as follows: 

```sh
Hello
World
llo World
Hello Wo
```

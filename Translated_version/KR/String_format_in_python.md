# String format in python

### In Python 3 everything is object and a string is of type str
```
s = ''
type(s)
```

### We can acess a string in your index
```
"python"[0] # 'p'
"python"[1] # 'y'
"python"[2] # 't'
"python"[3] # 'h'
"python"[4] # 'o'
"python"[5] # 'n'
```

### But we cannot change its value by assigning a value through the index.
```
word = "foo"
word[1] = "r"
# TypeError: 'str' object does not support item assignment
```
### String é um objeto iterável.

```
for letter in "python":
    print letter

>>
"""
p
y
t
h
o
n
"""
```

### Searching the string
```
"b" in "abc"     # True
"d" in "abc"     # False
"d" not in "abc" # True
"b" not in "abc" # False
```
### Common String Methods

`Len()` method
Show string length

```
s = "foo"
len(s)
# 3
```

### upper and lowe
`Upper()` method
Caps Lock.

```"foo".upper() # FOO```


`lower()` method
Lowercase.

```"FOO".lower() # foo```

### Convert to strin
`str()` method
Converts to string

```
num = 123
type(num)      # <class 'int'>
type(str(num)) # <class 'str'>
```

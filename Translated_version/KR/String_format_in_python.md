# 파이썬의 문자열 형식

### 파이썬 3에서는 모든 것이 객체이고 문자열은 str 유형입니다.
```
s = ''
type(s)
```

### index의 문자열에 접근 할 수 있습니다
```
"python"[0] # 'p'
"python"[1] # 'y'
"python"[2] # 't'
"python"[3] # 'h'
"python"[4] # 'o'
"python"[5] # 'n'
```

### 그러나 index를 통해 값을 할당하여 값을 변경할 수는 없습니다.
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

### 문자열 검색
```
"b" in "abc"     # True
"d" in "abc"     # False
"d" not in "abc" # True
"b" not in "abc" # False
```
### 일반적인 문자열 메소드

`Len()` method
Show string length

```
s = "foo"
len(s)
# 3
```

### upper와 lower
`Upper()` method
Caps Lock.

```"foo".upper() # FOO```


`lower()` method
Lowercase.

```"FOO".lower() # foo```

### 문자열로 변환
`str()` method
Converts to string

```
num = 123
type(num)      # <class 'int'>
type(str(num)) # <class 'str'>
```

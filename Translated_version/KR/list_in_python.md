## 파이썬 Lists

List은 주문 및 변경 가능한 모음입니다. 중복 멤버를 허용합니다.

파이썬에서 list는 대괄호로 작성됩니다.

```python
L = ["git", "github", "version_control"]
print(L)
L = [1, "github", 3.4]
print(L)
```
#### 접근항목

index번호를 사용하여 항목에 접근할 수 있습니다.

```python
L = ["git", "github", "version_control"]
print(L[1])
```
#### 항목값 바꾸기

index번호를 참조하여 값을 변경할 수 있습니다.

```python
L = ["git", "github", "version_control"]
L[1] = 123
print(L)
```
#### list 탐색

```python
L = ["git", "github", "version_control"]
for item in L:
  print (item)
```

#### 항목이 존재하는지 확인

```python
L = ["git", "github", "version_control"]
if "git" in L:
  print('Yes it exists!')
```

#### List 크기

```python
L = ["git", "github", "version_control"]
length = len(L)
print(length)
```

#### list에 항목 추가하기

```python
L = ["git", "github", "version_control"]
L.append("hey")
print(L)
```

```python
L = ["git", "github", "version_control"]
L.insert(1, "hey");
print(L)
```

#### list에서 항목 제거하기

remove (), 이것은 지정된 항목을 제거합니다

```python
L = ["git", "github", "version_control"]
L.remove("git")
print(L)
```

pop (), 이것은 지정된 index 제거합니다 (또는 index가 지정되지 않은 경우엔 마지막 항목).

```python
L = ["git", "github", "version_control"]
L.pop()
print(L)
```

del, 이것은 지정된 index을 제거합니다

```python
L = ["git", "github", "version_control"]
del L[1]
print(L)
```

del, 또한 이것은 list전체를 삭제할 수도 있습니다

```python
L = ["git", "github", "version_control"]
del L
print(L)     #this will cause an error because "L" no longer exists.
```

clear(), 이것은 list를 비우는 메소드입니다. 

```python
L = ["git", "github", "version_control"]
L.clear()
print(L)
```

#### List() contructor

L = list(("git", "github", "digital")) # 이중 대괄호에 유의
print(L)

| Command | Description |
| --- | --- |
| append() | Adds an element at the end of the list |
| clear() | Removes all the elements from the list |
| copy() | Returns a copy of the list |
| count() | Returns the number of elements with the specified value |
| extend() | Add the elements of a list (or any iterable), to the end of the current list |
| index() | Returns the index of the first element with the specified value |
| insert() | Adds an element at the specified position |
| pop() | Removes the element at the specified position |
| remove() | Removes the item with the specified value |
| reverse() | Reverse the order of list |
| sort() | Sort the list |

## 예시 1

```python
a = [5,10,15,20,25,30,35,40]

print("a[2] = ", a[2])

print("a[0:3] = ", a[0:3])

print("a[5:] = ", a[5:])
```

## 예시 2

```python
t = (5,'program', 1+3j)

print("t[1] = ", t[1])


print("t[0:3] = ", t[0:3])
```

## 예시 3

```python
a = {5,2,3,1,4}

# 설정된 변수 출력
print("a = ", a)

# a의 데이터타입
print(type(a))
```

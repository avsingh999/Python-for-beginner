## Python Lists

List is a collection which is ordered and changeable. Allows duplicate members.

In python lists are written in square brackets.

```python
L = ["git", "github", "version_control"]
print(L)
L = [1, "github", 3.4]
print(L)
```
#### Access Items

you can access the item using index number.

```python
L = ["git", "github", "version_control"]
print(L[1])
```
#### Change Item value

you can change value by refering to index number.

```python
L = ["git", "github", "version_control"]
L[1] = 123
print(L)
```
#### Traverse the list

```python
L = ["git", "github", "version_control"]
for item in L:
  print (item)
```

#### Check if Item exists

```python
L = ["git", "github", "version_control"]
if "git" in L:
  print('Yes it exists!')
```

#### List size

```python
L = ["git", "github", "version_control"]
length = len(L)
print(length)
```

#### Adding items to list

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

#### Remove items from list

remove(), it removes the specified item

```python
L = ["git", "github", "version_control"]
L.remove("git")
print(L)
```

pop(), removes the specified index, (or the last item if index is not specified)

```python
L = ["git", "github", "version_control"]
L.pop()
print(L)
```

del, removes the specified index

```python
L = ["git", "github", "version_control"]
del L[1]
print(L)
```

del, can also delete the entire list

```python
L = ["git", "github", "version_control"]
del L
print(L)     #this will cause an error because "L" no longer exists.
```

clear(), method empties the list

```python
L = ["git", "github", "version_control"]
L.clear()
print(L)
```

#### List() contructor

L = list(("git", "github", "digital")) # note the double round-brackets
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

## Example 1

```python
a = [5,10,15,20,25,30,35,40]

print("a[2] = ", a[2])

print("a[0:3] = ", a[0:3])

print("a[5:] = ", a[5:])
```

## Example 2

```python
t = (5,'program', 1+3j)

print("t[1] = ", t[1])


print("t[0:3] = ", t[0:3])
```

## Example 3

```python
a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))
```

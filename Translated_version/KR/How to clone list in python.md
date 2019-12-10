# 파이썬에서 list를 복제하는법.

list는 = 연산자로 복사될 수 있습니다. 예를 들면:

```python
old_list = [1, 2, 3]
new_list = old_list
```

이 방법에서 list를 복사하는거에 문제는 만약 당신이 new_list를 수정하는 경우, old_list또한 수정된다는 것입니다.

# 예시

```python
old_list = [1, 2, 3]
new_list = old_list

# list에 요소 추가
new_list.append('a')

print('New List:', new_list )
print('Old List:', old_list )
```

당신이 프로그램을 돌릴 때, 출력은 아래와 같을 것입니다:

```bash
Old List: [1, 2, 3, 'a']
New List: [1, 2, 3, 'a']
```

그러나, 만약 당신이 원래 list를 변경하지 않고 새 list를 수정할 하는게 필요할 떄, copy()메소드를 사용할 수 있습니다. 이건 얕은 복사라고 불립니다.

copy()메소드의 문법은 아래와 같습니다:

```python
new_list = list.copy()
```

# 예시

```python
# 섞인 list
list = ['cat', 0, 6.7]

# list 복사하기
new_list = list.copy()

# 새로운 list에 요소 추가하기
new_list.append('dog')

# 새로운 list와 옛 list 출력하기
print('Old List: ', list)
print('New List: ', new_list)
```

당신이 프로그램을 돌릴 때, 출력은 아래와 같을 것입니다:

```python
Old List: ['cat', 0, 6.7]
New List: ['cat', 0, 6.7, 'dog']
```
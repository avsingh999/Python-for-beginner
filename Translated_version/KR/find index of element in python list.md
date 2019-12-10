# 파이썬 list에서 index의 요소 찾기.

간단히 말해서, `index()` 메소드는 주어진 요소를 list에서 찾아 그 위치를 반환한다.

그러나, 같은 요소가 두번 이상 존재하면, `index()` 메소드는 가장 작은/첫번째 위치를 반환한다.

**메모**: 파이썬에서 index는 `1` 이 아니라  `0` 부터 시작한다.

list에 대한 `index()` 메소드의 문법은 다음과 같다:

```python
list.index(element)
```

# `index()` 매개변수

index 메소드는 하나의 인자만을 받는다:
* **element** - 검색할 요소.

# `index()` 의 반환값

 `index()` 메소드는 list안의 요소의 index를 반환한다.

찾을 수 없으면, 요소가 list안에 없음을 나타내는 ValueError을 일으킨다.

# 예시

```python
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# 요소 'e' 가 검색됨
index = vowels.index('e')

#  'e' 의 index가 출력됨
print('e의 index:', index)

#  'i' 의 요소가 검색됨
index = vowels.index('i')

# 요소의 첫번쨰 index만 출력됨
print('i의 index:', index)
```

당신이 프로그램을 돌린다면, 출력은 아마 아래와 같을것이다:

```bash
The index of e: 1
The index of i: 2
```
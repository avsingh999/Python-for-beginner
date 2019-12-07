# 파이썬에서 Dictionary란 무엇인가?

파이썬 Dictionary는 정렬되지 않은 항목들의 모임입니다. 키:값 쌍을 가지고있죠.
Dictionary는 파이썬판 해쉬테이블입니다. 키를 알고있을 때 값을 검색할때 매우 효율적이죠.

## dictionary만들기.

```python
dictionary = {} #빈 dictionary.
dictionary = {1: 'Hello', 2: 'World'}
dictionary = {'language' : 'python', 'versions' : [2, 3]}
dictionary = dict([(1,'apple'), (2,'ball')])
```

## How to access a dictionary element.

```python
my_var = {'Language': 'Python', 'version': '3.6.6'}
print(my_var['Language']) #결과: Python

print(my_var.get('version')) #결과: '3.6.6'
```

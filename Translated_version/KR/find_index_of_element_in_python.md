# 파이썬에서 어떻게 요소의 index를 찾는가?

 `index()` 메소드를 사용하여 요소의 index를 찾을 수 있습니다. 이 메소드는 list에서 요소의 첫 번째 발생을 반환합니다. 존재하지 않으면 에러를 반환합니다.

## 예시 1

```python
my_list = ['foo', 'bar', 'nothing', 'something', 'foo']
my_list.index('bar')
```

- 출력:

```sh
1
```

## 예시 2

```python
my_list = ['foo', 'bar', 'nothing', 'something', 'foo']
my_list.index('foo')
```

- 출력:

```sh
0
```

## 예시 3

```python
my_list = ['foo', 'bar', 'nothing', 'something', 'foo']
my_list.index('thing')
```

- 출력:

```sh
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'thing' is not in list
```

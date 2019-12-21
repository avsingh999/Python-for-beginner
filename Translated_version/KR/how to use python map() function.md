## 파이썬 map() 함수

##### map() 함수는 주어진 iterable (목록, 튜플 등)의 각 항목에 주어진 함수를 적용한 후 결과 list를 반환합니다.


#### 문법

```python
map(fun, iter)
```

#### 매개변수들 :

```
fun : 주어진 iterable의 각 요소를 map이 전달하는 함수입니다.
iter : 맵핑될 iterable입니다.
```


## 예시

튜플에서 각 단어의 길이를 계산하십시오:
 
```python
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(list(x))
```

#### 출력

[5, 6, 6]
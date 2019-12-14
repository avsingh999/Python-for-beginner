# while 반복문

while 반복문을 사용하면 조건이 true인 동안에 일련의 명령문을 실행할 수 있습니다.

`6`보다 작은 `i`를 출력

```python
i = 1
while i < 6:
    print(i)
    i += 1
```
> 참고 : `i`를 증가시켜야합니다. 그렇지 않으면 반복문 영원히 계속됩니다.
### break문

break문을 사용하면 while 조건이 true인 경우에도 루프를 중지할 수 있습니다:

 `i` 가 `3` 이면 루프를 종료합니다.

```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```
### continue문

continue문을 사용하면 현재의 반복을 중지하고 다음에 오는 것을 계속할 수 있습니다.


 `i` 가 `3` 일 때 다음의 것을 계속 반복합니다

```python
i = 0
while i < 6:
    i += 1 
    if i == 3:
        continue
    print(i)
```

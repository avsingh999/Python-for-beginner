### Lambda 함수 란 무엇입니까?

파이썬에서 Anonymous function는 이름없이 정의된 함수입니다.
이러한 Anonymous function를 람다함수라고합니다.

## 파이썬에서 람다함수의 문법

```
lambda arguments: expression
```

## 예시:

```python
# 숫자를 세제곱하기
cube = lambda x: x**3

print(cube(10)) #output: 1000

# list에있는 모든 숫자의 제곱을 출력합니다.

my_list = [1, 2, 3, 4]

square = lambda x: x**2

print(list(map(square, my_list))) # output: [1, 4, 9, 16]
```

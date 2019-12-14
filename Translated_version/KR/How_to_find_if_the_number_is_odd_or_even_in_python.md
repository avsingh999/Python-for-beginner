# 파이썬에서 숫자가 홀수인지 또는 짝수인지 찾는 방법

`%` (mod)는 두 숫자 사이의 나머지 나누기를 얻으므로 x가 짝수이면 x가 2인 나머지는 0입니다.
```
number = 2

if number%2 == 0:
    print(number,"짝수입니다.")
else:
    print(number, "홀수입니다.")
```

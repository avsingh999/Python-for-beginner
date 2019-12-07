숫자는 2로 나눌수 있다고 해도, 모듈로 `%` 연산을 사용해서 같은지 확인합니다.
<br>
``` python
num = int(input("숫자를 입력하세요"))
if num % 2 == 0:
    print("짝")
else:
    print("홀")
```

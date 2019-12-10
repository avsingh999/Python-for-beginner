# 파이썬에서의 예외처리

## 예외처리란 무엇인가요?
예외 처리는 컴퓨터 프로그램이 실행될 때 예외에 응답하는 프로세스입니다. 특수 처리가 필요한 예기치 못한 이벤트가 일어나면 예외가 발생합니다.

## 파이썬 예외처리:

 `try` 블록은 코드 블록의 에러들을 테스트할 수 있게 해준다.

 `except` 블록은 오류를 처리할 수 있게 해준다.

 `finally` 블록은 try 및 except 블록들의 결과에 상관없이 코드를 실행 할 수 있게 해준다.

## 사용법:
```
try:
  print(x)
except:
  print("예외가 발생되었습니다.")
```

## 예시

예외처리 없을시
```
>>> print( 0 / 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
```

예외처리 후
```
try:
  print( 0 / 0)
except ZeroDivisionError:
  print ("분모는 0이 될 수 없습니다..")
finally:
  print ("예외를 잘 처리하셨습니다.")
```

위 코드의 결과
```
분모는 0이 될 수 없습니다.
예외를 잘 처리하셨습니다.
```

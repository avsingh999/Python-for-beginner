## 파이썬 print()

```python
print("Python")
```

## print()의 문법 전체는 다음과 같습니다:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

```  
## print()매개변수
##objects - 인쇄 대상. *둘 이상의 객체가있을 수 있음을 나타냅니다.
##sep - 객체는 sep로 구분됩니다. 기본값: ' '
##end - end는 마지막에 인쇄됩니다
##file - write (string) 메소드가있는 객체여야합니다. 생략하면 sys.stdout이 사용되어 화면에 객체를 인쇄합니다.
##flush - 참이면 스트림이 강제로 flushed됩니다. 기본값 : False
```

## 파이썬에서 변수가 있는 print()
여러 가지 방법이 있습니다. 그들 중 하나는 f-string을 사용하고 있습니다.
```python
last_name = "홍"
first_name = "길동"
print(f"안녕. 내 이름은 {first_name} {last_name}이야.")
```

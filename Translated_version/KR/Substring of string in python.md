# 파이썬에서 문자열의 부분 문자열

다른방법으로 문자열(슬라이싱)에서 부분 문자열을 얻을 수 있습니다.

1. 시작 및 종료 index 지정. a[startIndex : endIndex]
2. 종료 index 지정. a[:endIndex]
3. 시작 index만 지정. a[startIndex :]

음수index를 지정하는 것은 문자열 끝에서 시작하는 index시작과 같습니다.

## 예

```python
myVar = "Hello World"
hello = myVar[0:5]
world = myVar[6:11]
sub1 = myVar[2:]
sub2 = myVar[:-3]
```

출력은 다음과 같을것입니다:

```sh
Hello
World
llo World
Hello Wo
```

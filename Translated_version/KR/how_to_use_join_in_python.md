#파이썬에서 join을 사용하는 방법

파이썬에서 join하는 형식은 다음과 같다.
``string.join(sequence,[,sep])``

여기서 sep은 문자열 요소의 list나 tuple이 될 시퀀스의 요소를 연결하는데 사용되는 문자열 구분기호입니다.

다음 함수는 시퀀스 및 구분 기호를 가져 와서 **join** 메서드를 사용하여 연결하는 함수의 예를 보여줍니다.

```python
def joinSequenceSequence(sequence,sep):

    print(sep.join(sequence))
```

## 결과물

다음과 같이 메소드를 호출하면 결과 **1-2-3-4-5** 가 나타납니다

```python
joinSequenceSequence(["1","2","3","4","5"],"-")
```

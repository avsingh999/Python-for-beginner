# 파이썬에 참여하는 법

다음 문법을 사용하여 문자열로 함께 list를 결합할 수 있습니다:

```python
a_list = [1,2,3]
a_string = " ".join(a_list)
print("A string:", a_string)
```

출력은 다음과 같을것입니다:

```sh
A string: 1 2 3
```

파이썬에서 *split* 작동 방식을 살펴보면`a_string.split (delimiter)`,
JavaScript와 같은 다른 언어에서 *join* 이 작동하는 방식은 파이썬에서`list.join (delimiter)`처럼 작동하는 것과 혼동하기 쉽습니다.
이 구문을 합리화하는 데 도움이되는 방법은 *join* 을 문자열을 list에 넣는것으로 생각하지 않는것입니다.
오히려 목록의 요소사이에 구분문자 문자열을 배치하는 함수로 사용하십시오.

# 파이썬에서 list 요소의 빈도를 세는 법

간단히 말해서, `count()` 메소드는 요소가 list에서 몇번이나 발생했는지 세어서 반환합니다.

 `count()` 메소드의 문법은 다음과 같다:

```python
list.count(element)
```

# `count()` 매개변수들

 `count()` 메소드는 하나의 인자를 가진다:

* **element** - count를 찾는 요소

#  `count()` 에서의 반환값

 `count()` 메소드는 list에서 요소의 발생 횟수를 반환합니다.

# 예시

```python
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# 요소 'i' 세기
count = vowels.count('i')

# 횟수 출력
print('i의 횟수는 다음과 같다:', count)
```

당신이 프로그램을 돌릴 때, 결과는 아래과 같을 것입니다:

```bash
i의 횟수는 다음과 같다: 2
p의 횟수는 다음과 같다: 0
```
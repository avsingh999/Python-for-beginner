# 파이썬 정규식

#### 정규식은 문자열에서 패턴 일치에 사용됩니다. 특정 형식을 준수하는 유효한 전화 번호, 전자 메일 주소를 찾기 위해 패턴을 일치시키는 일반적인 방법을 제공합니다. 일반적인 검색 기능을 사용하는 것은 지루한 작업입니다. 정규식은 유한 오토마타를 사용하여 내부적으로 구현됩니다.


### re.search(pattern, string)

문자열에서 처음 나타나는 패턴과 일치하는 index와 문자열을 포함하는 일치하는 객체를 반환합니다.

```python
import re  #import regex module

# 문자열 앞에 r을 추가하면 원시 문자열이됩니다.
print(re.search('n', r'ba\n'))
```

위의 프로그램 출력을 실행하면 다음과 같습니다: 

```bash
<_sre.SRE_Match object; span=(3, 4), match='n'>
```

### 객체 일치 메소드

| Method        | Functionality                               |
| ------------- | -------------                               |
| start()       | 일치하는 문자열의 시작index를 반환          |
| end()         | 일치하는 문자열의 끝index를 반환            |
| span()        | 시작 및 끝 index를 tuple로 반환             |
| group()       | 일치하는 문자열을 반환                      |

 
```python
import re 

print(re.search('ab', '12abcd').start()) 
print(re.search('ab', '12abcd').end())  
print(re.search('ab', '12abcd').span())  
print(re.search('ab', '12abcd').group())
```
위의 프로그램 출력을 실행하면 다음과 같습니다: 

```bash
2
4
(2, 4)
ab
```

### re.match(pattern, string) 

문자열의 시작부분에서 패턴을 일치시키고(prefix 일치) 일치하는 객체를 반환합니다.

```python
import re 

print(re.match('abc', 'abcdef'))
```
위의 프로그램 출력을 실행하면 다음과 같습니다: 

```bash
<_sre.SRE_Match object; span=(0, 3), match='abc'>
```

### re.findall(pattern, string) 

문자열에서 패턴의 모든항목을 찾고 일치하는 문자열 list를 반환합니다.

```python
import re 

print(re.findall('[0-9]+', '12ad123cd'))
```

##### 위의 프로그램 출력을 실행하면 다음과 같습니다: 

```bash
['12', '123']
```

### re.sub(pattern, repla, string)

문자열의 모든 일치 항목을 repla로 바꾸고 수정된 문자열을 반환

```python
import re 

print(re.sub('ab', 'cd', 'habcabc'))
```

##### 위의 프로그램 출력을 실행하면 다음과 같습니다: 

```bash
hcdccdc
```

### re.compile(pattern)

패턴을 컴파일하여 정규식 객체를 반환합니다. 이 객체는 match(), search() 및 기타 메소드를 사용하여 일치시키는 데 사용할 수 있습니다.

```python
import re 

p = re.compile('ab') #p can be reused
print(p.search('cab')) 
```

위의 프로그램 출력을 실행하면 다음과 같습니다: 

```bash
<_sre.SRE_Match object; span=(1, 3), match='ab'>
```

## 반복
##### \*는 0개 이상의 선행문자 발생을 일치시키는데 사용됩니다.
##### ? 선행문자의 0또는1  발생을 일치시키는데 사용됩니다.
##### + 는 하나 이상의 선행문자 발생을 일치시키는데 사용됩니다.
##### {x,y}는 최소 x 발생 및 선행문자의 최대 y 발생을 일치시키는데 사용됩니다.

```python
import re

print(re.search('ab*c', 'abbbbbc')) 
print(re.search('ab?c', 'ac'))
print(re.search('ab+c', 'abbc'))
print(re.search('a{1,4}', 'aaabcd'))
```
위의 프로그램 출력을 실행하면 다음과 같습니다: 

```bash
<_sre.SRE_Match object; span=(0, 7), match='abbbbbc'>
<_sre.SRE_Match object; span=(0, 2), match='ac'>
<_sre.SRE_Match object; span=(0, 4), match='abbc'>
<_sre.SRE_Match object; span=(0, 3), match='aaa'>
```

# 메타 문자

##### [] 는 일치시킬 문자그룹을 묶는 데 사용됩니다.
##### [0-9] 는 모든 십진수와 일치할 수 있습니다
##### [a-d] 는 a, b, c 또는 d와 일치할 수 있습니다
##### ^ 는 일치하는 문자를 제외시키는데 사용됩니다
##### .  개행문자를 제외한 모든 문자와 일치

```python
import re

print(re.search('[a-c]{2}', 'dmacf')) 
print(re.search('[0-9]{3}', 'aa123'))
print(re.search('[^a-c]', 'ca1d'))
print(re.search('.+', 'aaabcd\n'))
```
위의 프로그램 출력을 실행하면 다음과 같습니다: 

```bash
<_sre.SRE_Match object; span=(2, 4), match='ac'>
<_sre.SRE_Match object; span=(2, 5), match='123'>
<_sre.SRE_Match object; span=(2, 3), match='1'>
<_sre.SRE_Match object; span=(0, 6), match='aaabcd'>
```

##### \ w는 [a-zA-Z0-9_]에 해당하는 모든 알파벳 숫자와 일치합니다.
##### \ d는 [0-9]에 해당하는 모든 숫자와 일치합니다.
##### \ W는 [^ a-zA-Z0-9_]와 동일한 영숫자가 아닌 문자와 일치합니다.
##### \ D는 [^ 0-9]와 같은 10 진수가 아닌 문자와 일치합니다.
##### \ s는 공백 문자와 일치

```python
import re

print(re.search('\w\w', 'c123')) 
print(re.search('\d\d\d', 'aa123bc'))
print(re.search('\W', 'ca\n'))
print(re.search('\D', '123c23'))
print(re.search('\s', 'how are'))
```
위의 프로그램 출력을 실행하면 다음과 같습니다: 

```bash
<_sre.SRE_Match object; span=(0, 2), match='c1'>
<_sre.SRE_Match object; span=(2, 5), match='123'>
<_sre.SRE_Match object; span=(2, 3), match='\n'>
<_sre.SRE_Match object; span=(3, 4), match='c'>
<_sre.SRE_Match object; span=(3, 4), match=' '>
```

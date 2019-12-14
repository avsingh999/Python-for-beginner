# 파이썬에서 int로 문자열을 나누는 방법

이를 위해서는 먼저 파이썬이 네이티브 `split ()` 함수를 사용해야하며, 구분 기호에 따라 문자열을 구분합니다.
#문법

`string.split(separator, max)`
<br/>
`separator`	선택적임. 문자열을 분할 할 때 사용할 구분기호를 지정합니다. 기본값은 공백입니다.
<br/>
`max`	선택적임. 분할 수를 지정합니다. 기본값은 -1이며 "모든 발생"입니다.

# 방법

입력
```
string = "ONE TWO"
one = string.split(' ')[0] # ['ONE']
two = string.split(' ')[1] # ['TWO']
```
`[i]` 는 어떤 단어를 선택할 것인지를 나타냅니다. 여기서 i는 분리된 단어의 위치를 나타냅니다.
<br/>

# INT로 결과를 얻는 방법
```
string = "02-04-1994"

 string.split('-')  # ['02', 04', '1994']
 
day = string.split('-')[0]  # ['02']
month = string.split('-')[1] # ['04']
year = string.split('-')[2] # ['1994']

day = int(day)
month = int(month)
year = int(year)

print(day,month,year) # output is 2 4 1994
```

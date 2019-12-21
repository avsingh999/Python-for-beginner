# JSON 파일 읽기 및 쓰기

먼저 JSON 파일을 읽는 방법을 알려주십시오
이를 위해서는 "json"라이브러리를 포함시켜야합니다.
```python
import json
```

이제 프로그램에서 json파일(이 예제에서는 test.json)을 "open"해야합니다.
파일이 .py 파일과 동일한 폴더에 있다고 가정하면 다음과 같습니다:
```python
json_file = open("test.json", 'r')
```
open함수의 두번째 매개 변수에있는 char 'r'은 test.json 파일을 읽고싶다는 것을 의미합니다.

이제 test.json의 내용으로 문자열을 만듭니다:
```python
json_text = json_file.read
```

다음으로 파이썬에서 dict에 대한 json 텍스트의 내용을 전송해야합니다:
```python
json_dic = json.loads(json_text)
```
이것이 할 일은 json 파일의 내용으로 사전을 만드는 것입니다.

따라서 이것이 json 파일 인 경우 :
```json
{
	"students": [
		{
			"name": "John Brown",
			"age": "18"
		},
		{
			"name": "Ana Miranda",
			"age": "19" 
		}
	],
	"teachers": [
		{
			"name": "Peter Black",
			"age": "30"
		},
		{
			"name": "Mandy White",
			"age": "28"
		}
	]
}
```
예를 들어 Ana의 나이를 알고 싶습다면, 다음과 같을것입니다:
```python
print(json_dic["students"][1]["age"])
#output: 19
```
json파일내용은 두개의 키( "학생"및 "교사")가 포함 된 dictionary이며 이 키는 모두 dictionary들이 있는 list들입니다.

이제 파이썬으로 자신의 json파일을 작성하려고합니다.
json이 dictionary이라는 것을 알았습니다. 그러므로 키와 내용으로 구성되어 있습니다.
json을 예로 들어 봅시다. test.json을 쓰려면 프로그램에서 dictionary으로 그를 "재작성"해야합니다.
다음과 같을것입니다:
```python
school = {}

school["students"] = [{"name":"John Brown", "age":18}]
school["students"].append({"name":"Ana Miranda", "age":19})

teachers = [{"name":"Peter Black", "age":30}, {"name":"Mandy White", "age":28}]

school["teachers"] = teachers	
```
append는 list에 더 많은 내용을 추가하는 메소드입니다. 이 경우, School ["students"]는 append 메소드가 사용되기 전에 하나의 dictionary만있는 list임을 알 수 있습니다.

이제 남은 것은 .json 파일을 작성하고 작성하는 것입니다.
읽는 것과 마찬가지로 json 라이브러리가 필요합니다. 따라서 동일한 방식으로 가져 와서 다음과 같이합니다 :
```python
json_file = open("our_file.json", 'w')
json.dump(school, json_file)
```
그리고 끝났습니다. 학교 dictionary는 이제 열린 함수에서 작성된 our_file.json 파일에 있습니다.
문자 'w'는 우리가 열린파일에 쓸 것임을 의미합니다.
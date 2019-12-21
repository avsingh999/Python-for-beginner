### 라이브러리 필요

간결하고 사용하기 쉬운 Requests 라이브러리를 사용할 것입니다. 아래과 같이 설치하세요.

```sh
pip install requests
```

## 간단한 예시

```python
import requests

r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address=Bengaluru')
print (r.text)
```
요청-응답을 저장할 객체 `r`을 만듭니다. `requests.get` 메소드는 `googleapis`서버에 get 요청을 보냅니다. 응답 내용을 보려면 `r.text`를 사용합니다.

상태 코드를 보려면 `r.status_code`를 사용하십시오.

## post 요청 예시

```python
import requests
 
url = 'http://httpbin.org/post'
payload = {'a':'test', 'b':'my post request'}
r = requests.post(url, data=payload) 
print(r.json())

data = r.json()
print(data['form'])
```

위의 예는 `httpbin`에 게시 요청을 보냅니다. `payload`는 게시 요청에서 보내려는 데이터입니다. `r.json()`은 전체 응답 메시지를 출력하고 `data['form']`은 페이로드로 보낸 데이터를 출력합니다.

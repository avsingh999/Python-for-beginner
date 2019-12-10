# 파이썬에서 Requests 라이브러리 사용하기

먼저, Requests를 소개하도록 하겠습니다.

## Requests 리소스란 무엇일까요?

Requests는 파이썬으로 작성된 Apache2가 라이선스를 가지고있는 HTTP 라이브러리입니다. Requests는 인간이 언어와 상호작용하기 위해 사용되도록 설계되었습니다. 따라서 당신은 URL에 쿼리 문자열을 수동으로 추가하거나 POST데이터를 양식에 따라 인코딩 할 필요가 없습니다. 그게 당신에게 말이 안되더라도 걱정하지 마십시오. 떄가되면 될것입니다. 

Requests가 무엇을 할 수 있나요?

Requests는 당신이 파이썬을 사용하여 HTTP/1.1 requests들을 보내는것을 허락할겁니다. 이를 통해, 간단한 파이썬 라이브러리들을 통해 헤도들, 양식 데이터, 멀티파트 파일들 및 매게변수와 같은 내용을 추가할 수 있습니다. 또한 동일한 방식으로 파이썬의 응답 데이터에 접근할 수 있습니다.  

프로그래밍에서, 라이브러리는 프로그램이 사용할 수 있는 루틴들, 함수 및 연산자들의 모음 또는 사전 구성된 선택입니다. 이러한 요소들은 종종 모듈이라고도 하며 객체형식으로 저장됩니다.

라이브러리들은 중요한데, 모듈을 로드하고 해당 모듈에 의존하는 모든 프로그램에 명시적으로 연결하지 않고 제공하는 모든 기능을 활용하기 떄문입니다. 그것들은 진짜로 독립적이므로, 그것들과 함께 다른 프로그램들과 분리된채로 자신의 프로그램들을 만들 수 있습니다.

모듈을 일종의 코드 template로 생각하세요.

다시 한번 강조하자면, Requests는 파이썬 라이브러리입니다.

## Requests를 어떻게 설치하나요?

좋은 소식은 Requests 라이브러리를 설치하는 몇가지 방법들이 있다는 것입니다. 원하는 옵션들의 전체 목록을 보려면, 여기에서 Requests의 공식 설치문서를 참조하세요.

pip, easy_install, 또는 tarball를 사용할 수 있습니다.

만약 당신이 소스코드로 작업하고 싶다면, GitHub에서도 얻을 수 있습니다.

이 안내서의 목적에 따라, 우리는 라이브러리 설치를 위해 pip을 사용할겁니다.

당신의 파이썬 interpreter에, 다음과 같이 입력하세요:


```sh
pip install requests
```

## Requests 모듈 가져오기

파이썬에서 Requests 라이브러리로 작업하려면, 적절한 모듈을 가져와야만 합니다.스크립트 시작부분에 다음과 같은 코드를 추가하면 됩니다:

```python
import requests
 ```

물론, - 라이브러리 설치를 포함하여 - 이러한것들중 아무거라도 실행하려면 당신은 필요한 패키지를 다운로드하여 interpreter가 접근할 수 있게 해야합니다.

## Request 만들기

정보를 위해 웹사이트나 포털에 접속할 때 이를 request를 만든다고 말합니다. 그것이 바로 Requests 라이브러리가 수행하도록 설계된 이유입니다.

웹 페이지를 얻으려면 다음과 같은 작업을 수행해야합니다:

```python
r = requests.get('https://github.com/timeline.json')
```

## 응답코드 작업

파이썬에서 웹 사이트 또는 URL을 사용하여 뭐든 하기 전에 해당 포털의 현재 상태코드를 확인하는 것이 좋습니다. 사전 조회 객체로 이를 수행할 수 있습니다.

```python
r = requests.get('https://github.com/timeline.json')
r.status_code
>>200

r.status_code == requests.codes.ok
>>> True

requests.codes['temporary_redirect']
>>> 307

requests.codes.teapot
>>> 418

requests.codes['o/']
>>> 200
```

## 내용 가져오기

웹 서버가 응답을 반환한 후 필요한 내용을 수집할 수 있습니다. 또한 request함수 가져오기  사용하여 수행됩니다.

```python
import requests

r = requests.get('https://github.com/timeline.json')
print r.text

# Requests 라이브러리에는 JSON 데이터를 처리해야 할 경우를 대비하여, 내장 JSON 디코더가 함께 제공됩니다.

import requests

r = requests.get('https://github.com/timeline.json')
print r.json
```

## 해더들 작업

Python사전을 활용하면, 서버의 응답헤더에 접근하고 볼 수 있습니다. Requests가 작동하는 방식 덕분에, 원하는 대문자를 사용하여 헤더에 접근 할 수 있습니다.

만약 이 기능을 수행하지만 응답에 헤더가 없는 경우, 기본값은 None입니다.

```python
r.headers

{
    'status': '200 OK',
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json; charset=utf-8'
}

r.headers['Content-Type']
>>>'application/json; charset=utf-8'

r.headers.get('content-type')
>>>'application/json; charset=utf-8'

r.headers['X-Random']
>>>None

# 주어진 헤더에서 URL 얻기
resp = requests.head("http://www.google.com")
print resp.status_code, resp.text, resp.headers
```

## 인코딩
Requests는 서버에서 가져온 컨텐츠를 자동으로 10년동안 유지합니다. 그러나 대부분의 유니코드 문자집합은 어쨌든 완벽하게 디코딩됩니다.

서버에 요청하면 Requests 라이브러리는 응답을 위한 인코딩에 대해 잘 educated된 guess를 생성하고 HTTP 헤더를 기반으로 이를 수행합니다. guess된 인코딩은 r.text 파일에 접근할 때 사용됩니다.

이 파일을 통해 Requests 라이브러리가 사용중인 인코딩을 식별하고 필요한 경우 변경할 수 있습니다. 이 기능은 파일에서 찾을 수 있는 r.encoding속성 덕분에 가능합니다.

인코딩 값을 변경하는 경, 코드에서 r.text를 호출하는한 Requests는 새 유형을 사용합니다.

```python
print r.encoding
>> utf-8

>>> r.encoding = ‘ISO-8859-1’
```

# Custom Headers

If you want to add custom HTTP headers to a request, you must pass them through a dictionary to the headers parameter.

```python
import json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
```

## Redirection and History

Requests will automatically perform a location redirection when you use the GET and OPTIONS verbs in Python.

GitHub will redirect all HTTP requests to HTTPS automatically. This keeps things secure and encrypted.

You can use the history method of the response object to track redirection status.

```python
import json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
```

## Make an HTTP Post Request
You can also handle post requests using the Requests library.

```python
r = requests.post('http://httpbin.org/post')
```

But you can also rely on other HTTP requests too, like PUT, DELETE, HEAD, and OPTIONS.

```python
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
```

You can use these methods to accomplish a great many things. For instance, using a Python script to create a GitHub repo.

```python
import requests, json

github_url = "https://api.github.com/user/repos"
data = json.dumps({'name':'test', 'description':'some test repo'})
r = requests.post(github_url, data, auth=('user', '*****'))

print r.json
```

## Errors and Exceptions

There are a number of exceptions and error codes you need to be familiar with when using the Requests library in Python.

If there is a network problem like a DNS failure, or refused connection the Requests library will raise a ConnectionError exception.
With invalid HTTP responses, Requests will also raise an HTTPError exception, but these are rare.
If a request times out, a Timeout exception will be raised.
If and when a request exceeds the preconfigured number of maximum redirections, then a TooManyRedirects exception will be raised.
Any exceptions that Requests raises will be inherited from the requests.exceptions.RequestException object.

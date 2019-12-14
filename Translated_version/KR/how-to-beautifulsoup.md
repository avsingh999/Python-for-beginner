# BeautifulSoup은 뭔가요?

BeautifulSoup은 www.crummy.com의 파이썬 라이브러리입니다.

**특징들:**

Beautiful Soup는 당신이 주는 모든 것을 parsing하고 tree traversal를합니다.

-페이지의 모든 링크를 찾기.
-특정 클래스 객체 찾기
-abc.com과 일치하는 URL 찾기
-표 제목 찾기
-특정 텍스트 찾기

**설치**

```sh
pip install beautifulsoup4
```

시스템에 pip가 설치되어 있는지 확인하십시오. cmd가 pip를 설치했는지 확인하십시오:

```sh
pip --version
```

***하는법***

*기본적인 설정*

```python
from bs4 import BeautifulSoup

# beautifulsoup4 가져오기

soup = BeautifulSoup(html_doc, 'html.parser')

# html_doc을 html parser로 구문 분석합니다 (사용 가능한 다른 parser도 있습니다)
```

*소스코드*

```python
print(soup.prettify())                

#문서의 전체 소스코드를 포맷된 방식으로 출력하다.
```

*모든 링크 찾기*

```python
for a in soup.findAll('a',href=True):
    print(a.text)
```

*특정 클래스 div 객체 찾기*

```python
mydivs = soup.findAll("div", { "class" : "stylelistrow" })
```

*모든 테이블 찾기*

```python
tables = soup.findAll("table")

for table in tables:
    if table.findParent("table") is None:
        print(str(table))
```

**추가 읽기:**

 - [Python Web Scraping Tutorial using BeautifulSoup](https://www.dataquest.io/blog/web-scraping-tutorial-python/)
 - [Web scraping and parsing with Beautiful Soup 4 Introduction](https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/)
 - [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 - [Stackoverflow Questions](https://stackoverflow.com/questions/tagged/beautifulsoup)

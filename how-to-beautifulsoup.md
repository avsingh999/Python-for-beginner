# What is BeautifulSoup?
BeautifulSoup is a Python library from www.crummy.com

**Features:**

Beautiful Soup parses anything you give it, and does the tree traversal stuff for you.
 - Find all the links in page.
 - Find specific class objects
 - Find urls that match abc.com
 - Find table headings
 - Find specific text

**Installation**
```
pip install beautifulsoup4
```
Make sure you have pip installed in system. Check whether pip is installed or not by cmd:
```
pip --version
```

***How To***

*Basic Setup*
```
from bs4 import BeautifulSoup         // imports beautifulsoup4
soup = BeautifulSoup(html_doc, 'html.parser')     //parses the html_doc with html parser (There are other parsers available too)
```

*The Source Code*
```
print(soup.prettify())                //prints the whole source code of document in formatted way
```

*Find all links*
```
for a in soup.findAll('a',href=True):
  print(a.text)
```

*Find specific class div objects*
```
mydivs = soup.findAll("div", { "class" : "stylelistrow" })
```

*Find all tables*

```
tables = soup.findAll("table")

for table in tables:
     if table.findParent("table") is None:
         print(str(table))
```

**Further Read:**
 - [Python Web Scraping Tutorial using BeautifulSoup](https://www.dataquest.io/blog/web-scraping-tutorial-python/)
 - [Web scraping and parsing with Beautiful Soup 4 Introduction](https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/)
 - [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 - [Stackoverflow Questions](https://stackoverflow.com/questions/tagged/beautifulsoup)

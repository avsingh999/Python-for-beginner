# Python regex

#### Regular expressions are used for pattern matching in a string. They provide a general way for matching patters for finding valid phone numbers, email addresses which adhere to certain format. This is a tedious task to do using normal search functionalities. Regular expressions are implemented internally using finite automata. 


### re.search(pattern, string) 
matches first occurance of pattern in the string and returns match object containing index of match and the matched string

```python
import re  #import regex module

#appending r before string makes it raw string
print(re.search('n', r'ba\n'))
```
running above program ouput will be : 

```bash
<_sre.SRE_Match object; span=(3, 4), match='n'>
```

### Match object methods

| Method        | Functionality                               |
| ------------- | -------------                               |
| start()       | return starting index of matched string     |
| end()         | return ending index of matched string       |
| span()        | return starting and ending index as tuple   |
| group()       | return matched string                       |

 
```python
import re 

print(re.search('ab', '12abcd').start()) 
print(re.search('ab', '12abcd').end())  
print(re.search('ab', '12abcd').span())  
print(re.search('ab', '12abcd').group())
```
running above program ouput will be :

```bash
2
4
(2, 4)
ab
```

### re.match(pattern, string) 
matches pattern at the beginning of the string (prefix matching) and returns the match object

```python
import re 

print(re.match('abc', 'abcdef'))
```
running above program ouput will be :

```bash
<_sre.SRE_Match object; span=(0, 3), match='abc'>
```

### re.findall(pattern, string) 
finds all occurances of pattern in string and returns list of matched strings

```python
import re 

print(re.findall('[0-9]+', '12ad123cd'))
```
##### running above program ouput will be :

```bash
['12', '123']
```

### re.sub(pattern, repla, string)
replace all matches in string with repla and returns modified string

```python
import re 

print(re.sub('ab', 'cd', 'habcabc'))
```

##### running above program ouput will be :

```bash
hcdccdc
```

### re.compile(pattern) 
compiles pattern into returns regular expression object. This object can be used for matching using match(), search() and other methods.


```python
import re 

p = re.compile('ab') #p can be reused
print(p.search('cab')) 
```

running above program ouput will be :

```bash
<_sre.SRE_Match object; span=(1, 3), match='ab'>
```

## Repetitions
##### \* is used to match 0 or more occurances of preceding character
##### ? is used to match 0 or 1 occurance of preceding character
##### + is used to match 1 or more occurances of preceding character
##### {x,y} is used to match atleast x occurances and atmost y occurances of preceding character


```python
import re

print(re.search('ab*c', 'abbbbbc')) 
print(re.search('ab?c', 'ac'))
print(re.search('ab+c', 'abbc'))
print(re.search('a{1,4}', 'aaabcd'))
```
running above program ouput will be :

```bash
<_sre.SRE_Match object; span=(0, 7), match='abbbbbc'>
<_sre.SRE_Match object; span=(0, 2), match='ac'>
<_sre.SRE_Match object; span=(0, 4), match='abbc'>
<_sre.SRE_Match object; span=(0, 3), match='aaa'>
```

# Metacharacters

##### [] are used to enclose a group of characters to be matched
##### [0-9] can match any decimal digit
##### [a-d] can match a, b, c, or d 
##### ^ is used to exclude character from matching
##### . matches any character except newline character


```python
import re

print(re.search('[a-c]{2}', 'dmacf')) 
print(re.search('[0-9]{3}', 'aa123'))
print(re.search('[^a-c]', 'ca1d'))
print(re.search('.+', 'aaabcd\n'))
```
running above program ouput will be :

```bash
<_sre.SRE_Match object; span=(2, 4), match='ac'>
<_sre.SRE_Match object; span=(2, 5), match='123'>
<_sre.SRE_Match object; span=(2, 3), match='1'>
<_sre.SRE_Match object; span=(0, 6), match='aaabcd'>
```

##### \w matches any alpha numeric character, equivalent to [a-zA-Z0-9_]
##### \d matches any digit, equivalent to [0-9]
##### \W matches character other than alpha numeric character, equivalent to [^a-zA-Z0-9_]
##### \D matches any non decimal character, equivalent to [^0-9]
##### \s matches any whitespace character


```python
import re

print(re.search('\w\w', 'c123')) 
print(re.search('\d\d\d', 'aa123bc'))
print(re.search('\W', 'ca\n'))
print(re.search('\D', '123c23'))
print(re.search('\s', 'how are'))
```
running above program ouput will be :

```bash
<_sre.SRE_Match object; span=(0, 2), match='c1'>
<_sre.SRE_Match object; span=(2, 5), match='123'>
<_sre.SRE_Match object; span=(2, 3), match='\n'>
<_sre.SRE_Match object; span=(3, 4), match='c'>
<_sre.SRE_Match object; span=(3, 4), match=' '>
```

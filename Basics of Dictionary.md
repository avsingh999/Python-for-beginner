## What is a Dictionary in Python?

Python dictionary is an unordered collection of items. It has a key: value pair.
A dictionary is a python version of hash table. It is very efficient to retrieve values when the key is known.

### Creating dictionary.

```python
dictionary = {} #empty dictionary.
dictionary = {1: 'Hello', 2: 'World'}
dictionary = {'language' : 'python', 'versions' : [2, 3]}
dictionary = dict([(1,'apple'), (2,'ball')])
```

### How to access a dictionary element.

```python
my_var = {'Language': 'Python', 'version': '3.6.6'}
print(my_var['Language']) #output: Python

print(my_var.get('version')) #output: '3.6.6'
```

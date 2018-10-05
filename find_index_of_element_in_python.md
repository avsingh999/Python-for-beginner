# How to find index of an element in python?

You can find index of an element by using the `index()` method. That method returns the first occurence of the element in a list. If it doesn't exists returns an error.

## Example 1

```python
>>> my_list = ['foo', 'bar', 'nothing', 'something', 'foo']
>>> my_list.index('bar')
1
```

## Example 2

```python
>>> my_list = ['foo', 'bar', 'nothing', 'something', 'foo']
>>> my_list.index('foo')
0
```

## Example 3

```python
>>> my_list = ['foo', 'bar', 'nothing', 'something', 'foo']
>>> my_list.index('thing')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'thing' is not in list
```

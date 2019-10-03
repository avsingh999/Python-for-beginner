# What is a try-except block?
---
Occassionally, the code you write fails, whether by accident or on purpose. This generates an error, or `exception` as we call it. Python will normally bork, and generate the message that caused it to fail. Sometimes we want to avoid stopping code, or trace what the error in particular that caused it. To do so, we make use of the `try-except` block. There are 4 different methods that we can utilize:

- `try` - this is the start of the try-except block, which effectively tests if the block throws any exceptions.
- `except` - if an exception occurs within the try block, this block gets executed. However, we can specify many of these with many different types of exceptions (see example below).
- `finally` - this code block will get executed regardless of whether the code succeeded or failed. 
- `else` - you can use this block to specify code execution if no errors were thrown.

If you want to purposefully throw an exception of your own volition, python allows for that as well! This can be achieved by using a `raise.`

#### Examples:
---
```
def foo(bar): # first we define a function
	try:
		# assert statements are what they seem to be. 
		# They assert that the code that is under the assert test is true. 
		# Otherwise, they throw an assertion error.
		assert type(bar)==str
		if bar!="hello":
			raise Exception("Cannot complete hello world!") # Throwing our own exception
	except AssertionError:
		print("bar is not a string!")
	except Exception as e:
		print(e)
		print("Another exception happened")
	else:
		print(bar+" world!")
	finally:
		print("Executed program.")
```

```
>>> foo(1)
bar is not a string!
Executed program.

>>> foo("meow")
Cannot complete hello world!
Another exception happened
Executed program.

>>> foo("hello")
hello world!
Executed program.
```
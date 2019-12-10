# Read and Write json file

First let's know how to read a json file
In order to do this you must include the "json" library.
```python
import json
```

Now we should "open" our json file (test.json in this example) in our program.
Assuming the file is in the same folder as our .py file it will look like this:
```python
json_file = open("test.json", 'r')
```
The char 'r' on the second parameter of the function open means that we want to read the test.json file.

Now we will create a string with the content of test.json:
```python
json_text = json_file.read
```

Next we should transfer the content of json_text for a dic in python:
```python
json_dic = json.loads(json_text)
```
What this will do is create a dictionary with the content of our json file.

So if this is our json file:
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
and we want to know the age of Ana, for example, it will look like:
```python
print(json_dic["students"][1]["age"])
#output: 19
```
Note that our json file content is a dictionary with two keys ("students" and "teachers") and these keys are both lists with dictionaries.

So now we want to write our own json file with Python.
Like you've noticed the json is a dictionary. So is composed of keys and their content.
So let's use our json as an example. In order to write test.json we should "recreate" him on our program as a dictionary.
It will looks like this:
```python
school = {}

school["students"] = [{"name":"John Brown", "age":18}]
school["students"].append({"name":"Ana Miranda", "age":19})

teachers = [{"name":"Peter Black", "age":30}, {"name":"Mandy White", "age":28}]

school["teachers"] = teachers	
```
append is a method for add more content to a list. In this case school["students"] as you've might noticed it's a list with only one dictionary before the append method is used.

The only thing left now is to create our .json file and write on him.
Like on reading we will need the json library. So we'll import the same way and do like this:
```python
json_file = open("our_file.json", 'w')
json.dump(school, json_file)
```
And it's done. The school dictionary is now on the our_file.json file created on the open function.
The char 'w' means that we are going to write on the oppened file.
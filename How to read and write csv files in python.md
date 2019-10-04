# How read and write csv files in python

CSV files, which are commonly used for data exports, can easily be read or created using the python standard library.

# Example: reading values from a csv file
The following program reads the contents of a csv file containing strings separated by commas on multiple lines.

```python
import csv
with open('eggs.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(', '.join(row))
```

Output:
```bash
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam
```

# Example: creating a csv file from a 2D list
The following program creates a csv file from strings in a two-dimensional list.

```python
import csv
output_list = [
    ['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Baked Beans'],
    ['Spam', 'Lovely Spam', 'Wonderful Spam']
]
with open('eggs.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for row in output_list:
        spamwriter.writerow(row)
```

When you run the program, a csv file will be created, containing the values from `output_list`. Each sublist corresponds to one line.

## Introduction
This is an example with a simple Graphical User Interface (GUI) written in Python,
using tkinter.

## About tkinter
Tkinter is a standard Python interface with the Tk GUI toolkit. For more information and full
library documentation, go [here](https://docs.python.org/3/library/tkinter.html).

## Example

```python
from tkinter import Button, Tk, messagebox

def greet():
    # This is how to create a simple pop-up box in tkinter
    # The first parameter is the title of the box, while the
    # second one represents its contents.
    messagebox.showinfo('Greetings', 'Hello, world!')

# Here, `root` is the main object that we'll use for adding can be used for adding 
# objects to our GUI, like labels, buttons, etc.
root = Tk()

# Now, we create a button in our GUI
# Here, the arguments used mean:
#    1. `master` = The parent window (in our case `root`)
#    2. `text` = The text the button will contain
#    3. `width` = The width of the button
#    4. `command` = The function that will be executed when the button is pressed.
button = Button(master=root, text='Press me!', width=10, command=greet)
# Calling this method adds the button to the GUI.
button.pack()

# Here, we start running the GUI
root.mainloop()
```


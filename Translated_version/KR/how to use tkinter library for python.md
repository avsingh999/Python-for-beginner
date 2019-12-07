# How to use tkinter library for python 
tkinter provides us with a variety of common GUI elements which we can use to build our interface – such as buttons, menus and various kinds of entry fields and display areas. 

## Window
Import the Tkinter package, we will create a window and set its title:

```python
from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.mainloop()
```

**Size Window**
Set the size of a window

```python
window.geometry('350x200')
```

## Label
Create a label widget

```python
lbl = Label(window, text="Hello")
```

Set its position in the form using the grid function with its location, in this way:

```python
lbl.grid(column=0, row=0)
```

**Set label font size**

Change font type

```python
lbl = Label(window, text="Hello", font=("Arial Bold", 24))
```

## Button

Add a button

```python
btn = Button(window, text="Click Me")
 
btn.grid(column=1, row=0)
```

## Events

Manage the event click of a button
1. We will write the function that we need to execute when the button is clicked:

```python
def clicked():
 
    lbl.configure(text="Button was clicked !!")
```

Link the event to the button

```python
btn = Button(window, text="Click Me", command=clicked)
```

## Entry (Tkinter textbox)

1. Create a text box using the Tkinter Entry class in this way:

```python
txt = Entry(window,width=10)
```

To use the entered text, it is saved by a function
def clicked ()

```python
 def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
```

## Checkbutton (Tkinter checkbox)

```python
chk = Checkbutton(window, text='Option')
```

```python
chk_state = IntVar()
 
chk_state.set(0) #uncheck
 
chk_state.set(1) #check
```


## Radio button

```python
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
```

Get the value of the radio button

```python

def clicked():
 
   print(selected.get())

```

## MessageBox

```python
from tkinter import messagebox
 
messagebox.showinfo('Message title','Message content')
```

Shows warning message

```python
messagebox.showwarning('Message title', 'Message content')
```

Shows error message

```python
messagebox.showerror('Message title', 'Message content')
```


## SpinBox 

A Spinbox widget and pass the parameters from_ and to to specify the range of numbers of the Spinbox.


```python
spin = Spinbox(window, from_=0, to=100, width=5)
```

## Add a menu bar

To add a menu bar, you can use the menu class:

```python

from tkinter import Menu
 
menu = Menu(window)
 
menu.add_command(label='File')
 
window.config(menu=menu)
```

You can add the menu items, in any menu, with the add_cascade () function:

```python
menu.add_cascade(label='File', menu=new_item)
```


Thank you

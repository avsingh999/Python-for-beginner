## Hello World with Tkinter

_First, we import the Tkinter package and create a window_

```python
from tkinter import *
window = Tk()
```

_We set the title to the window._

```python
window.title("Hello World with Tkinter")
```

_We add a label to the window with format._

```python
lbl = Label(window, text="Hello World", font=("Arial Bold", 50))
```


_Then we will establish its position in the form using the grid function with its location._

```python
lbl.grid(column=0, row=0)
```
_And that's it, we'll have our Hello World_



```python
from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
window.mainloop()
```

![](hello.png)





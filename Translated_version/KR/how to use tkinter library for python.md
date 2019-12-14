# Python에 tkinter 라이브러리를 사용하는 방법 
tkinter는 버튼, 메뉴, 다양한 입력필드 및 디스플레이 영역과 같은 인터페이스를 구축하는데 사용할 수 있는 다양한 공통 GUI 요소를 제공합니다.

## Window
Tkinter 패키지를 가져 오면 창을 만들고 제목을 설정합니다:

```python
from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.mainloop()
```

**Size Window**
windiw의 크기를 정합니다.

```python
window.geometry('350x200')
```

## Label
label위젯 만들기

```python
lbl = Label(window, text="Hello")
```

다음과 같이 그리드 기능을 사용하여 장소에 위치를 설정하십시오:

```python
lbl.grid(column=0, row=0)
```

**Set label font size**

폰트 종류 변경

```python
lbl = Label(window, text="Hello", font=("Arial Bold", 24))
```

## Button

버튼을 추가합니다

```python
btn = Button(window, text="Click Me")
 
btn.grid(column=1, row=0)
```

## Events

버튼 클릭 이벤트 관리
1. 버튼을 클릭 할 때 실행해야 할 기능을 작성합니다:

```python
def clicked():
 
    lbl.configure(text="Button was clicked !!")
```

버튼에 이벤트를 연결합니다.

```python
btn = Button(window, text="Click Me", command=clicked)
```

## Entry (Tkinter textbox)

1. 이런 식으로 Tkinter Entry 클래스를 사용하여 텍스트 상자를 만듭니다:

```python
txt = Entry(window,width=10)
```

입력한 텍스트를 사용하려면, 다음과 같은 함수로 저장되어야 합니다.
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

Spinbox 위젯으로 from_ 및 to 매개변수를 전달하여 Spinbox의 숫자범위를 지정합니다.


```python
spin = Spinbox(window, from_=0, to=100, width=5)
```

## 메뉴바 추가하기

메뉴바를 추가하려면 메뉴클래스를 사용할 수 있습니다:

```python

from tkinter import Menu
 
menu = Menu(window)
 
menu.add_command(label='File')
 
window.config(menu=menu)
```

add_cascade() 함수를 사용하여 메뉴에서 메뉴항목을 추가할 수 있습니다.

```python
menu.add_cascade(label='File', menu=new_item)
```


감사합니다

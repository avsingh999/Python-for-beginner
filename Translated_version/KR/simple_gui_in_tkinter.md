## 소개

다음은 tkinter를 사용하여 Python으로 작성된 간단한 GUI (그래픽 사용자 인터페이스)를 사용한 예입니다.

## tkinter 소개

Tkinter는 Tk GUI 툴킷과의 표준 Python 인터페이스입니다. 자세한 내용과 전체 라이브러리 설명서를 보려면 [여기] https://docs.python.org/3/library/tkinter.html로 이동하십시오.

## 예시

```python
from tkinter import Button, Tk, messagebox

def greet():
    # 이것은 tkinter에서 간단한 팝업 상자를 만드는 방법입니다
    # 첫 번째 매개 변수는 box의 제목이며 두 번째 매개 변수는 내용을 나타냅니다.
    messagebox.showinfo('Greetings', 'Hello, world!')

# 여기에서 `root`는 레이블, 버튼 등과 같이 GUI에 객체를 추가하는데 사용할 수 있는 추가에 사용할 주요 객체입니다.
root = Tk()

# 이제 GUI에서 버튼을 만듭니다
# 여기서 사용 된 인자는 다음을 의미합니다.
#    1. `master` = 부모 창 (우리의 경우`root`)
#    2. `text` = 버튼에 포함될 텍스트
#    3. `width` = 버튼의 폭
#    4. `command` = 버튼을 눌렀을 때 실행될 기능입니다.
button = Button(master=root, text='Press me!', width=10, command=greet)
# 이 메소드를 호출하면 단추가 GUI에 추가됩니다.
button.pack()

# GUI 실행을 시작합니다
root.mainloop()
```


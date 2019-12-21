# Tkinter 프로그래밍

Tkinter는 Python의 표준 GUI 라이브러리입니다. Python을 Tkinter와 결합하면 GUI응용프로그램을 빠르고쉽게 만들 수 있습니다. Tkinter는 Tk GUI툴킷에 강력한 객체지향 인터페이스를 제공합니다.

Tkinter를 사용하여 GUI 애플리케이션을 작성하는것은 쉬운 작업입니다. 다음단계를 수행하면됩니다-

* Tkinter모듈을 가져옵니다.

* GUI응용프로그램 기본창을 만듭니다.

* 위에서 언급한 위젯 중 하나 이상을 GUI 애플리케이션에 추가하십시오.

* 사용자가 trigger한 각 이벤트에 대해 조치를 수행하려면 기본 이벤트루프를 입력하십시오.

## 예시

```python
#!/usr/bin/python

import tkinter
top = tkinter.Tk()
# 위젯을 추가하는 코드는 여기에 있습니다 ...
top.mainloop()
```

## Tkinter위젯

Tkinter는 GUI 애플리케이션에서 사용되는 버튼, 레이블 및 텍스트 상자와 같은 다양한 컨트롤을 제공합니다. 이러한 컨트롤을 일반적으로 위젯이라고합니다.

Tkinter에는 현재 `15`가지 유형의 위젯이 있습니다. 다음 표에서 이러한 위젯과 간략한 설명을 제공합니다.

1. Button

버튼 위젯은 애플리케이션에 버튼을 표시하는데 사용됩니다.

2.  Canvas

Canvas 위젯은 응용 프로그램에서 선, 타원, 다각형 및 사각형과 같은 모양을 그리는 데 사용됩니다.

3. Checkbutton

Checkbutton 위젯은 여러 옵션을 확인란으로 표시하는데 사용됩니다. 사용자는 한번에 여러옵션을 선택할 수 있습니다.

4. Entry

Entry위젯은 사용자의 값을 승인하기 위한 한줄 텍스트필드를 표시하는데 사용됩니다.

5. Frame

Frame 위젯은 다른 위젯을 구성하기위한 컨테이너 위젯으로 사용됩니다.

6. Label

Label 위젯은 다른 위젯에 한줄 캡션을 제공하는데 사용됩니다. 이미지도 포함할 수 있습니다.

7. Listbox

Listbox 위젯은 사용자에게 옵션 list를 제공하는데 사용됩니다.

8. Menubutton

Menubutton위젯은 응용프로그램에 메뉴를 표시하는데 사용됩니다.

9. Menu

Menu위젯은 사용자에게 다양한 명령을 제공하는데 사용됩니다. 이 명령들은 메뉴버튼 안에 있습니다.

10. Message

Message위젯은 사용자의 값을 승인하기위해 여러줄 텍스트 필드를 표시하는데 사용됩니다.

11. Radiobutton

Radiobutton위젯은 Radiobutton으로 여러 옵션을 표시하는데 사용됩니다. 사용자는 한번에 하나의 옵션만 선택할 수 있습니다.

12. Scale

Scale위젯은 slider위젯을 제공하는데 사용됩니다.

13. Scrollbar

Scrollbar위젯은 Listbox와 같은 다양한 위젯에 스크롤기능을 추가하는데 사용됩니다.

14. Text

Text위젯은 여러줄로 텍스트를 표시하는데 사용됩니다.

15. Toplevel

Toplevel위젯은 별도의 창컨테이너를 제공하는데 사용됩니다.

16. Spinbox

Spinbox 위젯은 표준 Tkinter Entry위젯의 변형으로, 고정된 수의값 중에서 선택할 수 있습니다.

17. PanedWindow

PanedWindow는 가로 또는 세로로 배열된 여러 개의 창을 포함할 수 있는 컨테이너 위젯입니다.

18. LabelFrame

LabelFrame은 간단한 컨테이너 위젯입니다. 주요목적은 복잡한 창 레이아웃을위한 스페이서 또는 컨테이너 역할을하는 것입니다.

19. tkMessageBox

이 모듈은 응용 프로그램에서 메시지 상자를 표시하는데 사용됩니다.

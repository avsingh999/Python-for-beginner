# 파이썬에서 그래프 그리는법 📕📗

* 파이썬에는 그래프 plotting을위한 많은 라이브러리가 있지만 이 문서에는`matplotlib`의 시연이 포함되어 있습니다.

## 설치

* `pip install matplotlib`
* pip는 의존성 자체를 관리하므로 걱정할 필요가 없습니다.

## 그래프

* 설치 후 `import matplotlib.pyplot as plt` 을 통해 패키지를 가져와야합니다.
* 많은 인수를 취할 그래프 `plot ()` 을 plot하는 내장 함수가 있지만 두 개의 인수 `x` 와 `y` 좌표를 전달합니다.

```python
x = [x1, x2,x3]
y = [x4, x5, x6]
plt.plot(x, y)
```
   
* plot기능에 대한 자세한 내용은 여기를 참조하십시오 @https://matplotlib.org/users/pyplot_tutorial.html

* 그래프를 표시하려면 `show ()` 함수를 사용해야합니다

* `plt.show()`

* 위의 좌표로 선 그래프를 그릴 것입니다.

* `plot ()` 함수에는 매개변수가 거의 없으므로 이에 대해 논의하십시오.

  * xlabel :- x축 라벨을 만들기 위함.

  * ylabel :- y축 라벨을 만들기 위함.
  
```python
plt.xlabel('국가')
plt.ylabel('백만명단위')
```  
  
* Title함수는 그래프의 제목을 제공하는 데 사용됩니다. `title ()`
 
```python
plt.title('2010년까지 파키스탄 인도의 인구')
```

* 따라서 위의 단계를 수행하면 간단한 선그래프가 표시되고 아래 링크에서 그래프 plotting에 대한 자세한 내용을 읽을 수 있습니다. 😄
@ https://matplotlib.org/

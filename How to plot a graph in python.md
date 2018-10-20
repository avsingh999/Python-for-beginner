# How to plot a graph in python 📕📗

* There are so many libraries available in python for graph plotting but this documentation contains the demostration of `matplotlib`.

## Installation

* `pip install matplotlib`
* pip will take care of dependences itself so you don’t need to get worried about it.

## Graph

* You first need to import the package after installation by `import matplotlib.pyplot as plt`.

* There is a inbuild funtion to plot the graph `plot()` which will take many arguments but I am passing two arguments `x` and `y` coordinates.

```python
x = [x1, x2,x3]
y = [x4, x5, x6]
plt.plot(x, y)
```
   
* Read more about plot function here @https://matplotlib.org/users/pyplot_tutorial.html

* To display the graph you need to use `show()` function

* `plt.show()`

* It will plot a line graph with above coordinates

* There are few more parameter in `plot()` funtion so let discuss about that

  * xlabel :- For creating the label for x axis

  * ylabel :- For creating the lablel for y axis
  
```python
plt.xlabel('Countries')
plt.ylabel('Population in million')
```  
  
* Title function is used to give the title of the graph `title()`
 
```python
plt.title('Pakistan India Population till 2010')
```

* So By following the above steps you will end up with a simple line graph and you can read more about the graph plotting from the link 
below 😄
@ https://matplotlib.org/

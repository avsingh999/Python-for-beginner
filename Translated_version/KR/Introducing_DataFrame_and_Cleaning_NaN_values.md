# DataFrame 및 NaN 값 정리 소개

Import and alias Pandas:

```python
import pandas as pd
```

링크에서 테이블을 로드하고, 데이터셋을 추출하십시오. 이와 관련하여 문제가 있는 경우 읽기에 제공된 샘플 코드를 주의해서 보십시오:


```python
url='http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2018/seasontype/2'
df = pd.read_html(url, header=0)[0]
```

다음으로 열이름을 웹사이트에서 제공한 열정의와 _similar_ 가 되도록 이름을 바꿉니다. 조심하고 실수로 열이름을 두번 사용하지 마십시오. 열이 특수문자를 사용하는 경우 일반문자로 바꾸어 보다 쉽게 작업할 수 있습니다:


```python
df.columns=['RK', 'PLAYER','TEAM','GP','G','A','PTS','+/-','PIM','PTS/G','SOG','PCT','GWG','\G','\A','+G','+A']
```

```python
type(df)
df.head()
```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>RK</th>
      <th>PLAYER</th>
      <th>TEAM</th>
      <th>GP</th>
      <th>G</th>
      <th>A</th>
      <th>PTS</th>
      <th>+/-</th>
      <th>PIM</th>
      <th>PTS/G</th>
      <th>SOG</th>
      <th>PCT</th>
      <th>GWG</th>
      <th>\G</th>
      <th>\A</th>
      <th>+G</th>
      <th>+A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RK</td>
      <td>PLAYER</td>
      <td>TEAM</td>
      <td>GP</td>
      <td>G</td>
      <td>A</td>
      <td>PTS</td>
      <td>+/-</td>
      <td>PIM</td>
      <td>PTS/G</td>
      <td>SOG</td>
      <td>PCT</td>
      <td>GWG</td>
      <td>G</td>
      <td>A</td>
      <td>G</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Connor McDavid, C</td>
      <td>EDM</td>
      <td>82</td>
      <td>41</td>
      <td>67</td>
      <td>108</td>
      <td>20</td>
      <td>26</td>
      <td>1.32</td>
      <td>274</td>
      <td>15.0</td>
      <td>7</td>
      <td>5</td>
      <td>15</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Claude Giroux, LW</td>
      <td>PHI</td>
      <td>82</td>
      <td>34</td>
      <td>68</td>
      <td>102</td>
      <td>28</td>
      <td>20</td>
      <td>1.24</td>
      <td>193</td>
      <td>17.6</td>
      <td>1</td>
      <td>9</td>
      <td>27</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Nikita Kucherov, RW</td>
      <td>TB</td>
      <td>80</td>
      <td>39</td>
      <td>61</td>
      <td>100</td>
      <td>15</td>
      <td>42</td>
      <td>1.25</td>
      <td>279</td>
      <td>14.0</td>
      <td>7</td>
      <td>8</td>
      <td>28</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Evgeni Malkin, C</td>
      <td>PIT</td>
      <td>78</td>
      <td>42</td>
      <td>56</td>
      <td>98</td>
      <td>16</td>
      <td>87</td>
      <td>1.26</td>
      <td>239</td>
      <td>17.6</td>
      <td>7</td>
      <td>14</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


인자를 숫자 타입으로 변환하십시오.
* ‘raise‘인 경우, 유효하지 않은 parsing은 예외를 발생시킵니다
* ‘coerce‘인 경우, 유효하지 않은 parsing NaN으로 설정됩니다
* ‘ignore’인 경우, 유효하지 않은 parsing은 inpu를 반환합니다


```python
df['GP']= pd.to_numeric(df.GP, errors='coerce')
df['G']= pd.to_numeric(df.GP, errors='coerce')
df['A']= pd.to_numeric(df.GP, errors='coerce')
df['PTS']= pd.to_numeric(df.GP, errors='coerce')
```

결측값 감지 (숫자 배열의 NaN, 객체 배열의 None / NaN)


```python
selector=df.GP.isnull() & df.G.isnull()& df.A.isnull() & df.PTS.isnull()
```

index를 사용하여 NaN 데이터를 찾습니다


```python
#선택자
bad_rows=df[selector].index

```

label이름과 해당 축을 지정하거나 직접 index 또는 열이름을 지정하여 행 또는 열을 제거하십시오.


```python
df.drop(bad_rows, inplace=True)
```

Delete the 'RK' column:


```python
del df['RK']
df.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PLAYER</th>
      <th>TEAM</th>
      <th>GP</th>
      <th>G</th>
      <th>A</th>
      <th>PTS</th>
      <th>+/-</th>
      <th>PIM</th>
      <th>PTS/G</th>
      <th>SOG</th>
      <th>PCT</th>
      <th>GWG</th>
      <th>\G</th>
      <th>\A</th>
      <th>+G</th>
      <th>+A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Connor McDavid, C</td>
      <td>EDM</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>20</td>
      <td>26</td>
      <td>1.32</td>
      <td>274</td>
      <td>15.0</td>
      <td>7</td>
      <td>5</td>
      <td>15</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Claude Giroux, LW</td>
      <td>PHI</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>28</td>
      <td>20</td>
      <td>1.24</td>
      <td>193</td>
      <td>17.6</td>
      <td>1</td>
      <td>9</td>
      <td>27</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nikita Kucherov, RW</td>
      <td>TB</td>
      <td>80.0</td>
      <td>80.0</td>
      <td>80.0</td>
      <td>80.0</td>
      <td>15</td>
      <td>42</td>
      <td>1.25</td>
      <td>279</td>
      <td>14.0</td>
      <td>7</td>
      <td>8</td>
      <td>28</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Evgeni Malkin, C</td>
      <td>PIT</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>16</td>
      <td>87</td>
      <td>1.26</td>
      <td>239</td>
      <td>17.6</td>
      <td>7</td>
      <td>14</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Nathan MacKinnon, C</td>
      <td>COL</td>
      <td>74.0</td>
      <td>74.0</td>
      <td>74.0</td>
      <td>74.0</td>
      <td>11</td>
      <td>55</td>
      <td>1.31</td>
      <td>284</td>
      <td>13.7</td>
      <td>12</td>
      <td>12</td>
      <td>20</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

index를 재설정하여 index에 구멍이 없는지 확인하십시오. 읽은 자료에는 이것의 예가 있습니다. 그건 그렇고, 원래 index를 삭제하십시오.


```python
df.reset_index()
df.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PLAYER</th>
      <th>TEAM</th>
      <th>GP</th>
      <th>G</th>
      <th>A</th>
      <th>PTS</th>
      <th>+/-</th>
      <th>PIM</th>
      <th>PTS/G</th>
      <th>SOG</th>
      <th>PCT</th>
      <th>GWG</th>
      <th>\G</th>
      <th>\A</th>
      <th>+G</th>
      <th>+A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Connor McDavid, C</td>
      <td>EDM</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>20</td>
      <td>26</td>
      <td>1.32</td>
      <td>274</td>
      <td>15.0</td>
      <td>7</td>
      <td>5</td>
      <td>15</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Claude Giroux, LW</td>
      <td>PHI</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>28</td>
      <td>20</td>
      <td>1.24</td>
      <td>193</td>
      <td>17.6</td>
      <td>1</td>
      <td>9</td>
      <td>27</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nikita Kucherov, RW</td>
      <td>TB</td>
      <td>80.0</td>
      <td>80.0</td>
      <td>80.0</td>
      <td>80.0</td>
      <td>15</td>
      <td>42</td>
      <td>1.25</td>
      <td>279</td>
      <td>14.0</td>
      <td>7</td>
      <td>8</td>
      <td>28</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Evgeni Malkin, C</td>
      <td>PIT</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>16</td>
      <td>87</td>
      <td>1.26</td>
      <td>239</td>
      <td>17.6</td>
      <td>7</td>
      <td>14</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Nathan MacKinnon, C</td>
      <td>COL</td>
      <td>74.0</td>
      <td>74.0</td>
      <td>74.0</td>
      <td>74.0</td>
      <td>11</td>
      <td>55</td>
      <td>1.31</td>
      <td>284</td>
      <td>13.7</td>
      <td>12</td>
      <td>12</td>
      <td>20</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



각 열의 데이터 유형은 텍스트 편집기 / 스프레드 시트 프로그램을 사용하여 데이터를 볼 때 표시되는 값을 반영합니까? int32 또는 float64가 표시될 것으로 예상되는 객체가 표시되면 열에 문자열 또는 누락된 값 또는 잘못된 값이 있을 수 있음을 나타내는 좋은지표입니다.

모든 열의 데이터 유형을 확인하고 숫자여야하는 숫자가 숫자인지 확인하십시오.


```python
df.dtypes
```

```
    PLAYER     object
    TEAM       object
    GP        float64
    G         float64
    A         float64
    PTS       float64
    +/-        object
    PIM        object
    PTS/G      object
    SOG        object
    PCT        object
    GWG        object
    \G         object
    \A         object
    +G         object
    +A         object
    dtype: object

```

Convert argument to a numeric type


```python
df['+/-']= pd.to_numeric(df['+/-'], errors='coerce')
df['PIM']= pd.to_numeric(df.PIM, errors='coerce')
df['PTS/G']= pd.to_numeric(df['PTS/G'], errors='coerce')
df['SOG']= pd.to_numeric(df.SOG, errors='coerce')
df['PCT']= pd.to_numeric(df.PCT, errors='coerce')
df['GWG']= pd.to_numeric(df['GWG'], errors='coerce')
df['\G']= pd.to_numeric(df['\G'], errors='coerce')
df['\A']= pd.to_numeric(df['\A'], errors='coerce')
df['+G']= pd.to_numeric(df['+G'], errors='coerce')
df['+A']= pd.to_numeric(df['+A'], errors='coerce')
df.head()
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PLAYER</th>
      <th>TEAM</th>
      <th>GP</th>
      <th>G</th>
      <th>A</th>
      <th>PTS</th>
      <th>+/-</th>
      <th>PIM</th>
      <th>PTS/G</th>
      <th>SOG</th>
      <th>PCT</th>
      <th>GWG</th>
      <th>\G</th>
      <th>\A</th>
      <th>+G</th>
      <th>+A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Connor McDavid, C</td>
      <td>EDM</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>20</td>
      <td>26</td>
      <td>1.32</td>
      <td>274</td>
      <td>15.0</td>
      <td>7</td>
      <td>5</td>
      <td>15</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Claude Giroux, LW</td>
      <td>PHI</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>28</td>
      <td>20</td>
      <td>1.24</td>
      <td>193</td>
      <td>17.6</td>
      <td>1</td>
      <td>9</td>
      <td>27</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nikita Kucherov, RW</td>
      <td>TB</td>
      <td>80.0</td>
      <td>80.0</td>
      <td>80.0</td>
      <td>80.0</td>
      <td>15</td>
      <td>42</td>
      <td>1.25</td>
      <td>279</td>
      <td>14.0</td>
      <td>7</td>
      <td>8</td>
      <td>28</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Evgeni Malkin, C</td>
      <td>PIT</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>16</td>
      <td>87</td>
      <td>1.26</td>
      <td>239</td>
      <td>17.6</td>
      <td>7</td>
      <td>14</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Nathan MacKinnon, C</td>
      <td>COL</td>
      <td>74.0</td>
      <td>74.0</td>
      <td>74.0</td>
      <td>74.0</td>
      <td>11</td>
      <td>55</td>
      <td>1.31</td>
      <td>284</td>
      <td>13.7</td>
      <td>12</td>
      <td>12</td>
      <td>20</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

```python
df.dtypes
```

```
    PLAYER     object
    TEAM       object
    GP        float64
    G         float64
    A         float64
    PTS       float64
    +/-         int64
    PIM         int64
    PTS/G     float64
    SOG         int64
    PCT       float64
    GWG         int64
    \G          int64
    \A          int64
    +G          int64
    +A          int64
    dtype: object

```

your_data_frame [ 'your_column']. unique () 또는 동일하게 your_data_frame.your_column.unique ()를 사용하여 각 열의 고유 한 값을보고 불량 값을 식별하십시오.

NaN으로 올바르게 인코딩해야하는 값을 찾으면 데이터 프레임을 로드할 때 na_values 매개변수를 사용하여 변환할 수 있습니다. 또는 대안으로 독서에서 논의된 다른방법 중 하나를 사용하십시오.


```python
df.PCT.unique()
```

```
    array([15. , 17.6, 14. , 13.7, 17.5, 13. ,  9.4, 11.7, 13.8, 12.7, 18.7,
           12.9,  8.8, 14.4, 16.3, 10.6, 11.8, 14.2, 14.9, 23.4, 11.9, 10.5,
           17.4,  9.5, 10.8, 10.1, 12.4, 18.3, 13.3, 14.8, 13.2, 11.3,  6.3])

```

[2 : 4, 'col3']으로 데이터 프레임을 indexing하기 위해 사용해야하는 indexing 방법을 알아 봅니다. 마지막으로 결과를 표시하십시오.

```python
df.iloc[2:4, [3]]
```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>G</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>80.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>78.0</td>
    </tr>
  </tbody>
</table>
</div>

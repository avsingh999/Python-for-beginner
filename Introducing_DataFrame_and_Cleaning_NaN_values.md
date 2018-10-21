# Introducing the DataFrame and Cleaning NaN values

Import and alias Pandas:

```python
import pandas as pd
```

Load up the table from the link, and extract the dataset out of it. If you're having issues with this, look carefully at the sample code provided in the reading:


```python
url='http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2018/seasontype/2'
df = pd.read_html(url, header=0)[0]
```

Next up, rename the columns so that they are _similar_ to the column definitions provided to you on the website. Be careful and don't accidentally use any column names twice. If a column uses special characters, you can replace them with regular characters to make it easier to work with:


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


Convert argument to a numeric type.
* If ‘raise’, then invalid parsing will raise an exception
* If ‘coerce’, then invalid parsing will be set as NaN
* If ‘ignore’, then invalid parsing will return the inpu


```python
df['GP']= pd.to_numeric(df.GP, errors='coerce')
df['G']= pd.to_numeric(df.GP, errors='coerce')
df['A']= pd.to_numeric(df.GP, errors='coerce')
df['PTS']= pd.to_numeric(df.GP, errors='coerce')
```

Detect missing values (NaN in numeric arrays, None/NaN in object arrays)


```python
selector=df.GP.isnull() & df.G.isnull()& df.A.isnull() & df.PTS.isnull()
```

Locate the NaN data using the index


```python
#selector
bad_rows=df[selector].index

```

Remove rows or columns by specifying label names and corresponding axis, or by specifying directly index or column names


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

Make sure there are no holes in your index by resetting it. There is an example of this in the reading material. By the way, drop the original index.


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



Do the data-types of each column reflect the values you see when you look through the data using a text editor / spread sheet program? If you see object where you expect to see int32 or float64, that is a good indicator that there might be a string or missing value or erroneous value in the column.

Check the data type of all columns, and ensure those that should be numeric are numeric.


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

Try use your_data_frame['your_column'].unique() or equally, your_data_frame.your_column.unique() to see the unique values of each column and identify the rogue values.

If you find any value that should be properly encoded to NaNs, you can convert them either using the na_values parameter when loading the dataframe. Or alternatively, use one of the other methods discussed in the reading.


```python
df.PCT.unique()
```

```
    array([15. , 17.6, 14. , 13.7, 17.5, 13. ,  9.4, 11.7, 13.8, 12.7, 18.7,
           12.9,  8.8, 14.4, 16.3, 10.6, 11.8, 14.2, 14.9, 23.4, 11.9, 10.5,
           17.4,  9.5, 10.8, 10.1, 12.4, 18.3, 13.3, 14.8, 13.2, 11.3,  6.3])

```

Figure out which indexing method you would need to use in order to index your dataframe with: [2:4, 'col3']. Finally, display the results:

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

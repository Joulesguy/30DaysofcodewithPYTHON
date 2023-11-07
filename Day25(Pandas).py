# 📘 Day 25: - 30DaysOfPython Challenge by Swift Cyberwatch
## Pandas
'''
Pandas is an open source, high-performance, easy-to-use data structures and data analysis 
tools for the Python programming language.
Pandas adds data structures and tools designed to work with table-like data which is *Series* 
and *Data Frames*.
Pandas provides tools for data manipulation: 
- reshaping
- merging
- sorting
- slicing
- aggregation
- imputation.
If you are using anaconda, you do not have install pandas.
'''
### Installing Pandas
'''
For Mac:
```
pip install conda
conda install pandas
```
For Windows:
```
pip install conda
pip install pandas
```
Pandas data structure is based on *Series* and *DataFrames*. 
A *series* is a *column* and a DataFrame is a *multidimensional table* made up of collection 
of *series*. In order to create a pandas series we should use numpy to create a one 
dimensional arrays or a python list.
Let us see an example of a series:
Names Pandas Series
Name
0 David
1 James
2 John
Countries Series
Country
0 United Kingdom
1 Canada
2 Nigeria
Cities Series
City
0 London
1 Alberta
2 Lagos
As you can see, pandas series is just one column of data. If we want to have multiple columns 
we use data frames. The example below shows pandas DataFrames.
Let us see, an example of a pandas data frame:
Name Country City
0 David United Kingdom London
1 James Canada Alberta
2 John Nigeria Lagos
Data frame is a collection of rows and columns. Look at the table below; it has many more 
columns than the example above:
Name Country City Weight Height
0 David United Kingdom London 74 174
1 James Canada Alberta 78 178
2 John Nigeria Lagos 69 169
Next, we will see how to import pandas and how to create Series and DataFrames using pandas
'''
### Importing Pandas

import pandas as pd # importing pandas as pd
import numpy as np # importing numpy as np

### Creating Pandas Series with Default Index

nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# dtype: int64

### Creating Pandas Series with custom index

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

# 1 1
# 2 2
# 3 3
# 4 4
# 5 5
# dtype: int64

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# 1 Orange
# 2 Banana
# 3 Mango
dtype: object

### Creating Pandas Series from a Dictionary

dct = {'name':'James','country':'Nigeria','city':'Ibadan'}

s = pd.Series(dct)
print(s)

# name James
# country Canada
# city Alberta
dtype: object

### Creating a Constant Pandas Series

s = pd.Series(10, index = [1, 2, 3])
print(s)

# 1 10
# 2 10
# 3 10
# dtype: int64

### Creating a Pandas Series Using Linspace

s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

# 0 5.000000
# 1 6.666667
# 2 8.333333
# 3 10.000000
# 4 11.666667
# 5 13.333333
# 6 15.000000
# 7 16.666667
# 8 18.333333
# 9 20.000000
# dtype: float64

## DataFrames
# Pandas data frames can be created in different ways.
### Creating DataFrames from List of Lists

data = [
['James', 'Canada', 'Alberta'], 
['David', 'UK', 'London'],
['John', 'Nigeria', 'Lagos']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Names</th>
# <th>Country</th>
# <th>City</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# </tr>
# </tbody>
# </table>
### Creating DataFrame Using Dictionary

data = {'Name': ['James', 'David', 'John'], 'Country':[
'Canada', 'UK', 'Nigeria'], 'City': ['Alberta', 'London', 'Lagos']}
df = pd.DataFrame(data)
print(df)

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# </tr>
# </tbody>
# </table>
### Creating DataFrames from a List of Dictionaries

data = [
{'Name': 'James', 'Country': 'Canada', 'City': 'Alberta'},
{'Name': 'David', 'Country': 'UK', 'City': 'London'},
{'Name': 'John', 'Country': 'Nigeria', 'City': 'Lagos'}]
df = pd.DataFrame(data)
print(df)

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# </tr>
# </tbody>
# </table>
## Reading CSV File Using Pandas
# To download the CSV file, what is needed in this example, console/command line is enough:
# ```
# curl -O https://raw.githubusercontent.com/James/30-Days-Of-Python/master/data/weight￾height.csv
# ```
# Put the downloaded file in your working directory.

import pandas as pd
df = pd.read_csv('weight-height.csv')
print(df)

### Data Exploration
# Let us read only the first 5 rows using head()

print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Gender</th>
# <th>Height</th>
# <th>Weight</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>Male</td>
# <td>73.847017</td>
# <td>241.893563</td>
# </tr>
# <tr>
# <td>1</td>
# <td>Male</td>
# <td>68.781904</td>
# <td>162.310473</td>
# </tr>
# <tr>
# <td>2</td>
# <td>Male</td>
# <td>74.110105</td>
# <td>212.740856</td>
# </tr>
# <tr>
# <td>3</td>
# <td>Male</td>
# <td>71.730978</td>
# <td>220.042470</td>
# </tr>
# <tr>
# <td>4</td>
# <td>Male</td>
# <td>69.881796</td>
# <td>206.349801</td>
# </tr>
# </tbody>
# </table>
# Let us also explore the last recordings of the dataframe using the tail() methods.

print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Gender</th>
# <th>Height</th>
# <th>Weight</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>9995</td>
# <td>Female</td>
# <td>66.172652</td>
# <td>136.777454</td>
# </tr>
# <tr>
# <td>9996</td>
# <td>Female</td>
# <td>67.067155</td>
# <td>170.867906</td>
# </tr>
# <tr>
# <td>9997</td>
# <td>Female</td>
# <td>63.867992</td>
# <td>128.475319</td>
# </tr>
# <tr>
# <td>9998</td>
# <td>Female</td>
# <td>69.034243</td>
# <td>163.852461</td>
# </tr>
# <tr>
# <td>9999</td>
# <td>Female</td>
# <td>61.944246</td>
# <td>113.649103</td>
# </tr>
# </tbody>
# </table>
# As you can see the csv file has three rows: Gender, Height and Weight. If the DataFrame would 
# have a long rows, it would be hard to know all the columns. Therefore, we should use a method 
# to know the colums. we do not know the number of rows. Let's use shape meathod.

print(df.shape) # as you can see 10000 rows and three columns (10000, 3)
# Let us get all the columns using columns.
# ```
print(df.columns)
# ```
# Index(['Gender', 'Height', 'Weight'], dtype='object')
# Now, let us get a specific column using the column key
# ```
heights = df['Height'] # this is now a series
# ```
# ```
print(heights)

# 0 73.847017
# 1 68.781904
# 2 74.110105
# 3 71.730978
# 4 69.881796
# ... 
# 9995 66.172652
# 9996 67.067155
# 9997 63.867992
# 9998 69.034243
# 9999 61.944246
# Name: Height, Length: 10000, dtype: float64
# ```
# ```
weights = df['Weight'] # this is now a series
# ```
# ```
print(weights)
# ```
# ```
# 0 241.893563
# 1 162.310473
# 2 212.740856
# 3 220.042470
# 4 206.349801
# ... 
# 9995 136.777454
# 9996 170.867906
# 9997 128.475319
# 9998 163.852461
# 9999 113.649103
# Name: Weight, Length: 10000, dtype: float64

print(len(heights) == len(weights))

True
# The describe() method provides a descriptive statistical values of a dataset.
print(heights.describe()) # give statisical information about height data

# count 10000.000000
# mean 66.367560
# std 3.847528
# min 54.263133
# 25% 63.505620
# 50% 66.318070
# 75% 69.174262
# max 78.998742
# Name: Height, dtype: float64

print(weights.describe())

# count 10000.000000
# mean 161.440357
# std 32.108439
# min 64.700127
# 25% 135.818051
# 50% 161.212928
# 75% 187.169525
# max 269.989699
# Name: Weight, dtype: float64

print(df.describe()) # describe can also give statistical information from a dataFrame

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Height</th>
# <th>Weight</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>count</td>
# <td>10000.000000</td>
# <td>10000.000000</td>
# </tr>
# <tr>
# <td>mean</td>
# <td>66.367560</td>
# <td>161.440357</td>
# </tr>
# <tr>
# <td>std</td>
# <td>3.847528</td>
# <td>32.108439</td>
# </tr>
# <tr>
# <td>min</td>
# <td>54.263133</td>
# <td>64.700127</td>
# </tr>
# <tr>
# <td>25%</td>
# <td>63.505620</td>
# <td>135.818051</td>
# </tr>
# <tr>
# <td>50%</td>
# <td>66.318070</td>
# <td>161.212928</td>
# </tr>
# <tr>
# <td>75%</td>
# <td>69.174262</td>
# <td>187.169525</td>
# </tr>
# <tr>
# <td>max</td>
# <td>78.998742</td>
# <td>269.989699</td>
# </tr>
# </tbody>
# </table>
# Similar to describe(), the info() method also give information about the dataset.
## Modifying a DataFrame
# Modifying a DataFrame:
# * We can create a new DataFrame
# * We can create a new column and add it to the DataFrame, 
# * we can remove an existing column from a DataFrame, 
# * we can modify an existing column in a DataFrame, 
# * we can change the data type of column values in the DataFrame
### Creating a DataFrame
# As always, first we import the necessary packages. Now, lets import pandas and numpy, two best friends ever.

import pandas as pd
import numpy as np
data = [
{"Name": "James", "Country":"Canada","City":"Alberta"},
{"Name": "David", "Country":"UK","City":"London"},
{"Name": "John", "Country":"Nigeria","City":"Lagos"}]
df = pd.DataFrame(data)
print(df)

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# </tr>
# </tbody>
# </table>
# Adding a column to a DataFrame is like adding a key to a dictionary.
# First let's use the previous example to create a DataFrame. After we create the DataFrame, we 
# will start modifying the columns and column values.
### Adding a New Column
# Let's add a weight column in the DataFrame

weights = [74, 78, 69]
df['Weight'] = weights
df

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# <th>Weight</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# <td>74</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# <td>78</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# <td>69</td>
# </tr>
# </tbody>
# </table>
# Let's add a height column into the DataFrame aswell

heights = [173, 175, 169]
df['Height'] = heights
print(df)

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# <th>Weight</th>
# <th>Height</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# <td>74</td>
# <td>173</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# <td>78</td>
# <td>175</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# <td>69</td>
# <td>169</td>
# </tr>
# </tbody>
# </table>
# As you can see in the DataFrame above, we did add new columns, Weight and Height. Let's add 
# one additional column called BMI(Body Mass Index) by calculating their BMI using thier mass 
# and height. BMI is mass divided by height squared (in meters) - Weight/Height * Height.
# As you can see, the height is in centimeters, so we shoud change it to meters. Let's modify 
# the height row.
### Modifying column values

df['Height'] = df['Height'] * 0.01
df

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# <th>Weight</th>
# <th>Height</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# <td>74</td>
# <td>1.73</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# <td>78</td>
# <td>1.75</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# <td>69</td>
# <td>1.69</td>
# </tr>
# </tbody>
# </table>

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
    bmi.append(b)
    return bmi
bmi = calculate_bmi()

df['BMI'] = bmi
df

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# <th>Weight</th>
# <th>Height</th>
# <th>BMI</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# <td>74</td>
# <td>1.73</td>
# <td>24.725183</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# <td>78</td>
# <td>1.75</td>
# <td>25.469388</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# <td>69</td>
# <td>1.69</td>
# <td>24.158818</td>
# </tr>
# </tbody>
# </table>
### Formating DataFrame columns
# The BMI column values of the DataFrame are float with many significant digits after decimal. 
# Let's change it to one significant digit after point.

df['BMI'] = round(df['BMI'], 1)
print(df)

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# <th>Weight</th>
# <th>Height</th>
# <th>BMI</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# <td>74</td>
# <td>1.73</td>
# <td>24.7</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# <td>78</td>
# <td>1.75</td>
# <td>25.5</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# <td>69</td>
# <td>1.69</td>
# <td>24.2</td>
# </tr>
# </tbody>
# </table>
# The information in the DataFrame seems not yet complete, let's add birth year and current year 
# columns.

birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
df

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# <th>Weight</th>
# <th>Height</th>
# <th>BMI</th>
# <th>Birth Year</th>
# <th>Current Year</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# <td>74</td>
# <td>1.73</td>
# <td>24.7</td>
# <td>1769</td>
# <td>2020</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# <td>78</td>
# <td>1.75</td>
# <td>25.5</td>
# <td>1985</td>
# <td>2020</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# <td>69</td>
# <td>1.69</td>
# <td>24.2</td>
# <td>1990</td>
# <td>2020</td>
# </tr>
# </tbody>
# </table>
## Checking data types of Column values

print(df.Weight.dtype)

# dtype('int64')

df['Birth Year'].dtype # it gives string object , we should change this to number

df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # let's check the data type now

# dtype('int32')

# Now same for the current year:

df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype

dtype('int32')

# Now, the column values of birth year and current year are integers. We can calculate the age.

ages = df['Current Year'] - df['Birth Year']
ages

# 0 251
# 1 35
# 2 30
# dtype: int32

df['Ages'] = ages
print(df)

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# <th>Weight</th>
# <th>Height</th>
# <th>BMI</th>
# <th>Birth Year</th>
# <th>Current Year</th>
# <th>Ages</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# <td>74</td>
# <td>1.73</td>
# <td>24.7</td>
# <td>1769</td>
# <td>2019</td>
# <td>250</td>
# </tr>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# <td>78</td>
# <td>1.75</td>
# <td>25.5</td>
# <td>1985</td>
# <td>2019</td>
# <td>34</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# <td>69</td>
# <td>1.69</td>
# <td>24.2</td>
# <td>1990</td>
# <td>2019</td>
# <td>29</td>
# </tr>
# </tbody>
# </table>
# The person in the first row lived so far for 251 years. It is unlikely for someone to live so 
# long. Either it is a typo or the data is cooked. So lets fill that data with average of the 
# columns without including outlier. 
mean = (35 + 30)/ 2

mean = (35 + 30)/ 2
print('Mean: ',mean) #it is good to add some description to the output, so we know what is what

Mean: 32.5

### Boolean Indexing

print(df[df['Ages'] > 120])

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# <th>Weight</th>
# <th>Height</th>
# <th>BMI</th>
# <th>Birth Year</th>
# <th>Current Year</th>
# <th>Ages</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>0</td>
# <td>James</td>
# <td>Canada</td>
# <td>Alberta</td>
# <td>74</td>
# <td>1.73</td>
# <td>24.7</td>
# <td>1769</td>
# <td>2020</td>
# <td>251</td>
# </tr>
# </tbody>
# </table>

print(df[df['Ages'] < 120])

# <table border="1" class="dataframe">
# <thead>
# <tr style="text-align: right;">
# <th></th>
# <th>Name</th>
# <th>Country</th>
# <th>City</th>
# <th>Weight</th>
# <th>Height</th>
# <th>BMI</th>
# <th>Birth Year</th>
# <th>Current Year</th>
# <th>Ages</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td>1</td>
# <td>David</td>
# <td>UK</td>
# <td>London</td>
# <td>78</td>
# <td>1.75</td>
# <td>25.5</td>
# <td>1985</td>
# <td>2020</td>
# <td>35</td>
# </tr>
# <tr>
# <td>2</td>
# <td>John</td>
# <td>Nigeria</td>
# <td>Lagos</td>
# <td>69</td>
# <td>1.69</td>
# <td>24.2</td>
# <td>1990</td>
# <td>2020</td>
# <td>30</td>
# </tr>
# </tbody>
# </table>
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
#load the weather dataset from the downloads folder
data=pd.read_csv('~/Downloads/weather_data.csv')
#display the first few rows of the dataset
print(data.head())
   Outdoor Drybulb Temperature [C]  ...  24h Prediction Direct Solar Radiation [W/m2]
0                            17.81  ...                                           0.0
1                            16.14  ...                                           0.0
2                            16.10  ...                                           0.0
3                            16.10  ...                                           0.0
4                            16.16  ...                                           0.0

[5 rows x 16 columns]
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> #visualize the data to identify outliers
>>> sns.boxplot(data=data)
<Axes: >
pl
>>> plt.show()
>>> #calculate q1,q3 and IQR
>>> Q1= data.quantile(0.25)
>>> Q3= data.quantile(0.75)
>>> IQR= Q3-Q1
>>> #check the lower bound condition
>>> lower_bound_condition=data<(q1-1.5*IQR)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    lower_bound_condition=data<(q1-1.5*IQR)
NameError: name 'q1' is not defined. Did you mean: 'Q1'?
>>> #filter the outliers
>>> data=data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1))]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> #compute the correlation matrix
>>> corr=data.corr()
>>> #display the correlation matrix
>>> sns.heatmap(corr, annot=True,cmap='coolwarm')
<Axes: >
>>> plt.show()
>>> from sklearn.model_selection import train_test_split
>>> from sklearn.linear_model import Linearregression
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    from sklearn.linear_model import Linearregression
ImportError: cannot import name 'Linearregression' from 'sklearn.linear_model' (C:\Users\Sankar\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\linear_model\__init__.py)

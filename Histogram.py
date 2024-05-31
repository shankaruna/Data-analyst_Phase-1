Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
from sklearn.datasets import load_iris
#load the iris dataset
iris=load_iris()
#get features and target labels
data=pd.DataFrame(iris.data,columns=iris.feature_names)
target=iris.target_names[iris.target]
#get basic statistics
print(data.describe())
       sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
count         150.000000        150.000000         150.000000        150.000000
mean            5.843333          3.057333           3.758000          1.199333
std             0.828066          0.435866           1.765298          0.762238
min             4.300000          2.000000           1.000000          0.100000
25%             5.100000          2.800000           1.600000          0.300000
50%             5.800000          3.000000           4.350000          1.300000
75%             6.400000          3.300000           5.100000          1.800000
max             7.900000          4.400000           6.900000          2.500000
#visualize data distribution(histogram)
import matplotlib.pyplot as plt
data.hist(figsize=(10,6))
array([[<Axes: title={'center': 'sepal length (cm)'}>,
        <Axes: title={'center': 'sepal width (cm)'}>],
       [<Axes: title={'center': 'petal length (cm)'}>,
        <Axes: title={'center': 'petal width (cm)'}>]], dtype=object)
plt.xlabel("features")
Text(0.5, 0, 'features')
>>> plt.ylabel("frequency")
Text(0, 0.5, 'frequency')
>>> plt.title("distribution of Iris flower features")
Text(0.5, 1.0, 'distribution of Iris flower features')
>>> plt.show()
>>> #scatter plot for Sepal length vs. Sepal width colored by species
>>> plt.figure(figsize=(8,6))
<Figure size 800x600 with 0 Axes>
>>> #adjust figure size for better visualization
>>> plt.scatter(iris_data['sepallength'),iris_data['sepalwidth'],iris_data['species']
...             
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> plt.scatter(iris_data['sepallength'],iris_data['sepalwidth'],iris_data['species'])
...             
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    plt.scatter(iris_data['sepallength'],iris_data['sepalwidth'],iris_data['species'])
NameError: name 'iris_data' is not defined
>>> plt.scatter
...             
<function scatter at 0x000001C1FD4084A0>
>>> plt.xlabel('sepal length (cm)')
...             
Text(0.5, 0, 'sepal length (cm)')
>>> plt.ylabel('sepal width (cm)')
...             
Text(0, 0.5, 'sepal width (cm)')
>>> plt.title('relationship between sepal length and sepal width')
...             
Text(0.5, 1.0, 'relationship between sepal length and sepal width')
>>> plt.legend()
...             

Warning (from warnings module):
  File "<pyshell#25>", line 1
UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
<matplotlib.legend.Legend object at 0x000001C1FDD4B890>
>>> plt.show()
...             

Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> from sklearn.datasets import load_iris
>>> #Load the Iris dataset
>>> iris=load_iris()
>>> #Get features and target labels
>>> data=pd.DataFrame(iris.data, columns=iris.feature_names)
>>> target = iris.target_names[iris.target]
>>> #Get basic statistics
>>> print(data.describe())
       sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
count         150.000000        150.000000         150.000000        150.000000
mean            5.843333          3.057333           3.758000          1.199333
std             0.828066          0.435866           1.765298          0.762238
min             4.300000          2.000000           1.000000          0.100000
25%             5.100000          2.800000           1.600000          0.300000
50%             5.800000          3.000000           4.350000          1.300000
75%             6.400000          3.300000           5.100000          1.800000
max             7.900000          4.400000           6.900000          2.500000
>>> #Visualize data distribution(Histogram)
>>> import matplotlib.pyplot as plt
>>> data.hist(figsize=(10,6))
array([[<Axes: title={'center': 'sepal length (cm)'}>,
        <Axes: title={'center': 'sepal width (cm)'}>],
       [<Axes: title={'center': 'petal length (cm)'}>,
        <Axes: title={'center': 'petal width (cm)'}>]], dtype=object)
>>> plt.xlabel("features")
Text(0.5, 0, 'features')
>>> plt.ylabel("frequency")
Text(0, 0.5, 'frequency')
>>> plt.title("distribution of Iris flower features")
Text(0.5, 1.0, 'distribution of Iris flower features')
>>> plt.show()



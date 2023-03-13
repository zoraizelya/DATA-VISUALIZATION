# we need to import libraries first
import seaborn as sns
import matplotlib.pyplot as plt
# we do use numpy to find something like mean / median 
import numpy

# we need to load data set
flower = sns.load_dataset("iris")
print(flower)
# for line ploting graph
# sns.lineplot(x="sepal_length",y="species",data=flower)
# we do some style and more things
sns.barplot(x="sepal_length",y="petal_length",hue="species",ci=None, palette="pastel",data=flower,color="red",saturation=0.2,estimator=numpy.mean)
plt.show()
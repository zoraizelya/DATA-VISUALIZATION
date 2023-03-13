# 1st we need to import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# 2nd this is to set a theme
sns.set_theme(style="ticks",color_codes=True)

# 3rd  import data set
titanic = sns.load_dataset("titanic")
#print(titanic)

# # 4th we have to plot basic graph with 1 variable
# p = sns.countplot(x="sex", data=titanic)
# plt.show()

# # 5th plot basic graph with 2 variables
# p = sns.countplot(x="sex",hue="class", data=titanic)
# plt.show()

# 6th plot basic graph with 2 variables,  with a title
p = sns.countplot(x="sex",hue="class", data=titanic)
p.set_title("Plot for Basic Titanic")
plt.show()
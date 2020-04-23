# https://www.kaggle.com/rtatman/datasets-for-regression-analysis
# importing relavant libraries:

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import pearsonr

# importing data:

data = pd.read_csv (r'/home/ram/Desktop/reg_data/deaths_data/corona_cases.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
print(data)
print(data.describe())
print(data.columns)

y=data['Total Deaths']
def Reverse(lst):
    return [ele for ele in reversed(lst)]
y=Reverse(y)
x1=data['Total cases']
x1=Reverse(x1)
#The Pearson correlation coefficient (named for Karl Pearson) can
# be used to summarize the strength of the linear relationship between
# two data samples.
corr, _ = pearsonr(x1, y)
print('Pearsons correlation: %.3f' % corr)

# Exploring the Data
plt.scatter(x1, y)
plt.xlabel("Total dialy cases",fontsize = 20)
plt.ylabel("Total daily Deaths",fontsize = 20)
plt.show()
# R^2----we can conclude that how much percentage of the total sum of squares
# can be explained by using the estimated regression equation to
# #predict the required . the remainder is error!
x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()
print(results.summary())

# Plotting the Regression line
plt.scatter(x1, y)
yhat = [0.5205 * i + 137.2966 for i in x1]
fig = plt.plot(x1, yhat, lw=4, c="orange", label = "regressionline")
plt.xlabel("Total dialy cases", fontsize = 20)
plt.ylabel("Total daily Deaths", fontsize = 20)
plt.show()




import matplotlib
import matplotlib.pyplot as plt
import numpy as np

lst1=x1;
lst2=y;
lst_p=data['Date']
labels = data['Date']
men_means = lst1
women_means = lst2

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='cases')
rects2 = ax.bar(x + width/2, women_means, width, label='deaths')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()

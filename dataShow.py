import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 数据准备
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
# 用 Matplotlib 画散点图
plt.scatter(x, y,marker='<')
plt.show()
# 用 Seaborn 画散点图
df = pd.DataFrame({'x': x, 'y': y})
sns.jointplot(x="x", y="y", data=df, kind='scatter');
plt.show()
# 用 Matplotlib 画折线图
x=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
y=[5,3,6,20,12,40,32,35,23,19]
plt.plot(x,y)
plt.show()
# 用 Seaborn 画折线图
df=pd.DataFrame({'x':x,'y':y})
sns.lineplot(x="x",y="y",data=df)
plt.show()
#数据准备
a=np.random.randn(100)
s=pd.Series(a)
# 用 Matplotlib 画直方图
plt.hist(s)
plt.show()
# 用 Seaborn 画直方图
sns.distplot(s,kde=True)
plt.show()
sns.distplot(s,kde=False)
plt.show()
# 数据准备
x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
y = [5, 4, 8, 12, 7]
# 用 Matplotlib 画条形图
plt.bar(x, y)
plt.show()
# 用 Seaborn 画条形图
sns.barplot(x, y)
plt.show()

# 数据准备
#生成0-1之间的10*4维度数据
data=np.random.normal(size=(10,4))
lables=['A','B','C','D']
# 用 Matplotlib 画箱线图
plt.boxplot(data,labels=lables)
plt.show()
# 用 Seaborn 画箱线图
df=pd.DataFrame(data,columns=lables)
sns.boxplot(data=df)
plt.show()

#数据准备
nums=[25,37,33,37,6]
labels=['high-school','bachelor','master','ph.d','other']
# 用 Matplotlib 画饼图
plt.pie(x=nums,labels=labels)
plt.show()

#数据准备
flights=sns.load_dataset("flights")
data=flights.pivot('year','month','passengers')
#用seaborn画热力图
sns.heatmap(data)
plt.show()

#数据准备
car_crashes=sns.load_dataset('car_crashes')
#用seaborn画成对关系
sns.pairplot(car_crashes)
plt.show()


#预测波士顿房价
#encoding=utf-8
from sklearn.model_selection import  train_test_split
from sklearn.metrics import  mean_absolute_error
from sklearn.datasets import  load_boston
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.tree import  DecisionTreeRegressor
#准备数据集
boston=load_boston()
#探索数据
print(boston.feature_names)
#获取特征集和分类标识
features=boston.data
prices=boston.target
#获取33%的数据作为测试集
train_features,test_features,train_prices,test_prices=train_test_split(features,prices,test_size=0.33,random_state=0)
#创建回归树
dtr=DecisionTreeRegressor()
#拟合构造CART回归树
dtr.fit(train_features,train_prices)
#预测测试集集中的房价
predict_price=dtr.predict(test_features)
#测试集的结果评价
print('回归树二乘偏差均值：',mean_squared_error(test_prices,predict_price))
print('回归树绝对值偏差均值：',mean_absolute_error(test_prices,predict_price))
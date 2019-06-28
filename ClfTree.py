#encoding=utf-8
from sklearn.model_selection import  train_test_split
from  sklearn.metrics import  accuracy_score
from sklearn.tree import  DecisionTreeClassifier
from sklearn.datasets  import  load_iris

#准备数据集
iris=load_iris()
#获取特征集和分类标识
features=iris.data
labels=iris.target
#随机抽取33%的数据作为测试集，其他为训练集这里的random_state就是为了保证程序每次运行都分割一样的训练集和测试集。否则，同样的算法模型在不同的训练集和测试集上的效果不一样。
train_fratures,test_features,train_labels,test_labels=train_test_split(features,labels,test_size=0.33,random_state=0)
#创建CART分类树sklearn
clf=DecisionTreeClassifier(criterion='gini')
#拟合构造CART分类树
clf=clf.fit(train_fratures,train_labels)
#用cart分类树做预测
test_predict=clf.predict(test_features)
#预测结果与测试集结果作对比
score=accuracy_score(test_labels,test_predict)
print('CART分类树准确率%.3lf'% score)


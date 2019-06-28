#encoding=utf-8
from sklearn.model_selection import  train_test_split
from  sklearn.metrics import  accuracy_score
from sklearn.tree import  DecisionTreeClassifier
from sklearn.datasets  import  load_iris
#决策树可视化
from sklearn.tree import export_graphviz
import graphviz
#准备数据集鸢尾花卉数据
iris=load_iris()
#获取特征集和分类标识
features=iris.data
labels=iris.target
#随机抽取33%的数据作为测试集，其他为训练集这里的random_state就是为了保证程序每次运行都分割一样的训练集和测试集。否则，同样的算法模型在不同的训练集和测试集上的效果不一样。
train_features,test_features,train_labels,test_labels=train_test_split(features,labels,test_size=0.33,random_state=0)
#创建CART分类树sklearn
clf=DecisionTreeClassifier(criterion='gini')
#拟合构造CART分类树
clf=clf.fit(train_features,train_labels)
#用cart分类树做预测
test_predict=clf.predict(test_features)
#预测结果与测试集结果作对比
score=accuracy_score(test_labels,test_predict)
print('CART分类树准确率%.3lf'% score)


from sklearn.datasets import  load_digits
#准备数据集手写数字数据集做分类
digits=load_digits()
#获取分类
features=digits.data
labels=digits.target
#随机抽取33%的数据作为测试集，其他为训练集这里的random_state就是为了保证程序每次运行都分割一样的训练集和测试集。否则，同样的算法模型在不同的训练集和测试集上的效果不一样。
train_features,test_features,train_labels,test_labels=train_test_split(features,labels,test_size=0.33,random_state=0)
#创建CART分类树sklearn
clf=DecisionTreeClassifier(criterion='gini')
#创建拟合分类树
clf=clf.fit(train_features,train_labels)
#用cart分类树做预测
test_predict=clf.predict(test_features)
#对比结果
score=accuracy_score(test_labels,test_predict)
print('手写数字分类树的预测结果：% .4lf' % score)


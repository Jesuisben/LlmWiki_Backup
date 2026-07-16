dataIn, dataOut = './../dataIn/', './../dataOut/'

filename = dataIn + 'pima-indians-diabetes.csv'
import pandas as pd
data=pd.read_csv(filename)
print(data.shape)
print('-'*30)

print(data.columns)
print('-'*30)

label='class' # 정답 관련 컬럼을 머신 러닝에서는 '라벨'이라고 부릅니다
print(data[label].unique())
print('-'*30)

concern=['pregnant', 'plasma', 'pressure', 'thickness', 'insulin', 'bmi', 'pedigree', 'age']
x_data=data[concern]
y_data=data[label]

# 훈련용 데이터와 테스트용 데이터를 70대 30으로 분리합니다.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = \
    train_test_split(x_data, y_data, test_size=0.3)

# 데이터를 표준화 합니다.
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

x_train=scaler.fit_transform(x_train)

x_test=scaler.transform(x_test)

# 로지스틱 회귀에 대한 모델을 구현합니다.
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(x_train, y_train)

# 훈련용 데이터와 테스트용 데이터에 대한 정확도를 확인합니다.
train_score=model.score(x_train, y_train)
print('train accuracy : %.4f' % (train_score))
print('-'*30)

test_score=model.score(x_test, y_test)
print('test accuracy : %.4f' % (test_score))
print('-'*30)

print('학습 이후의 회귀 계수(coefficient) 파악하기')
print('기울기 :', model.coef_)
print('절편 :', model.intercept_)

# 회귀 계수(coefficient) 정보를 시각화 합니다.
import matplotlib
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus']=False

plt.figure()

import numpy as np
from pandas import Series
myseries=Series(np.reshape(model.coef_, -1))
print(myseries)
print('-'*30)

myseries.plot(kind='bar')
plt.title('독립 변수들의 가중치')
# plt.grid(True)
plt.xticks(np.arange(len(concern)), concern, rotation='horizontal')

imagefilename='logisticRegression03_01.png'
plt.savefig(dataOut + imagefilename)
print(imagefilename + ' 파일이 저장됨')

# 성능 평가 지표(정확도, 혼동 행렬 등등)를 확인합니다.
print('test result :')
from sklearn.metrics import confusion_matrix

test_prediction=model.predict(x_test) # 테스트 데이터를 이용한 예측

# 실제 정답과 예측된 값을 이용한 혼동 행렬을 만듭니다.
cf_matrix=confusion_matrix(y_test,test_prediction)
print('confusion_matrix :')
print(cf_matrix)
print('-'*30)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,test_prediction)
print('accuracy : %.4f' % (100*accuracy))
print('-'*30)

from sklearn.metrics import classification_report
cl_report=classification_report(y_test,test_prediction)
print('classification_report :')
print(cl_report)
print('-'*30)

# 혼동 행렬에 대한 히트맵을 그려 봅니다.
import seaborn as sns
plt.figure()

myframe=pd.DataFrame(cf_matrix)
sns.heatmap(myframe, annot=True, cmap='YlGnBu', fmt='g')

plt.title('Confusion Matrix')
plt.xlabel('real')
plt.ylabel('prediction')

imagefilename='logisticRegression03_02.png'
plt.savefig(dataOut + imagefilename)
print(imagefilename + ' 파일 저장됨')
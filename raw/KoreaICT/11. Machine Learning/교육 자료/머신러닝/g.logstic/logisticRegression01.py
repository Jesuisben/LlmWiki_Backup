dataIn, dataOut = './../dataIn/', './../dataout/'
filename = dataIn + 'iris.csv'

import pandas as pd

data = pd.read_csv(filename, header=0)
# print(dataIn.columns)
# print('-'*30)
#
# print(dataIn.shape)
# print('-'*30)

x_label = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
x_data = data[x_label]
y_data = data['Species']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3)

print('before x_train :\n', x_train)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() # 표준화 스케일러 객체

# fit_transform : 평균과 표준 편차를 이용하여 표준화한 다음, 변형 작업을 수행합니다..
x_train = scaler.fit_transform(x_train)

# x_test는 데이터는 x_train에서 학습된 스케일러 객체를 사용해 변환하여 일관된 스케일을 유지하도록 해야 하므로,
# fit을 제외하고 변형(transform) 작업만 수행하도록 해야 합니다.
x_test = scaler.transform(x_test)

# print('after x_train :\n', x_train)

# 모델을 생성합니다.
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
print('train 정확도 : %.3f' % (train_score))
print('-'*30)

test_score = model.score(x_test, y_test)
print('test 정확도 : %.3f' % (test_score))
print('-'*30)

print(type(model.coef_))
print('학습(fit) 이후에 계수 확인')
print('m행 n열 ==> m은 클래스 개수, n은 컬럼 개수')
print('기울기 : \n', model.coef_)
print('-'*30)

print('절편 : ', model.intercept_)
print('-'*30)

# 샘플 데이터와 모델을 사용하여 데이터를 예측해봅니다.
import numpy as np
sample = np.array([[5.0, 3.0, 1.2, 0.1], [6.1, 2.9, 4.3, 1.2], [7.7, 3.0, 6.4, 1.9]])
sample = pd.DataFrame(sample, columns=x_label)
sample = scaler.transform(sample)
print(sample)
print('-'*30)

print('예측값 확인')
prediction = model.predict(sample)
print(prediction)
print('-'*30)

print('확률로 보기')
prediction_proba = model.predict_proba(sample)
print(prediction_proba)
print('-'*30)

print('데이터 별로 최대 값을 가지는 인덱스 찾기')
print(np.argmax(prediction_proba, axis=-1))
print('-'*30)

print('test results :')
# test_prediction : 테스트 데이터를 사용한 예측 결과 정보
test_prediction = model.predict(x_test)

print('confusion matrix :')
from sklearn.metrics import confusion_matrix
cf_matrix = confusion_matrix(y_test, test_prediction)
print(cf_matrix)
print('-'*30)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, test_prediction)
print('정확도 : %.4f' % (100*accuracy))
print('-'*30)

from sklearn.metrics import classification_report
cl_report = classification_report(y_test, test_prediction)
print('클래스 보고서')
print(cl_report)
print('-'*30)

# seaborn 라이브러리는 matplotlib의 서브 라이브러리
import seaborn as sns

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.figure()

# confusion_matrix를 사용하여 히트맵 이미지를 그려 봅니다.
myframe=pd.DataFrame(cf_matrix)
sns.heatmap(myframe, annot=True, cmap='YlGnBu', fmt='g')

plt.title('Confusion Matrix')
plt.xlabel('prediction')
plt.ylabel('real')

imagefilename = dataOut + 'logistic01.png'
plt.savefig(imagefilename)
print(imagefilename + ' 파일 저장됨')

print('finished')
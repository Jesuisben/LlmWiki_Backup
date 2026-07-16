import numpy as np

dataIn, dataOut = './../dataIn/', './../dataOut/'

filename = dataIn +  'titanic.csv'
import pandas as pd
data=pd.read_csv(filename)
print(data.shape)
print('-'*30)

print(data.columns)
print('-'*30)

# survived : 생사 여부 컬럼([0 1])
print(data['survived'].unique())
print('-'*30)

# 코딩 변경 : 적합한 분석을 위하여 데이터를 인위적으로 바꾸는 작업(re-coding)
print(data['sex'].unique())
print('-'*30)

data['sex'] = data['sex'].map({'female':1, 'male':0})

print(data['sex'].unique())
print('-'*30)

# 결측치 처리 : 비어 있는 age 컬럼은 나머지 age의 평균으로 대체하겠습니다.
# data['age'].fillna(value=data['age'].mean(), inplace=True)
data['age'] = data['age'].fillna(data['age'].mean())
print('-'*30)

# 더미 코딩 : 해당 승객이 어떤 클래스(1등석/2등석)에 승선했는 지를 알려 주는 신규 컬럼 생성
print(data['pclass'].unique())
print('-'*30)

# firstclass 컬럼에는 1등석인 경우에만 숫자 1이 들어 갑니다.
# 여기서 숫자 1은 'on'의 개념입니다.
data['firstclass'] = data['pclass'].apply(lambda x:1 if x == 1 else 0 )

# secondclass 컬럼에는 2등석인 경우에만 숫자 1이 들어 갑니다.
data['secondclass'] = data['pclass'].apply(lambda x:1 if x == 2 else 0 )

# 머신 러닝에 사용할 컬럼 : 독립 변수(일등석, 이등석, 성별, 나이), 종속 변수(생존 여부)
concern = ['sex', 'age', 'firstclass', 'secondclass']
x_data = data[concern]
y_data = data['survived']

print('x_data\n', x_data)
print('-'*30)

print('y_data\n', y_data)
print('-'*30)

# 입력과 출력 데이터 셋을 분리합니다.
from sklearn.model_selection import train_test_split
seed = 1234
x_train, x_test, y_train, y_test = \
    train_test_split(x_data, y_data, test_size=0.3, random_state=seed)

# 표준 정규화를 수행합니다.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)

x_test = scaler.transform(x_test)

# 모델을 생성합니다.
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
print('train accuracy : %.4f' % (train_score))
print('-'*30)

test_score = model.score(x_test, y_test)
print('test accuracy : %.4f' % (test_score))
print('-'*30)

print('학습 이후의 회귀 계수 확인')
print('기울기 : \n', model.coef_)
print('절편 : \n', model.intercept_)

# 기울기 :
# ['sex',       'age',      'firstclass', 'secondclass']
# [[ 1.27547829 -0.45986584  0.97211399    0.48698546]]
# 성별과 일등석의 가중치 계수가 크게 나옵니다.
# 이 2개의 컬럼이 생존 여부와 큰 인과 관계를 가진다고 볼 수 있습니다.
# 반면, 나이는 음수가 나오는 데, 연장자일수록 생존 확률이 낮아짐을 의미합니다.

# 가중치 정보를 이용한 시각화
import matplotlib
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus']=False

from pandas import Series
myseries=Series(np.reshape(model.coef_, -1)) # 1차원 Series화
myseries.plot(kind='bar')
plt.title('독립 변수들 가중치(weight)')
plt.xticks(np.arange(len(concern)), concern, rotation='horizontal')
imagefilename='logisticRegression02_01.png'
plt.savefig(dataOut + imagefilename)
print(imagefilename + ' 파일 저장됨')

# 샘플용 데이터로 예측하기
# 'sex', 'age', 'firstclass', 'secondclass' 컬럼 순
soo=np.array([0.0, 20.0, 0.0, 0.0])
hee=np.array([1.0, 17.0, 1.0, 0.0])
minho=np.array([0.0, 32.0, 1.0, 0.0])
sample=np.array([soo, hee, minho])

sample=scaler.transform(sample) # 데이터 정규화

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

imagefilename='logisticRegression02_02.png'
plt.savefig(dataOut + imagefilename)
print(imagefilename + ' 파일 저장됨')

print('finished')
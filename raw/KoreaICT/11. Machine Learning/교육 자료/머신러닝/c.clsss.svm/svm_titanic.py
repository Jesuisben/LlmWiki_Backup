import pandas as pd
import seaborn as sns

# [Step 1] 데이터 준비 - Seaborn에서 제공하는 titanic 데이터 셋 가져 오기
# load_dataset 함수를 사용하여 데이터프레임으로 변환
df = sns.load_dataset('titanic')

# 1은 생존자로써 342명이고, 0은 사망자로써 549명입니다.
print(df['survived'].value_counts())

# [Step 2] 데이터 전처리
print('중복되는 행 개수 : ' + str(sum(df.duplicated())))
print('# 중복이 되는 행은 제거하도록 합니다.')
print('before drop_duplicates : ' + str(len(df)))
df = df.drop_duplicates()
print('after drop_duplicates : ' + str(len(df)))

# 다음 결과를 보면 deck 열(승객이 머물렀던 갑판)에 결측치 데이터가 많습니다.
print('\ndf.info()')
print(df.info())

# 탑승 항구(embarked)와 도시 이름(embark_town) 컬럼은 다음과 같습니다.
# NaN 값이 많은 deck 열과, embarked과 데이터가 겹치는 embark_town 열은 삭제하도록 합니다.
print(df[['embarked', 'embark_town']].head(10))
rdf = df.drop(['deck', 'embark_town'], axis=1)

# how='any' 옵션은 해당 행 또는 열에 결측치가 하나라도 있으면 제거합니다.
rdf = rdf.dropna(subset=['age'], how='any', axis=0)

# 승선 도시(embarked) 컬럼은 범주형 데이터이므로, 범주 데이터 중에서 빈도 수가 가장 많은 항목으로 결측치를 치환하도록 합니다.
# mode() 메소드는 최빈도를 나타내는 항목을 찾아 주는 메소드입니다.
# mode()[0]는 최빈도수가 여러개 나오는 경우 1번째 항목을 선택하겠습니다.
most_frequency = rdf['embarked'].mode()[0]
print(f'most_frequency={most_frequency}')
rdf['embarked'] = rdf['embarked'].fillna(most_frequency)

# [Step 3] 변수 선택
# 분석에 활용할 열(속성)을 선택합니다.
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]

# 원핫 인코딩을 사용하여 범주형 데이터를 모형이 인식할 수 있도록 숫자형으로 변환해 줍니다.
# 이후 female, male 컬럼이 신규로 생성이 됩니다.
'''get_dummies() 함수는 범주형 데이터를 원-핫 인코딩으로 변환합니다.
예를 들어, ndf['sex']가 "male"과 "female"이라는 두 개의 범주 값을 가진다면, get_dummies()는 두 개의 새로운 열을 생성합니다(각각 "male"과 "female").
결과적으로 onehot_sex에는 각 범주에 대해 1과 0의 값을 가지는 데이터프레임이 생성됩니다. 예를 들어, "male"은 [1, 0], "female"은 [0, 1]로 표현됩니다.
python
'''
print('\nbefore ndf.columns')
print(ndf.columns)

onehot_sex = pd.get_dummies(data=ndf['sex'])

# 이후 town_C, town_Q, town_S 컬럼이 신규로 생성이 됩니다.
onehot_embarked = pd.get_dummies(data=ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_sex, onehot_embarked], axis=1)

print('\nafter ndf.columns')
print(ndf.columns)

# 원핫 인코딩에 사용된 컬럼을 제거합니다.
ndf = ndf.drop(['sex', 'embarked'], axis=1)

print('\nndf.info()')
print(ndf.info())

# [Step 4] 데이터셋 구분 - 훈련용(train dataIn)/ 검증용(test dataIn)
# 독립 변수와 종속 변수를 분리합니다.
x = ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male',
       'town_C', 'town_Q', 'town_S']]  # 독립 변수 x
y = ndf['survived']  # 종속 변수 Y(생존 여부)

print('\ny.unique()')
print(y.unique())

# 독립 변수 데이터를 정규화(normalization)시킵니다.
from sklearn import preprocessing

print('\nbefore normalization')
print(x[:5])

scaler = preprocessing.StandardScaler()
x = scaler.fit(x).transform(x)

print('\nafter normalization')
print(x[:5])

# 전체 데이터를 train data와 test data로 7:3 비율로 구분합니다.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)

print(f'train data 개수 : {x_train.shape}')
print(f'test data 개수 : {x_test.shape}')

from collections import Counter

# y_train, y_test의 각 값의 카운트를 출력
train_counter = Counter(y_train)
test_counter = Counter(y_test)

print("y_train 카운트:", train_counter)
print("y_test 카운트:", test_counter)

# [Step 5] svm 분류 모형 - ROC 커브를 그리기 위해 probability=True 옵션 설정
# sklearn 라이브러리에서 svm 분류 모형 가져오기
from sklearn import svm

# 모형 객체 생성 (kernel='rbf' 적용)
# SVC(Support Vector Classification)는 분류 문제에 사용되는 클래스입니다.
# 선형 및 비선형 분류 모두 가능하며, 커널 트릭을 사용하여 복잡한 데이터도 처리할 수 있습니다.
model = svm.SVC(kernel='rbf', probability=True)  # probability=True를 추가

# train data를 가지고 모형 학습
model.fit(x_train, y_train)

# test data를 가지고 y_pred을 예측 (분류)
prediction = model.predict(x_test)

print(type(prediction)) # 넘파이 배열
print(type(y_test)) # 판다스 시리즈

print(prediction[0:10])
print(y_test.values[0:10])

# 분류 모델 성능 평가 
print('\n# 분류 모델 성능 평가(Confusion Matrix)')
from sklearn import metrics  # metrics는 `평가 지표`라는 뜻
svm_matrix = metrics.confusion_matrix(y_test, prediction)
print(svm_matrix)

# 기본 라이브러리 불러오기
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# Confusion Matrix 시각화
plt.figure(figsize=(8, 6))
sns.heatmap(svm_matrix, annot=True, fmt='d', cmap='OrRd',
            xticklabels=['Negative', 'Positive'],
            yticklabels=['Negative', 'Positive'])

plt.title('Confusion Matrix')
plt.ylabel('실제값')
plt.xlabel('예측값')

dataOut = './../dataOut/'

filename = dataOut + 'svm_titanic_image_01.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')

print('# 모형 성능 평가 - 평가 지표 계산')
svm_report = metrics.classification_report(y_test, prediction)
print(svm_report)

# ROC 커브 및 AUC 계산
from sklearn.metrics import roc_curve, auc

# test 데이터에 대한 예측 확률을 계산
# model.predict_proba(x_test) 호출로 각 클래스(0과 1)에 대한 예측 확률을 얻는다.
# [:, 1]을 사용하여 생존(1)일 확률만 선택한다.
  # 생존(1)일 확률
print('클래스별 확률 값 확인')  # 예측 확률을 출력하기 위한 메시지
prediction_probability = model.predict_proba(x_test)
print(prediction_probability[0:3])  # 테스트 데이터의 예측된 생존 확률을 출력

# 생존일 확률 정보만 따로 추출합니다.
alive_probability = prediction_probability[:, 1]


# ROC 커브를 계산하기 위해, 실제 레이블(y_test)와 예측된 확률(alive_probability)을 사용
# fpr: 거짓 긍정 비율, tpr: 진짜 긍정 비율, thresholds: 다양한 임계값을 배열로 반환
fpr, tpr, thresholds = roc_curve(y_test, alive_probability)

# AUC(Area Under the Curve) 계산
# fpr과 tpr을 사용하여 ROC 곡선 아래의 면적을 계산한다.
roc_auc = auc(fpr, tpr)

# ROC 커브 시각화
plt.figure(figsize=(8, 8))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc="lower right")

# 저장 및 출력
filename = dataOut + 'svm_titanic_roc_curve.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')
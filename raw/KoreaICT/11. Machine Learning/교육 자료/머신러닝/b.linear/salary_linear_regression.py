# 기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

# 유니코드 지원
# 이 설정이 False일 경우 유니코드 마이너스 기호가 제대로 표시되지 않음
plt.rcParams['axes.unicode_minus'] = False

# 모든 컬럼을 출력할 수 있도록 옵션 설정
pd.set_option('display.max_columns', None)

import seaborn as sns

# 데이터 셋을 읽어 들입니다.
salary = pd.read_csv('../dataIn/Salary_dataset.csv', index_col=0)


print('\n# 데이터 살펴보기')
print(salary.head())

# [Step 2] 데이터 탐색
print('\n# 데이터 자료형 확인')
'''
실수형 float64(4), 정수형 int64(3), 문자열형 object(2)
'''
print(salary.info())

print('\n# 데이터 통계 요약 정보를 확인합니다.')
# 기본 값으로 수치형 컬럼에 대해서만 보여줍니다.
print(salary.describe())

print('\n# 누락 데이터 확인')
'''결과가 0이면 누락 데이터가 없음'''
print(salary.isnull().sum())

print('\n# 중복 데이터 확인 : ' + str(salary.duplicated().sum()))

# seaborn pairplot : 2 변수간의 관련성을 그림으로 그려 줍니다.
sns.pairplot(salary)
plt.savefig('../dataOut/image01.png')

print('\n# 상관 계수 분석 - 데이터프레임')
corr = salary.corr(numeric_only=True)
print(corr)

print('\n# 상관 계수 분석 - 히트맵')
# 마스크 생성 (상단 트라이 앵글을 숨기고, 하단 절반만 보여 줍니다.)
mask = np.triu(np.ones_like(corr, dtype=bool))

# 히트맵 그리기
plt.figure(figsize=(10, 8))
sns.heatmap(corr, mask=mask, cmap='coolwarm',
            annot=True, fmt=".2f", cbar=True, square=True)
plt.title('변수들간 상관 계수', size=15)
plt.savefig('../dataOut/image02.png')

sns.jointplot(x='YearsExperience', y='Salary', kind='reg', data=salary, line_kws={"color": "red"})
plt.savefig('../dataOut/image03.png')

# Step 4: 데이터셋 구분 - 훈련용(train dataIn)/ 검증용(test dataIn)
# 속성(변수) 선택
x = salary[['YearsExperience']]  #독립 변수 x
y = salary['Salary']       #종속 변수 Y

# train dataIn 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,               #독립 변수
                                                    y,               #종속 변수
                                                    test_size=0.3,   #검증 30%
                                                    random_state=10) #랜덤 추출 값
print('train dataIn 개수: ', len(x_train))
print('test dataIn 개수: ', len(x_test))

# Step 5: 단순 회귀 분석 모델 - sklearn 사용
# sklearn 라이브러리에서 선형 회귀 분석 모듈 가져오기
from sklearn.linear_model import LinearRegression

# 단순회귀분석 모델 객체 생성
lr = LinearRegression()

# train data를 가지고 모델 학습
lr.fit(x_train, y_train)

# 학습을 마친 모델에 test data를 적용하여 결정 계수(R-제곱) 계산
r_square = lr.score(x_test, y_test)
print('R^2 결정 계수 : ', r_square)
'''
설명력: 모델이 종속 변수의 변동 중 약 68.9%를 설명하고 있으며, 이는 비교적 높은 설명력으로 해석될 수 있습니다.
즉, 독립 변수들이 종속 변수의 변동에 상당한 영향을 미치고 있다는 것을 의미합니다.

잔여 변동: 나머지 31.1%의 변동은 모델이 설명하지 못한 부분으로, 이는 독립 변수 이외의 요인들,
데이터의 불확실성, 혹은 모델의 구조적 한계 때문일 수 있습니다.
'''

print('\n# 회귀식의 기울기')
print('기울기 a: ', lr.coef_)

print('\n# 회귀식의 y절편')
print('y절편 b', lr.intercept_)
'''
이 회귀식은 독립 변수와 종속 변수 사이에 음의 상관 관계가 있음을 보여줍니다. 기울기
a=−0.0076554은 독립 변수가 1단위 증가할 때 종속 변수가 약 0.0077 감소함을 의미하며,
y절편 b=46.60은 독립 변수가 0일 때 종속 변수의 예상 값이 46.6임을 나타냅니다.
'''

# 모델에 test dataIn 데이터를 입력하여 예측한 값 y_pred을 실제 값 y와 비교
y_pred = lr.predict(x_test)

# 오차 계산
test_preds = pd.DataFrame(y_test)
test_preds.columns = ['y_test']
test_preds['y_pred'] = y_pred
test_preds['squared_error'] = (test_preds['y_pred'] - test_preds['y_test'])**2
print('test_preds')
print(test_preds)

filename = "../dataOut/test_preds.csv"
test_preds.to_csv(filename, index=False)  # index=False는 인덱스 열을 제거합니다.
print(filename + " CSV 파일이 성공적으로 저장되었습니다.")

mse = test_preds['squared_error'].mean()
print('# 평균 제곱 오차(mse) : ', mse)

# 오차 분석
plt.figure()
# fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# 산점도와 회귀선*실제 값(y_test)과 예측 값(y_pred)의 관계)
# 모델이 실제 값을 얼마나 잘 예측하는지 보여줍니다.
# 실제 직선에 많이 붙어 있는 것이 좋은 것입니다.
sns.regplot(x='y_test', y='y_pred',  data=test_preds, line_kws={"color": "red"});
plt.title('정답과 예측치의 산점도')

plt.tight_layout()
plt.savefig('../dataOut/image04.png')
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dataIn = '../dataIn/'

df = pd.read_csv(dataIn + 'auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceelerations', 'model_year', 'origin', 'name']
print('\n데이터 살펴 보기')
print(df.head())

print('\n데이터 자료형 확인')
print(df.info())

print('\n데이터 통계 정보 요약')
print(df.describe())

print('\n컬럼별 누락 데이터 확인')
print(df.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

dataOut = '../dataOut/'

sns.pairplot(df)
filename = 'pairplot.png'
plt.savefig(dataOut + filename)
print(filename + ' 파일이 저장되었습니다.')

print('\n상관 계수')
corr = df.corr(numeric_only=True)
print(corr)

import numpy as np

plt.figure(figsize=(10, 8))
mask = np.triu(np.ones_like(corr, dtype=bool))

sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt='.2f', cbar=True, square=True)

plt.title('변수들간 상관 계수', size=15)
filname = 'corr_heatmap.png'
plt.savefig(dataOut + filname)
print(f'{filname} 파일 생성됨')

print('\n컬럼 목록')
print(df.columns)

print('\nhorsepower 컬럼의 고유한 값 확인')
print(df['horsepower'].unique())

# 마력이 '?'인 항목 개수 파악
print('\n빈도수 역순으로 조회')
print(df['horsepower'].value_counts())

df['horsepower'] = df['horsepower'].replace('?', np.nan)
df['horsepower'] = df['horsepower'].astype('float')

print('\n데이터 통계 정보 다시 확인')
print(df.describe())

print('\n결측치 제거전 : ' + str(df['horsepower'].isnull().sum()))
df_nan = df.dropna(subset=['horsepower'], axis=0)
print('\n결측치 제거후 : ' + str(df_nan['horsepower'].isnull().sum()))

# 결측치들을 비결측치들의 평균 값으로 대체하도록 합니다.
print('\n결측치 제거전 : ' + str(df['horsepower'].isnull().sum()))
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())
print('\n결측치 제거후 : ' + str(df['horsepower'].isnull().sum()))

print('\n분석에 필요한 열(feature_특성)만 추출하기')
print('연비, 실린더, 마력(출력), 중량')
ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]

print('다중 회귀 분석을 위하여 복사본을 생성합니다.')
multidf = ndf.copy() # 참조 복사가 아닌 값 복사를 수행합니다.

xxx = ndf # 참조 복사


print('\n상관 계수')
corr = ndf.corr(numeric_only=True)
print(corr)

import numpy as np

plt.figure(figsize=(10, 8))
mask = np.triu(np.ones_like(corr, dtype=bool))

sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt='.2f', cbar=True, square=True)

plt.title('변수들간 상관 계수', size=15)
filname = 'corr_heatmap_new.png'
plt.savefig(dataOut + filname)
print(f'{filname} 파일 생성됨')

message = '''
차량 무게(weight)는 연비(mpg)에 음의 상관 계수를 보이고 있습니다.
즉, 차량이 무거울수록 연비가 떨어진다는 것을 파악할 수 있습니다.
'''

print(message)

print('`연비`와 `무게`의 산점도 그래프')
plt.figure(figsize=(10, 8))
sns.scatterplot(data=ndf, x='weight', y='mpg')
plt.title('`연비`와 `무게`의 산점도 그래프', size=15)
filname = 'scatterplot.png'
plt.savefig(dataOut + filname)
print(f'{filname} 파일 생성됨')


# 독립 변수(weight) 1개를 사용하여 종속 변수(mpg)에 대한 단순 회귀 분석 테스트
# 회귀선 표시
plt.figure(figsize=(10, 8))
# kind='reg' : 회귀선(regression line)을 포함해 주세요.
sns.jointplot(data=ndf, x='weight', y='mpg', kind='reg', line_kws={'color':'red'})
filname = 'jointplot.png'
plt.savefig(dataOut + filname)
print(f'{filname} 파일 생성됨')

x = ndf[['weight']] # 독립 변수
y = ndf['mpg'] # 종속 변수

print('독립 변수 및 종속 변수를 7대3 비율로 학습용 데이터 셋과 테스트용 데이터 셋으로 분리합니다.')
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=10)

print(f'학습용 데이터 셋 개수 : {len(x_train)}')
print(f'테스트용 데이터 셋 개수 : {len(x_train)}')

# 단순 회귀 분석 모델 객체 생성
model = LinearRegression()

model.fit(x_train, y_train) # 학습

print('\n회귀 계수 : 회귀 식의 기울기')
print(model.coef_)

print('\n회귀식의 y 절편')
print(model.intercept_)

print('\n수식 표현')
print(f'y = {model.coef_[0]} * x + {model.intercept_}')
'''
이 모델은 독립 변수와 종속 변수 사이에 음의 상관 관계를 가지고 있음을 보여줍니다.
가중치가 -0.0076554은 독립 변수가 1증가할 때, 종속 변수는 대략 0.0076554씩 감소함을 의미합니다.
y 절편 46.60365052224634는 독립 변수의 값이 0일 때 예상되는 종속 변수의 값입니다.
'''

r_square = model.score(x_test, y_test)
print(f'R^2 결정 계수 : {r_square}')
'''
설명력 : 모델이 종속 변수의 변동 중에서 약 68.9%를 설명하고 있습니다.
즉, 독립 변수들이 종속 변수에 상당한 영향력을 미치고 있음을 의미합니다.

잔여 변동 : 나머지 31.1% 정도는 모델이 잘 설명하지 못하는 부분으로, 데이터의 불확실성, 
혹은 모델의 구조적인 한계일 수 있습니다.
'''

# prediction은 머신 러닝이 학습한 모델을 이용하여 예측해준 정보
prediction = model.predict(x_test)

# 오차(잔차) 계산
test_preds = pd.DataFrame()
test_preds['label'] = y_test # 실제 정답 데이터를 의미하는 label
test_preds['prediction'] = prediction # 학습한 모델이 예측해준 정보
# squared_error : (실제정답 - 예측값)의 제곱
test_preds['squared_error'] = (test_preds['label'] - test_preds['prediction']) ** 2

print('\n평균 제곱 오차 데이터 프레임')
print(test_preds.head())

filename = 'test_preds.csv'
test_preds.to_csv(dataOut + filename, index=False)
print(f'{filename} 파일 생성됨')

# 평균 제곱 오차(mean squared error)
mse = test_preds['squared_error'].mean()
print(mse)

print('산점도와 회귀선')
plt.figure(figsize=(10, 10))
sns.regplot(x='label', y='prediction', data=test_preds, line_kws={'color':'red'})
plt.title('정답과 예측 값의 산점도 그래프')
plt.xlim([5, 45])
plt.ylim([5, 45])
filename = 'regplot.png'
plt.savefig(dataOut + filename)
print(filename + ' 파일이 저장되었습니다.')

# 여기서 부터 다중 회귀 분석입니다.
print('multidf.columns')
print(multidf.columns)

# 독립 변수와 종속 변수를 분리
independent_variable = ['cylinders', 'horsepower', 'weight']
x = multidf[independent_variable]
y = multidf['mpg']

# 훈련용 데이터와 테스트용 데이터 분리
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=10)

print(f'훈련용 데이터 형상 : {x_train.shape}')
print(f'테스트용 데이터 형상 : {x_test.shape}')

# 다중 회귀 분석을 위한 모델 생성
multi_model = LinearRegression()

multi_model.fit(x_train, y_train)

r_square = multi_model.score(x_test, y_test)
print(f'R^2 결정 계수 : {r_square}')

slope = multi_model.coef_.tolist()
print(f'기울기 : {slope}')
print(f'y절편 : {multi_model.intercept_}')

# 막대 그래프 그리기
plt.bar(independent_variable, slope)
plt.title('회귀식의 기울기')
plt.xlabel('변수')
plt.ylabel('기울기')
plt.savefig(dataOut + 'independent_variable_slope.png')

prediction = multi_model.predict(x_test)

fig, axes = plt.subplots(1, 3, figsize=(12, 5))

for i, col in enumerate(x_test.columns):
    axes[i].plot(x_train[col], y_train, 'o', label='훈련 데이터')
    axes[i].plot(x_test[col], prediction, 'r+', label='예측값')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('mpg')
    # 범례 위치는 데이터의 분포를 보시고, 적정 위치에 두세요.
    axes[i].legend(loc='best')

plt.suptitle('독립 변수에 따른 종속 변수 산점도', size=15)
plt.savefig(dataOut + 'multivariance_regression.png')

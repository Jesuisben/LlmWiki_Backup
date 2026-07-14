#1. 데이터 수집하기
#
# 1975-2022년 자장면 물가지수
# 2020년 자장면 재료 가격
# 1.1 데이터 수집하기
# 1.2 데이터프레임에 저장하기
import pandas as pd

dataIn = '../dataIn/'

# 물가 지수가 6.079라는 것은 물가가 기준 시점에 비해 약 507.9% 상승했음을 의미합니다.
df = pd.read_csv(dataIn + '자장면소비자물가지수(1975-2022).csv', encoding='cp949')
print('\n# 물가 지수 앞 데이터 일부 확인하기')
print(df.head())

# 2 데이터 탐색과 전처리하기
# 2.1 데이터 둘러보기
print('\n# 데이터 속성 확인하기')
print(df.info())

print('\n# 물가 지수에 대한 통계 값 확인하기')
print(df.describe())

#2.2 데이터 전처리하기
# 2020년도 자장면 재료 가격과 해당 년도의 물가 지수를 이용하여 각 제품들의 가격 정보를 구합니다.
price2020 = [3734, 2032, 1356, 5195]   # 양파, 돼지고기,밀가루, 자장면 가격

# 자장면 재료별 물가지수를 가격 데이터로 변환합니다.
# 2016년도에 돼지 고기의 물가 지수가 91.841 입니다.
# 2020년도의 양파 가격에 곱한 다음 100으로 나누고 소수점 2째자리로 반올림합니다.
df['양파 가격'] = round(df['양파'] * price2020[0]/100,2)
df['돼지고기 가격'] = round(df['돼지고기'] * price2020[1]/100,2)
df['밀가루 가격'] = round(df['밀가루'] * price2020[2]/100,2)
df['자장면 가격'] = round(df['자장면'] * price2020[3]/100,2)

print('\n# 자장면 재료 가격 확인하기')
print(df[41:48])  # 2020년 기준년도의 소비자 물가지수는 100이다

#2.3 탐색적 데이터 분석하기
print('\n# 데이터 프레임의 컬럼 정보 확인')
print(df.columns)

# 데이터 분석에 필요한 컬럼 정보들만 필터링합니다.
concern = ['연도', '양파 가격', '돼지고기 가격', '밀가루 가격', '자장면 가격']
newFrame = df.loc[:, concern]
print('\n# 관심 컬럼만 확인')
print(newFrame.head())

print('\n# 속성간 상관 관계 출력')
print(newFrame.corr())

# 한글 라이브러리 설치하기
# pip install koreanize-matplotlib

dataOut = './../dataOut/'

# 히트맵으로 상관 관계 시각화하기
import koreanize_matplotlib # 그냥 적어 놓으면 됩니다.
import matplotlib.pyplot as plt
import seaborn as sns

sns.heatmap(newFrame.corr(), annot=True, cmap='Greens')   #히트맵 출력
filename = dataOut + 'black_bean_heatmap.png'

plt.tight_layout()  # 여백 자동 조정
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')

# pairplot으로 시각화하기
plt.figure(figsize=(10, 7))
sns.pairplot(newFrame)
filename = dataOut + 'black_bean_pariplot.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')



# 2.4 독립 변수와 종속 변수 선정하기
print('\n# 데이터 프레임의 컬럼 정보 확인')
print(newFrame.columns)

# 자장면 재료 가격 데이터를 x에 저장
x = newFrame.loc[:,['연도', '양파 가격', '돼지고기 가격', '밀가루 가격']]   

y = newFrame.loc[:,'자장면 가격'] # 자장면 가격 데이터를 y 데이터에 저장
print('\nx.head()')
print(x.head())

#2.5 훈련 데이터와 테스트 데이터를 7대3으로 분할합니다.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.3, random_state=42)

#3.모델 생성하기 3.1 모델 학습하기
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

print('\n# 회귀 계수와 y 절편 확인하기')
coff = model.coef_
intercept = model.intercept_
print(f'# 회귀 계수 :')
print(coff)
print(f'# y 절편 : {intercept}')

print('\n# 회귀 계수를 개별로 출력하기')
for idx in range(len(coff)):
    print(f'가중치 w{idx+1} = {coff[idx]:.4f}')
print(f'편향(bias) = {intercept:.4f}')


# 연도를 x1, 양파 가격을 x2, 돼지고기 가격을 x3, 밀가루 가격을 x4라고 할 때 자장면 가격(y)를 예측하는 모델의 식은 다음과 같다.
print('\n모델의 회귀 식')
print(f'y = {model.coef_[0]:.3f} * x1 + {model.coef_[1]:.3f} * x2 + {model.coef_[2]:.3f} * x3 + {model.coef_[3]:.3f} * x4 + {model.intercept_:.3f}')

# 3.3 모델 성능 확인하기
print('\n훈련 데이터로 학습한 모델의 성능(R2):', model.score(x_train, y_train))

# 4. 모델 평가 및 예측하기
# 4.1 모델 성능 평가하기
# 테스트 데이터로 모델 성능 평가
print('테스트 데이터로 모델의 성능(R2) 평가:', model.score(x_test, y_test))

# mean_absolute_error 오차들의 절댓값 합
# mean_squared_error 오차제곱들의 합
# r2_score 결정계수

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
prediction = model.predict(x_test)

print('\nMean squared error :', mean_squared_error(prediction, y_test))
print('Mean absolute error :', mean_absolute_error(prediction, y_test))
print('R2 score : ', r2_score(prediction, y_test))

# 4.2 모델을 예측해 보고, 실제 값과 예측 값을 동시에 출력해 봅니다.

# 실제값과 예측값을 데이터프레임으로 변환
comparison_df = pd.DataFrame({
    '실제값': y_test.reset_index(drop=True),
    '예측값': prediction
})

# MSE와 MAE를 각각 계산하여 컬럼으로 추가
comparison_df['MSE'] = (comparison_df['실제값'] - comparison_df['예측값']) ** 2
comparison_df['MAE'] = abs(comparison_df['실제값'] - comparison_df['예측값'])

# 결과 출력
print('\n실제값/예측값 비교 데이터프레임')
print(comparison_df.head(20))

# MSE와 MAE의 평균값 출력
mean_mse = comparison_df['MSE'].mean()
mean_mae = comparison_df['MAE'].mean()

print(f'\n전체 데이터의 평균 MSE: {mean_mse}')
print(f'전체 데이터의 평균 MAE: {mean_mae}')

# comparison_df를 CSV 파일로 저장
filename = dataOut + 'comparison_results.csv'
comparison_df.to_csv(filename, index=False, encoding='CP949')  # 인덱스 제외, UTF-8 인코딩
print(filename + ' 파일이 저장되었습니다.')

# #5. 모델 활용 문제 해결하기
# 학습된 모델에 신규 데이터를 사용하여 예측해 봅니다.
df_new = pd.read_csv(dataIn + 'new_data.csv', encoding='CP949')
print('\ndf_new')
print(df_new)

print('\n새로운 데이터 예측 값 : ')
print(model.predict(df_new))
import pandas as pd

# 데이터 파일이 위치한 경로를 저장 (상대 경로로 지정)
dataIn, dataOut = './../dataIn/', './../dataOut/'

# auto-mpg.csv 파일을 읽어와 데이터프레임으로 저장
# header=None: 파일에 열 제목이 없으므로 헤더를 직접 지정해야 함
df = pd.read_csv(dataIn + 'auto-mpg.csv', header=None)

# 데이터프레임 열에 대한 이름을 수동으로 지정
# mpg: 마일 당 갤런, cylinders: 실린더 수, displacement: 엔진 배기량,
# horsepower: 마력, weight: 차량 무게, acceleration: 가속 성능,
# model year: 모델 연도, origin: 생산지, name: 자동차 모델 이름
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print('\ndf.head()')
print(df.head())

# Matplotlib 라이브러리 불러오기 (데이터 시각화를 위한 라이브러리)
import matplotlib.pyplot as plt

# 그래프에서 사용할 폰트를 'Malgun Gothic'으로 설정 (한글 지원)
plt.rc('font', family='Malgun Gothic')

# 유니코드 마이너스 기호(−)가 그래프에서 제대로 표시되지 않으면,
# 이를 방지하기 위해 unicode_minus 옵션을 False로 설정
plt.rcParams['axes.unicode_minus'] = False

# 상관 계수 분석을 위한 데이터 출력
print('\n# 상관 계수 분석 - 데이터프레임')

# 상관 계수를 계산하여 corr 변수에 저장 (숫자형 데이터만 사용)
corr = df.corr(numeric_only=True)
print('\ncorr')
print(corr)

# 그래프 크기 지정 (가로 10, 세로 8)
plt.figure(figsize=(10, 8))

# 넘파이와 Seaborn 라이브러리 불러오기
import numpy as np

# 상관 행렬의 상삼각 행렬 마스크 생성 (대칭이므로 절반만 보여줌)
# triu : Upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

import seaborn as sns
# 상관 계수 히트맵 그리기
# mask: 상삼각 부분만 표시하도록 마스크 적용
# cmap: 'coolwarm' 색상 팔레트를 사용하여 상관 계수를 색상으로 표현
# annot=True: 상관 계수 숫자를 셀에 표시
# fmt=".2f": 상관 계수 값을 소수점 두 자리로 표시
# cbar=True: 컬러바 표시
# square=True: 각 셀을 정사각형 모양으로 그리기
sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt=".2f", cbar=True, square=True)

# 그래프 제목을 '변수들간 상관 계수'로 설정, 글자 크기는 15
plt.title('변수들간 상관 계수', size=15)

# 결과 이미지를 PNG 파일로 저장 (경로는 ./../result/image02.png)
filname = 'correlation.png'
plt.savefig(dataOut + filname)
print(f'{filname} 파일 생성됨')

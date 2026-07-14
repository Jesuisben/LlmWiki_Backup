# 기본 라이브러리 불러오기
import pandas as pd  # 데이터 분석을 위한 pandas 라이브러리 불러오기
import matplotlib.pyplot as plt  # 데이터 시각화를 위한 matplotlib 라이브러리 불러오기

# 한글 폰트 설정 및 마이너스 기호 문제 해결
plt.rc('font', family='Malgun Gothic')  # 한글 폰트 설정 (Malgun Gothic)
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지지 않도록 설정

# pandas 출력 옵션 설정 (모든 열을 출력하도록 설정)
pd.set_option('display.max_columns', None)

# [Step 1] 데이터 준비
# 데이터셋 경로 설정 (UCI ML Repository에서 다운로드)
dataIn, dataOut = './../dataIn/', './../dataout/'  # 데이터 입출력 경로 설정
filename = dataIn + 'Wholesale customers data.csv'  # 데이터 파일 경로 설정

# 데이터셋 로드
df = pd.read_csv(filename, header=0)  # CSV 파일을 pandas DataFrame으로 읽어오기

# [Step 2] 데이터 탐색
print('\n# 데이터 살펴 보기')
print(df.head())  # 데이터셋의 첫 5행을 출력하여 데이터의 기본 구조 확인

# 데이터셋에서 분석에 필요한 열만 선택 (Channel과 Region 열 제외)
df = df.iloc[:, 2:]  # 첫 두 열을 제외한 나머지 열 선택

print('\n# 데이터 자료형 확인')
print(df.info())  # 각 열의 데이터 타입 및 null 값의 개수 확인

print('\n# 데이터 통계 요약 정보 확인')
print(df.describe())  # 각 열의 기초 통계량 확인 (평균, 표준편차, 최소/최대값 등)

print('\n# 누락 데이터 확인')
print(df.isnull().sum())  # 각 열의 결측값 개수 확인

print('\n# 중복 데이터 확인')
print(df.duplicated().sum())  # 중복된 행의 수 확인

# [Step 3] 데이터 전처리
print('\n# 분석에 사용할 속성 일부 선택')
x = df.iloc[:, :]  # 데이터의 모든 열을 선택 (x는 독립 변수)

print(x[:5])  # 전처리 전 독립 변수의 첫 5행을 출력

from sklearn import preprocessing  # 데이터 정규화를 위한 sklearn 라이브러리 가져오기
x_std = preprocessing.StandardScaler().fit_transform(x)  # 데이터 표준화 (평균 0, 표준편차 1로 변환)

print('\n# 정규화된 독립 변수 일부 선택')
print(x_std[:5])  # 정규화된 독립 변수의 첫 5행을 출력

# [Step 4] k-means 군집 모형 - sklearn 사용
from sklearn import cluster  # 군집화를 위한 sklearn 라이브러리 가져오기

# KMeans 군집화 모형 객체 생성
# 머신 자체가 n_init번 정도 시뮬레이션을 수행 후, 최적의 중심점 n_clusters을 잡고 시작합니다.
kmeans = cluster.KMeans(init='k-means++', n_clusters=5, n_init=10)  # 군집의 수를 5로 설정, k-means++ 초기화 방법 사용

# 모형 학습
print(kmeans.fit(x_std))  # 모델을 정규화된 데이터에 적합

# 군집 예측
cluster_label = kmeans.labels_  # 각 데이터 포인트의 군집 레이블을 가져옴
print('\n# cluster_label')
print(cluster_label)  # 군집 레이블 출력

# 원본 데이터프레임에 군집 레이블 추가
df['Cluster'] = cluster_label  # 데이터프레임에 'Cluster' 열 추가
print(df.head())  # 군집 레이블이 추가된 데이터프레임의 첫 5행을 출력

print('\n# Cluster 컬럼을 기준으로 그룹화하여 통계 정보 출력')
# 1. Cluster별 각 컬럼의 평균 계산
cluster_means = df.groupby('Cluster').mean()  # 군집별로 각 열의 평균을 계산

print("Cluster별 평균 값:")
print(cluster_means)  # 군집별 평균 값 출력

# 2. 각 열에서 가장 큰 값을 가진 Cluster 찾기
max_value_clusters = cluster_means.idxmax()  # 각 열에서 최대값을 가진 군집 찾기


print("\n열별로 가장 큰 값을 가진 Cluster:")
print(max_value_clusters)  # 열별로 가장 큰 값을 가진 군집 출력

print('\n# 클러스터 값으로 그룹화하고, 그룹별로 내용 출력(head() 함수를 이용하여 몇행만 출력)')
grouped = df.groupby('Cluster')
for group_no, group in grouped:
    print(f'군집 번호 : {group_no}')
    print(f'군집별 데이터 개수 : {len(group)}개')
    print(group.head(10))  # 일부 몇개만 출력
    print('-'*30)
# end for


print('# 그래프로 그리기')

clusters = sorted(df['Cluster'].unique())  # 정렬된 클러스터
colors = [plt.get_cmap('Set1')(i) for i in range(len(clusters))]

fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# 클러스터별 색상 지정
color_dict = {cluster: colors[i] for i, cluster in enumerate(clusters)}

# 왼쪽 영역
for cluster in clusters:
    subset = df[df['Cluster'] == cluster]
    axes[0].scatter(subset['Grocery'], subset['Frozen'], c=[color_dict[cluster]], alpha=0.7, label=f'Cluster {cluster}')
axes[0].set_title('`식료품` vs `냉동 식품`', size=14)

# 오른쪽 영역
for cluster in clusters:
    subset = df[df['Cluster'] == cluster]
    axes[1].scatter(subset['Milk'], subset['Delicassen'], c=[color_dict[cluster]], alpha=0.7, label=f'Cluster {cluster}')
axes[1].set_title('`유제품` vs `조제 식품`', size=14)

plt.suptitle('산점도 그래프', size=17)

import matplotlib.patches as mpatches

# 범례 생성
patches = [mpatches.Patch(color=colors[i], label=f'Cluster {clusters[i]}') for i in range(len(clusters))]

# 왼쪽 및 오른쪽 영역에 범례 추가
axes[0].legend(handles=patches, title="Cluster")
axes[1].legend(handles=patches, title="Cluster")

dataOut = './../dataOut/'
filename = dataOut + 'image01.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')

print('# 그래프로 그리기')
fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# 왼쪽 영역
for cluster in clusters:
    subset = df[df['Cluster'] == cluster]
    axes[0].scatter(subset['Grocery'], subset['Frozen'], c=[color_dict[cluster]], alpha=0.7, label=f'Cluster {cluster}')
axes[0].set_xlim(0, 30000)  # x축 제한 설정
axes[0].set_ylim(0, 20000)  # y축 제한 설정
axes[0].set_title('`식료품` vs `냉동 식품`', size=14)

# 오른쪽 영역
for cluster in clusters:
    subset = df[df['Cluster'] == cluster]
    axes[1].scatter(subset['Milk'], subset['Delicassen'], c=[color_dict[cluster]], alpha=0.7, label=f'Cluster {cluster}')
axes[1].set_xlim(0, 30000)  # x축 제한 설정
axes[1].set_ylim(0, 20000)  # y축 제한 설정
axes[1].set_title('`유제품` vs `조제 식품`', size=14)

plt.suptitle('산점도 그래프', size=17)

# 범례 생성
patches = [mpatches.Patch(color=colors[i], label=f'Cluster {clusters[i]}') for i in range(len(clusters))]

# 왼쪽 및 오른쪽 영역에 범례 추가
axes[0].legend(handles=patches, title="Cluster")
axes[1].legend(handles=patches, title="Cluster")

filename = dataOut + 'image02.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')
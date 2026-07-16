import folium
from sklearn.cluster import dbscan, DBSCAN
from sklearn.preprocessing import StandardScaler

dataIn = './../dataIn/'
filename = dataIn + 'middle_shcool_graduates_report.xlsx'

import pandas as pd
df = pd.read_excel(filename)

print('\n열이름 출력')
print(df.columns.values)

# 디스플레이 옵션 지정
pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

print('\n데이터 살펴 보기')
print(df.head())

print('\n통계 요약 정보 확인')
print(df.describe())

print('\n데이터 자료형 확인')
print(df.info())

school_map = folium.Map(location=[37.55, 126.98], zoom_start=12)

for name, latitude, longitude in zip(df['학교명'], df['위도'], df['경도']):
    folium.CircleMarker(
        location=[latitude, longitude],
        radius=5,
        color='brown', # color circle perimeter
        fill=True,
        fill_color='coral', # fill circle inside
        fill_opacity=0.7,
        popup=name
    ).add_to(school_map)

print(school_map)

dataOut = './../dataOut/'
filename = 'seoul_school_location.html'
school_map.save(dataOut + filename)
print(f'{filename} 파일이 저장되었습니다.')

print('범주형 컬럼들에 대하여 unique한 값의 개수를 파악합니다.')
dummy_list = ['지역', '코드', '유형', '주야']
print('특성별 고유 값 개수 파악')
for feature in dummy_list:
    print(f'{feature} : {df[feature].nunique()}')

print('범주형 컬럼들에 대한 one-hot encoding')
print('dummy_list 목록에 대하여 원핫 인코딩 수행')
df_encoded = pd.get_dummies(df, columns=dummy_list)

print('원본의 컬럼 정보')
print(df.columns)

print('인코딩된 데이터 프레임의 컬럼 정보')
print(df_encoded.columns)

# 집합 연산 공부 : union, intersection, difference
print('신규 생성된 컬럼 정보')
difference = df_encoded.columns.difference(df.columns)
print(difference)

print('군집 분석에서 사용할 컬럼(feature)만 따로 추출합니다.')
train_features = ['과학고', '외고_국제고', '자사고', '자공고', '유형_공립', '유형_국립', '유형_사립']

# 독립 변수 추출하기
x = df_encoded.loc[:, train_features]

print('before normalization')
print(x)

print('독립 변수를 정규화합니다.')
scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x)

print('after normalization')
print(x)

print('머신 러닝 모델 만들기')
# eps : 2개의 샘플이 동일한 클러스터에 속하기 위한 최대 반지름
# min_samples : 하나의 Cluster을 구성하기 위한 최소 데이터의 갯수
dbscan = DBSCAN(eps=0.8, min_samples=5)

dbscan.fit(x) # 모델 학습

cluster_label = dbscan.labels_
print('군집의 예측 값')
print(cluster_label)

df_encoded['Cluster'] = cluster_label

# -1은 어느 그룹에도 속하지 않는 noise point 정보입니다.
print('클러스터별 빈도 수')
print(df_encoded['Cluster'].value_counts())

print('클러스터별로 그룹핑하고, 각 그룹별로 일부 출력')
concern = ['학교명', '과학고', '외고_국제고', '자사고'] # 보고자 하는 열 정보
grouped = df_encoded.groupby('Cluster')
print(type(grouped)) # <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

for group_no, group in grouped :
    print(f'군집 번호 : {group_no}')
    print(f'군집별 데이터 갯수 : {len(group)}개')
    print(group.loc[:, concern].head())
    print('-'*30)
# end for

# 지도에 그리기(클러스터별 색상 구분 지어서)
colors = {-1:'gray', 0:'coral', 1:'blue', 2:'green', 3:'red', 4:'purple', 5:'orange', 6:'brown', 7:'brick', 8:'yellow', 9:'margenta', 10:'cyan', 11:'tan'}

cluster_map = folium.Map(location=[37.55, 126.98], zoom_start=12)

for name, latitude, longitude, cluster in zip(df_encoded['학교명'], df_encoded['위도'], df_encoded['경도'], df_encoded['Cluster']):
    folium.CircleMarker(
        location=[latitude, longitude],
        radius=5,
        color=colors[cluster],
        fill=True,
        fill_color=colors[cluster],
        fill_opacity=0.7,
        popup=name
    ).add_to(cluster_map)

print(cluster_map)

dataOut = './../dataOut/'
filename = 'seoul_school_cluster.html'
cluster_map.save(dataOut + filename)
print(f'{filename} 파일이 저장되었습니다.')







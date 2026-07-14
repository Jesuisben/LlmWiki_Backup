import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean, cosine, pdist, squareform

# 음식을 평가한 데이터 (각 음식은 5가지 속성에 대한 점수를 가집니다)
data = [
    [2, 5, 3, 4, 4],  # 짜장면 (달달함, 목넘김, 고소함, 기름짐, 매콤함 순)
    [2, 4, 3, 3, 5],  # 짬뽕
    [4, 5, 3, 4, 4],  # 라면
    [5, 6, 3, 3, 3],  # 우동
    [4, 1, 3, 2, 2]   # 돈가스
]

# 리스트 형태의 데이터를 numpy 배열로 변환 (계산을 쉽게 하기 위함)
mat = np.array(data)


# 데이터를 pandas DataFrame으로 변환 (행과 열에 레이블을 추가하여 가독성 높임)
# 5개의 음식 정보에 대한 5개의 특성(feature)
myindex = ['짜장면', '짬뽕', '라면', '우동', '돈가스']
mycolumns = ['달달함', '목넘김', '고소함', '기름짐', '매콤함']
df = pd.DataFrame(mat, index=myindex, columns=mycolumns)

print('\nDataFrame Info')
print(df)

# Scipy(Scientific Python)는 파이썬에서 과학적 계산과 수학적 연산을 위한 라이브러리입니다.
from scipy.spatial.distance import euclidean

# 유클리디언 거리 계산 함수 정의
def calculate_euclidean(df):
    # 음식 간 유클리디언 거리를 저장할 빈 데이터프레임 생성
    distances = pd.DataFrame(index=df.index, columns=df.index)
    # 각 음식 쌍에 대해 거리 계산
    for row in df.index:
        for col in df.index:
            # 유클리디언 거리 계산 (값이 작을수록 두 음식이 더 유사함)            
            distances.loc[row, col] = euclidean(df.loc[row], df.loc[col])
             
    return distances

# 유클리디언 거리 계산
euclidean_distances = calculate_euclidean(df)
print(f'유클리디언 거리\n', euclidean_distances)

from scipy.spatial.distance import cosine 

# 코사인 유사도 계산 함수 정의
def calculate_cosine_similarity(df):
    # 음식 간 코사인 유사도를 저장할 빈 데이터프레임 생성
    similarities = pd.DataFrame(index=df.index, columns=df.index)
    # 각 음식 쌍에 대해 코사인 유사도 계산
    for row in df.index:
        for col in df.index:
            # 코사인 거리가 아닌 유사도 계산 (1 - cosine 거리)
            # 두 벡터가 일치할수록 유사도는 1에 가까움            
            similarities.loc[row, col] = 1 - cosine(df.loc[row], df.loc[col])            
    return similarities


# 코사인 유사도 계산
cosine_similarities = calculate_cosine_similarity(df)
print(f'코사인 유사도\n', cosine_similarities)

from scipy.spatial.distance import pdist, squareform

# scipy 라이브러리를 사용하여 유클리디언 거리 계산
# pdist는 한 쌍씩 거리 계산 후, 1차원 벡터로 반환
distances = pdist(data, metric='euclidean')

# 1차원 벡터로 반환된 거리를 거리 행렬로 변환 (대칭 행렬 형태)
distance_matrix = squareform(distances)

# 거리 벡터 출력 (두 음식 간의 거리 정보)
print("\n거리 벡터:")
print(distances)

# 거리 행렬 출력 (음식 간의 거리 행렬로 변환한 결과)
print("\n거리 행렬:")
print(distance_matrix)

# 히트맵 그리기
plt.figure(figsize=(6, 5))
sns.heatmap(distance_matrix, annot=True, cmap='coolwarm', xticklabels=myindex, yticklabels=myindex)
plt.title('음식간 거리 히트맵')

dataOut = './../dataOut/'
plt.savefig(dataOut + 'distance_matrix.png')
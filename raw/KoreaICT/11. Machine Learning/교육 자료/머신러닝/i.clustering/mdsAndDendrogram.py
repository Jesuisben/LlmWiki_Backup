from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist, squareform
from sklearn.manifold import MDS

data = [[2, 5, 3, 4, 4], [2, 4, 3, 3, 5], [4, 5, 3, 4, 4], [5, 6, 3, 3, 3], [4, 1, 3, 2, 2]]

import numpy as np
matrix = np.array(data)

import pandas as pd

mycolumns = ['달달함', '목넘김', '고소함', '기름짐', '매콤함']
myindex = ['짜장면', '짬뽕', '라면', '우동', '돈가스']
df = pd.DataFrame(matrix, index=myindex, columns=mycolumns)

print('데이터 정보')
print(df)

# 유클리디언 거리 알고리즘을 사용하여 거리를 계산 후 1차원 배열로 반환해 줍니다.
distance = pdist(df, metric='euclidean') # 유클리디언 거리
print('거리 정보(1차원 배열)')
print(distance) # 나올 수 있는 경우의 수는 수학에서 '조합' 공부하기

# squareform : 1차원 거리 벡터를 대칭 행렬(2차원) 형태로 변환해 줍니다.
distance_matrix = pd.DataFrame(squareform(distance), index=df.index, columns=df.index)
print('거리 행렬')
print(distance_matrix)

new_distance = distance ** 2
distance_matrix = pd.DataFrame(squareform(new_distance), index=df.index, columns=df.index)
print('거리 행렬')
print(distance_matrix)

linked = linkage(distance, method='single') # 최단 거리 군집화

import matplotlib.pyplot as plt

dataIn, dataOut = './../dataIn/', './../dataOut/'

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 덴드로 그램 그리기
plt.figure(figsize=(8, 4))
plt.title('dendrogram(single linkage)')

dendrogram(linked, labels=df.index.tolist())
plt.savefig(dataOut + 'image01.png')

# 다차원 척도법
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)

mds_fit = mds.fit_transform(squareform(distance))

plt.figure(figsize=(6, 6))
plt.scatter(mds_fit[:, 0], mds_fit[:, 1], color='red')
plt.plot([-2.5, 3], [0, 0], 'k--') # draw x-axia dotted line
plt.plot([0, 0], [-2.5, 3], 'k--') # draw y-axia dotted line

for idx, label in enumerate(df.index):
    plt.text(mds_fit[idx, 0], mds_fit[idx, 1], label, color='red')

plt.title('MDS Plot')

plt.savefig(dataOut + 'mds-plot.png')
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 데이터
X = np.array([
    [3, 3],
    [4, 4],
    [3, 5],
    [5, 4],
    [4, 2],
    [7, 7],
    [8, 8],
    [7, 9],
    [6, 8],
    [8, 7]
])

# 초기 중심점
initial_centers = np.array([
    [4, 5],
    [6, 6]
])

# K-Means 수행
kmeans = KMeans(
    n_clusters=2,
    init=initial_centers,
    n_init=1,
    random_state=42
)

kmeans.fit(X)

# 결과 출력
print("=== 최초 중심점 ===")
for i, center in enumerate(initial_centers):
    print(f"중심점{i}: {center}")

print("\n=== 갱신된 중심점 ===")
for i, center in enumerate(kmeans.cluster_centers_):
    print(f"중심점{i}: {center}")

# --------------------
# 시각화
# --------------------
plt.figure(figsize=(8, 6))

colors = ['royalblue', 'orange']

# 군집별 데이터 표시
for cluster in range(2):
    cluster_points = X[kmeans.labels_ == cluster]

    plt.scatter(
        cluster_points[:, 0],
        cluster_points[:, 1],
        s=120,
        color=colors[cluster],
        label=f'Cluster {cluster}'
    )

# 데이터 번호 표시
for i, point in enumerate(X, start=1):
    plt.text(
        point[0] + 0.1,
        point[1] + 0.1,
        str(i),
        fontsize=10
    )

# 초기 중심점
plt.scatter(
    initial_centers[:, 0],
    initial_centers[:, 1],
    marker='X',
    s=350,
    color='red',
    label='Initial Centers'
)

# 갱신된 중심점
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker='X',
    s=350,
    color='black',
    label='Updated Centers'
)

# 중심점 이동 경로
for old, new in zip(initial_centers, kmeans.cluster_centers_):
    plt.arrow(
        old[0],
        old[1],
        new[0] - old[0],
        new[1] - old[1],
        length_includes_head=True,
        head_width=0.15,
        linestyle='--'
    )

plt.title("K-Means Clustering (K=2)", size=20)
plt.xlabel("x1")
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(0, 11, 1))
plt.ylabel("x2")
plt.grid(True)
plt.legend()
# plt.show()
plt.savefig("../dataOut/" + "kmeans_example.png")
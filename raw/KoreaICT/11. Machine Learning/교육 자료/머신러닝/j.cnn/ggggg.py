import matplotlib.pyplot as plt

# 한글 폰트 설정 및 마이너스 기호 문제 해결
plt.rc('font', family='Malgun Gothic')  # 한글 폰트 설정 (Malgun Gothic)
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지지 않도록 설정

# 데이터 (번호, 키, 몸무게, 성별)
data = [
    (1, 170, 65, '남'),
    (2, 160, 50, '여'),
    (3, 175, 70, '남'),
    (4, 158, 48, '여'),
    (5, 182, 78, '남'),
    (6, 165, 55, '여'),
    (7, 178, 73, '남'),
    (8, 162, 52, '여'),
    (9, 185, 82, '남'),
    (10, 168, 57, '여'),
    (11, 172, 68, '남'),
    (12, 155, 46, '여'),
    (13, 180, 76, '남'),
    (14, 164, 54, '여'),
    (15, 177, 72, '남'),
    (16, 167, 59, '여'),
    (17, 174, 69, '남'),
    (18, 163, 53, '여'),
    (19, 171, 63, '남'),
    (20, 169, 61, '여'),
]

# 새로운 데이터 (21번)
new_point = (21, 170, 65)

# 남/여 분리
male_x = [x for _, x, y, g in data if g == '남']
male_y = [y for _, x, y, g in data if g == '남']

female_x = [x for _, x, y, g in data if g == '여']
female_y = [y for _, x, y, g in data if g == '여']

# 그래프 그리기
plt.figure(figsize=(8, 6))

# 남자 (파란색)
plt.scatter(male_x, male_y, color='blue', label='남')

# 여자 (빨간색)
plt.scatter(female_x, female_y, color='red', label='여')

# 새로운 데이터 (녹색 원)
plt.scatter(new_point[1], new_point[2],
            color='green',
            marker='o',
            s=150,
            label='21번 (미분류)')

# 축 라벨
plt.xlabel('키 (cm)')
plt.ylabel('몸무게 (kg)')
plt.title('KNN 데이터 시각화')

plt.legend()
plt.grid(True)

plt.show()
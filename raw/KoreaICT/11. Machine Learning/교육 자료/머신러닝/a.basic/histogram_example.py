import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

np.random.seed(100)

low, high, bin_size, bindo = 20, 101, 5, 100
korean_scores = np.random.randint(low, high, size=bindo)
print(korean_scores)

# 히스토그램 그리기
mybin = np.arange(low, high, bin_size)
plt.figure(figsize=(10, 6))
plt.hist(korean_scores, bins=mybin, edgecolor='black', alpha=0.7)

# 그래프 설정
plt.title('시험 점수 Histogram')
plt.xlabel( f'계급의 크기 : {bin_size}')
plt.ylabel('빈도수')
plt.xticks(mybin)
plt.yticks(range(11))
# plt.grid(True)

# 히스토그램 표시

dataOut = './../dataOut/'

filename = dataOut + 'histogram.png' # 저장할 파일명 정의
plt.savefig(filename)  # 그래프를 이미지 파일로 저장
print(filename + ' 파일이 저장되었습니다.')  # 파일 저장 완료 메시지 출력

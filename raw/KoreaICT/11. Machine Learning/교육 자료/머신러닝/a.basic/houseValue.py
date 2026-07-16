# matplotlib.pyplot 라이브러리를 plt로 축약하여 import
# 한글 폰트를 사용하기 위해 'Malgun Gothic' 폰트를 설정
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

# x축에 들어갈 데이터로 리스트 형태의 데이터 3개를 생성 (방 개수, 위치, 신축 년도)
x = [[1, 2, 3, 4, 5], [30, 25, 20, 15, 10], [2005, 2010, 2015, 2020, 2024]]
# y축에 해당하는 가격 데이터를 생성
y = [2, 3, 5, 7, 11]

# 1행 3열의 서브플롯(figures)를 생성하고, 전체 크기를 15x5로 설정
# sharey=True로 설정하여 모든 그래프에서 y축을 공유
# sharey=True이면 y축의 레이블을 공유하겠다는 의미
fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

# 각 그래프에 제목을 붙이기 위해 x축 데이터에 대한 설명을 리스트로 작성
xlabels = ['방개수', '위치(도보 시간)', '신축 년도']

# 각 서브플롯에 대해 반복문을 통해 데이터를 시각화
for idx in range(len(xlabels)):
    # idx에 따라 각 서브플롯에 x 데이터와 y 데이터를 그리며, o 마커를 사용
    axs[idx].plot(x[idx], y, marker='o')
    # 각 서브플롯의 제목을 설정 (x축 설명 + '와 가격')
    axs[idx].set_title(xlabels[idx] + '와 가격', size=15)
    # x축 레이블을 설정
    axs[idx].set_xlabel(xlabels[idx], size=12)
    # y축 레이블을 '가격'으로 설정
    axs[idx].set_ylabel('가격')
# end for

# 모든 서브플롯에 대해 y축 값의 범위를 0에서 12로 고정
plt.ylim([0, 12])
# 서브플롯 간 간격을 자동으로 조정하여 레이아웃이 겹치지 않도록 함
plt.tight_layout()

# 그래프를 'hose_value.png' 파일로 저장
dataOut = './../dataOut/'
filename = dataOut + 'house_value.png'
plt.savefig(filename)

print(filename + ' 파일이 저장되었습니다.')

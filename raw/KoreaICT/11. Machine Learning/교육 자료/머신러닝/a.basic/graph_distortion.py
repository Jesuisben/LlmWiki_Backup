import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 5명의 국어 점수 생성 (85점에서 90점 사이)
students = ['김유정', '이민수', '소민기', '윤진혁', '강수연']
korean_scores = [86, 87, 88, 89, 87]

# 서브 플롯 설정 (1행 2열)
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

chart_data = [['skyblue', 0, 100], ['lightgreen', 85, 90]]
for idx in range(2):
    axes[idx].bar(students, korean_scores, color=chart_data[idx][0])
    axes[idx].set_title(f'Korean Scores ({chart_data[idx][1]} to {chart_data[idx][2]})')
    axes[idx].set_xlabel('Students')
    axes[idx].set_ylabel('Scores')
    axes[idx].set_ylim(chart_data[idx][1], chart_data[idx][2])
# end for

# 레이 아웃 조정
plt.tight_layout()
dataOut = './../dataout/'
filename = dataOut + 'pairplot.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')
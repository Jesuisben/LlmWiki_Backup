'''
건강 위험도 예측
다음과 같이 6개의 요소가 있다고 가정합니다.
6개의 요소 중 3개를 랜덤으로 선택하기
'''

from itertools import combinations

elements = ['성별', '나이', '몸무게', '혈압', '흡연 여부', '근육량']
k = 3

combs = list(combinations(elements, k))

print('조합의 개수 : %d' % len(combs))

for comb in combs:
    print(comb)
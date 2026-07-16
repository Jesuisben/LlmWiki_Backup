import numpy as np

# 엔트로피를 구해 주는 함수
def shannon_entropy(probabilities):
    # 주어진 확률 분포의 Shannon 엔트로피를 계산합니다.
    # probabilities (list or numpy array): 사건의 확률을 포함하는 리스트 또는 배열.
    # 주어진 확률 분포의 엔트로피를 반환해 줍니다.

    # 0이 포함된 확률이 있을 경우 로그를 계산할 때 무한대 또는 NaN을 방지하기 위해 필터링합니다.
    probabilities = np.array(probabilities)

    probabilities = probabilities[probabilities > 0]  # 0보다 큰 것만 추출
    print('확률 정보 : ' + str(probabilities))

    # Shannon 엔트로피 계산
    entropy = -np.sum(probabilities * np.log2(probabilities))

    # return entropy
    print(f"엔트로피: {entropy}")
    print()

# end def shannon_entropy(probabilities)


from collections import Counter  # 계수기


# =====================================================
# 범용 분석 함수
# =====================================================
def analyze_ball_list(ball_list, title):
    print('=' * 60)
    print(title)
    print('=' * 60)

    print('ball_list =')
    print(ball_list)
    print()

    # 항목의 빈도 계산
    counter = Counter(ball_list)
    print('counter=' + str(counter))

    total_count = len(ball_list)  # 총 항목 수

    # 각 항목의 비율 계산
    ratios = {
        key: value / total_count
        for key, value in counter.items()
    }

    print('ratios=' + str(ratios))
    print()

    # 결과 출력
    for color, ratio in ratios.items():
        print(f"{color}: {ratio:.5f}")

    probabilities = [value for value in ratios.values()]
    shannon_entropy(probabilities)

# end def analyze_ball_list(ball_list, title)


# =====================================================
# 예제 1
# 기존 예제
# =====================================================
ball_list = [
    'red',
    'red',
    'red',
    'blue',
    'blue',
    'blue',
    'blue'
]

analyze_ball_list(
    ball_list,
    '예제1 : red 3개, blue 4개'
)


# =====================================================
# 예제 2
# 모두 blue인 경우
# 엔트로피가 0이 되는 순수 집합(Pure Set)
# =====================================================
ball_list = [
    'blue',
    'blue',
    'blue',
    'blue',
    'blue',
    'blue',
    'blue'
]

analyze_ball_list(
    ball_list,
    '예제2 : 모두 blue'
)


# =====================================================
# 예제 3
# yellow가 추가된 경우
# =====================================================
ball_list = [
    'red',
    'red',
    'blue',
    'blue',
    'blue',
    'yellow',
    'yellow'
]

analyze_ball_list(
    ball_list,
    '예제3 : red + blue + yellow'
)


# =====================================================
# 예제 4
# red, blue, yellow가 동일 비율
# 엔트로피가 상대적으로 높음
# =====================================================
ball_list = [
    'red',
    'red',
    'blue',
    'blue',
    'yellow',
    'yellow'
]

analyze_ball_list(
    ball_list,
    '예제4 : red, blue, yellow 동일 비율'
)


# =====================================================
# 예제 5
# 4가지 색상
# =====================================================
ball_list = [
    'red',
    'blue',
    'yellow',
    'green',
    'red',
    'blue',
    'yellow',
    'green'
]

analyze_ball_list(
    ball_list,
    '예제5 : red, blue, yellow, green'
)


# =====================================================
# 동전 던지기에서 앞면과 뒷면이 동일한 확률 (50%)로 나올 때의 엔트로피
# =====================================================
probabilities = [0.5, 0.5]
print('=' * 60)
print('동전 던지기')
print('=' * 60)
shannon_entropy(probabilities)


# =====================================================
# 주사위 각 눈금에 대한 확률 정보에 대한 엔트로피
# =====================================================
probabilities = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
print('=' * 60)
print('주사위')
print('=' * 60)
shannon_entropy(probabilities)
'''
2. MLP (다층 퍼셉트론)
MLP는 가장 기본적인 신경망입니다.

예제:
good movie  -> 긍정
bad movie   -> 부정

분류하기
'''

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier

import pandas as pd

# "좋은 영화인지 나쁜 영화인지 문장을 보고 판단하는 간단한 AI를 만드는 예제"
# 데이터
texts = [
    "good movie",
    "great movie",
    "bad movie",
    "terrible movie"
]

labels = [1, 1, 0, 0] # 정답 데이터입니다.

# 문장을 숫자로 변환
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

print('X')
print(X)


# 단어 목록
words = vectorizer.get_feature_names_out()

# DataFrame 생성
df = pd.DataFrame(
    X.toarray(),
    columns=words,
    index=texts
)

print(df)
'''
각 문장을 숫자로 표현

문장	good	great	bad	terrible	movie
good movie	1	0	0	0	1
great movie	0	1	0	0	1
bad movie	0	0	1	0	1
terrible movie	0	0	0	1	1
'''

# MLPClassifier : # MLP(Multi-Layer Perceptron) 알고리즘입니다.
# 입력값을 받아 패턴을 학습하고 결과를 예측하는 인공신경망입니다.
model = MLPClassifier(
    hidden_layer_sizes=(5,), # 은닉층(Hidden Layer)의 뉴런 수입니다.
    max_iter=2000 # 최대 학습 횟수입니다.
)

model.fit(X, labels)

# 예측
y_test = "good film"
test = vectorizer.transform([y_test])

print(f'테스트 데이터 :{y_test}')
print(f'예측 값 : {model.predict(test)}')


'''
4. 마르코프 체인(Markov Chain)

마르코프 체인은 현재 상태만으로 다음 상태를 예측 하는 모델입니다.

예)
오늘 날씨 = 맑음
이면

내일도 맑음일 확률 70%
비 올 확률 20%
흐릴 확률 10%

간단한 텍스트 생성 예제
문장

I like coffee
I like tea
You like coffee
를 학습
'''

import random

corpus = [
    "I like coffee",
    "I like tea",
    "You like coffee"
]

chain = {}

for sentence in corpus:
    words = sentence.split()

    for i in range(len(words)-1):

        current = words[i]
        next_word = words[i+1]

        chain.setdefault(current, [])
        chain[current].append(next_word)

print(chain)

# {'I': ['like', 'like'], 'like': ['coffee', 'tea', 'coffee'], 'You': ['like']}

current = "I"

result = [current]

for _ in range(5):

    if current not in chain:
        break

    current = random.choice(chain[current])
    result.append(current)

print(" ".join(result))

# I like coffee

'''
PPT 한 장 요약
기법	목적	입력	출력
Word2Vec	단어를 벡터로 변환	단어	숫자 벡터
N-gram	단어 패턴 추출	문장	단어 조합
Markov Chain	다음 단어 예측	현재 상태	다음 상태
MLP	분류/예측	특징 벡터	클래스
'''

'''
흐름으로 표현하면 다음과 같습니다.

문장
 ↓
N-gram
 ↓
Word2Vec
 ↓
특징 벡터
 ↓
MLP
 ↓
긍정 / 부정 분류

(전통적인 NLP 파이프라인)

반면

Markov Chain
 ↓
확률 기반 다음 단어 생성

이렇게 설명하면 초보자들도 네 가지 기법의 역할 차이를 쉽게 이해할 수 있습니다.
'''
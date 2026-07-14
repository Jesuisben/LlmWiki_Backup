"""
Word2Vec 학습 + 유사 단어 검색 + 단어 벡터 시각화
"""

from gensim.models import Word2Vec
import matplotlib.pyplot as plt

# ------------------------------
# Word2Vec 학습 데이터
# ------------------------------
sentences = [
    # -------------------------
    # 부모 관련
    # -------------------------
    ["아버지", "부모", "가족", "직장"],
    ["아버지", "부모", "가족", "책임"],
    ["아버지", "부모", "가족", "보호"],

    ["어머니", "부모", "가족", "요리"],
    ["어머니", "부모", "가족", "돌봄"],
    ["어머니", "부모", "가족", "보호"],

    # -------------------------
    # 남녀 관련
    # -------------------------
    ["남자", "사람", "친구", "축구"],
    ["남자", "사람", "친구", "운동"],
    ["남자", "사람", "친구", "회사"],

    ["여자", "사람", "친구", "독서"],
    ["여자", "사람", "친구", "여행"],
    ["여자", "사람", "친구", "회사"],

    # -------------------------
    # 반려동물 관련
    # -------------------------
    ["강아지", "반려동물", "산책", "동물"],
    ["강아지", "반려동물", "귀여운", "동물"],
    ["강아지", "반려동물", "꼬리", "동물"],

    ["고양이", "반려동물", "귀여운", "동물"],
    ["고양이", "반려동물", "야옹", "동물"],
    ["고양이", "반려동물", "수염", "동물"],

    # -------------------------
    # 공통 개념
    # -------------------------
    ["인생", "행복", "사랑"],
    ["인생", "경험", "성장"],
    ["사랑", "행복", "가족"]
]

# ------------------------------
# Word2Vec 모델 학습
# ------------------------------
model = Word2Vec(
    sentences,
    vector_size=2,  # 그래프 출력을 위해 2차원 벡터 사용
    window=2,
    min_count=1,
    workers=1,
    seed=42,
    epochs=300
)

# ------------------------------
# 단어 벡터 출력
# ------------------------------
word_list = ["아버지", "남자", "강아지"]

for word in word_list:
    print(f'\n# {word} 벡터 : {model.wv[word]}')


# ------------------------------
# 유사 단어 찾기
# ------------------------------
for word in word_list:
    print(f'\n# {word}와 유사한 단어')
    print(model.wv.most_similar(word))

# ------------------------------
# 학습된 단어 목록
# ------------------------------
words = model.wv.index_to_key

print('\n# 학습된 단어 목록(가나다순)')

sorted_words = sorted(words)

print(sorted_words)

# ------------------------------
# 한글 폰트 설정
# ------------------------------
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# ------------------------------
# 단어 벡터 시각화
# ------------------------------
plt.figure(figsize=(8, 5))

for word in words:
    x = model.wv[word][0]
    y = model.wv[word][1]

    plt.scatter(x, y, s=100, color='black')

    plt.annotate(
        word,
        (x, y),
        xytext=(0, 10),
        textcoords='offset points',
        ha='center',
        fontsize=12
    )

plt.xlabel("Vector Dimension 1")
plt.ylabel("Vector Dimension 2")
plt.title("Word2Vec Word Vectors")
plt.grid(True)

plt.tight_layout()

dataOut = '../dataOut/'
plt.savefig(dataOut + 'word2vec_test.png')
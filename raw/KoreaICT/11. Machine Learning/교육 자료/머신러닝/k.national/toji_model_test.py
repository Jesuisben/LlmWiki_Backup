import math

from gensim.models import word2vec
from wordcloud import WordCloud

import matplotlib.pyplot as plt

# 소설 '토지' model 파일을 읽어서 특정 단어에 대한 유사도 확인 및 시각화 작업을 진행합니다.

dataOut = '../dataOut/'

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False


def showGraph(keyword, somedata):
    su = len(somedata)  # 전체 데이터 수

    item = [x[0] for x in somedata]  # 축에 보여질 항목 이름들
    count = [x[1] for x in somedata]  # 그려지는 수치 데이터

    plt.figure(figsize=(8, 5))

    plt.title(f'단어 "{keyword}"과(와)의 유사도')

    plt.barh(range(su), count, align='center')

    plt.yticks(range(su), item)

    min_value = min(count)
    max_value = max(count)

    xmin = math.floor(min_value * 10) / 10
    xmax = math.ceil(max_value * 10) / 10

    plt.xlim(xmin, xmax)

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(dataOut + 'word2vec_bar.png')


def showSimiliar(hot_keyword):
    returndata = model.wv.most_similar(
        positive=[hot_keyword]
    )
    return returndata


# 워드클라우드 생성
def saveWordCloud(wordInfo):

    wc = WordCloud(
        font_path="C:/Windows/Fonts/malgun.ttf",
        width=1200,
        height=800,
        background_color="white",
        max_words=100
    ).generate_from_frequencies(wordInfo)

    plt.figure(figsize=(12, 8))

    plt.imshow(wc)

    plt.axis("off")

    plt.title("토지 Word2Vec 워드클라우드")

    plt.tight_layout()

    plt.savefig(dataOut + 'make_wordcloud.png')


# ------------------------------
# Word2Vec 모델 읽기
# ------------------------------

filename = dataOut + 'toji.model'

model = word2vec.Word2Vec.load(filename)

print('파일 로드 완료 :', filename)

# ------------------------------
# 유사 단어 검색
# ------------------------------

keyword = '집'

somedata = showSimiliar(keyword)

print(f'\n# "{keyword}"와 유사한 데이터')

for word, score in somedata:
    print(f'{word} : {score:.4f}')

showGraph(keyword, somedata)

print('파일 word2vec_bar.png 저장 완료')

# ------------------------------
# Word2Vec Vocabulary 빈도 이용
# ------------------------------

wordInfo = {}

for word in model.wv.index_to_key:

    count = model.wv.get_vecattr(
        word,
        'count'
    )

    # 빈도 높은 단어만 사용
    if count > 60 and len(word) >= 2:
        wordInfo[word] = count

# ------------------------------
# 주요 단어 출력
# ------------------------------

print("\n===== 주요 단어 =====")

for word, count in sorted(
        wordInfo.items(),
        key=lambda x: x[1],
        reverse=True):

    print(f"{word}({count})")

# ------------------------------
# 워드클라우드 생성
# ------------------------------

saveWordCloud(wordInfo)

print('파일 make_wordcloud.png 저장 완료')

print("작업 종료")
import math
import sys
import pandas as pd

from konlpy.tag import Komoran

# 코엔엘파이(konlpy)가 자바 경로를 찾습니다.
# 설정할 JAVA_HOME 경로
java_home_path = 'C:\\Users\\ICT02-000\\.jdks\\ms-21.0.10\\bin'

class BayesianFilter:

    def __init__(self):

        self.words = set()
        self.word_dict = {}
        self.category_dict = {}

        try:
            self.komoran = Komoran(
                userdic="../dataIn/user_dic.txt"
            )
            print("사용자 사전 적용")
        except:
            self.komoran = Komoran()
            print("기본 사전 사용")

        print("생성자 호출됨")

    ###################################################
    # 형태소 분석
    ###################################################
    def bayes_split(self, text):

        results = []

        malist = self.komoran.pos(text)

        print(f"\n단어 : {text}")
        print(f"형태소 분석 : {malist}")


        for word, pos in malist:

            # 일반명사
            if pos == "NNG":
                results.append(word)

            # 고유명사
            elif pos == "NNP":
                results.append(word)

            # 영문
            elif pos == "SL":
                results.append(word)

        return results

    ###################################################
    # 학습
    ###################################################
    def fit(self, text, category):

        word_list = self.bayes_split(text)

        for word in word_list:
            self.increase_word(word, category)

        self.increase_category(category)

        # 현재 상태 출력
        print("\n[학습 결과]")
        print(f"문장 : {text}")
        print(f"카테고리 : {category}")

        print("\nword_dict")
        print(self.word_dict)

        print("\nwords")
        print(self.words)

        print("\ncategory_dict")
        print(self.category_dict)

        print("\n" + "=" * 50)

    ###################################################
    # 단어 카운트
    ###################################################
    def increase_word(self, word, category):

        if category not in self.word_dict:
            self.word_dict[category] = {}

        if word not in self.word_dict[category]:
            self.word_dict[category][word] = 0

        self.word_dict[category][word] += 1

        self.words.add(word)

    ###################################################
    # 카테고리 카운트
    ###################################################
    def increase_category(self, category):

        if category not in self.category_dict:
            self.category_dict[category] = 0

        self.category_dict[category] += 1

    ###################################################
    # 카테고리 확률
    ###################################################
    def category_prob(self, category):

        total = sum(self.category_dict.values())

        return self.category_dict[category] / total

    ###################################################
    # 단어 등장 확률
    ###################################################
    def get_word_count(self, word, category):

        if word in self.word_dict[category]:
            return self.word_dict[category][word]

        return 0

    ###################################################
    # 라플라스 스무딩
    ###################################################
    def word_prob(self, word, category):

        n = self.get_word_count(word, category) + 1

        d = (
            sum(self.word_dict[category].values())
            + len(self.words)
        )

        return n / d

    ###################################################
    # 점수 계산
    ###################################################
    def score(self, words, category):

        score = math.log(
            self.category_prob(category)
        )

        for word in words:
            score += math.log(
                self.word_prob(word, category)
            )

        return score

    ###################################################
    # 예측
    ###################################################
    def predict(self, text):

        words = self.bayes_split(text)

        best_category = None
        max_score = -sys.maxsize

        score_list = []

        for category in self.category_dict:

            score = self.score(
                words,
                category
            )

            score_list.append(
                (category, score)
            )

            print(
                f"{category} 점수 = {score:.4f}"
            )

            if score > max_score:
                max_score = score
                best_category = category

        return best_category, score_list


###################################################
# 메인
###################################################

bf = BayesianFilter()

dataIn = "../dataIn/"

df = pd.read_csv(
    dataIn + "mail_data.csv"
)

print("\n===== 학습 시작 =====")

for _, row in df.iterrows():

    bf.fit(
        row["text"],
        row["category"]
    )

print("\n===== 학습 완료 =====")

print("\n등록된 카테고리")
print(bf.category_dict)

print("\n전체 단어 수")
print(len(bf.words))

###################################################
# 테스트
###################################################

test_data = [
    "무료 배송",
    "특가 할인",
    "회의 일정",
    "프로젝트 보고",
    "계약 검토",
    "챗GPT 교육",
    "스프링AI 강의"
]

print("\n단어별 테스트 결과 출력하기")
for text in test_data:
    # print("입력 :", text)

    category, scores = bf.predict(text)

    print("예측 결과 :", category)
    print("점수 :", scores)

    print("-----------------------------------")
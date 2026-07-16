from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier

import pandas as pd

# pd.set_option('display.max_columns', None)

dataIn = '../dataIn/'
# CSV 읽기
df = pd.read_csv(dataIn + "movie_review.csv")

texts = df["text"]
labels = df["label"]

# 문장을 숫자로 변환 (BoW)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# 단어 목록
words = vectorizer.get_feature_names_out()

# DataFrame 생성
df = pd.DataFrame(
    X.toarray(),
    columns=words,
    index=texts
)

print(df)

# MLP 모델
model = MLPClassifier(
    hidden_layer_sizes=(10,),
    max_iter=2000,
    random_state=42
)

# 학습
model.fit(X, labels)

# 테스트 문장 5개
test_sentences = [
    "this movie was fantastic",
    "i really loved this film",
    "the story was boring",
    "this was the worst movie ever",
    "excellent acting and great storyline"
]

test_X = vectorizer.transform(test_sentences)

predictions = model.predict(test_X)

for sentence, pred in zip(test_sentences, predictions):
    result = "Positive" if pred == 1 else "Negative"
    print(f"{sentence} -> {result}")
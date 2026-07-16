 # N-gram 예제

from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "I love machine learning"
]

vectorizer = CountVectorizer(
    ngram_range=(2, 2)
)

X = vectorizer.fit_transform(texts)

print('ngram_range=(2, 2) 결과')
print(vectorizer.get_feature_names_out())

# Bigram을 이용한 감성 분석
texts = [
    "not good",
    "very good",
    "not bad"
]

vectorizer = CountVectorizer(
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(texts)

print('\nngram_range=(1, 2) 결과')
print(vectorizer.get_feature_names_out())
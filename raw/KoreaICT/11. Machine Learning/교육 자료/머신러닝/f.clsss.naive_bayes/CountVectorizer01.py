# 차후에는 파일(csv, txt 형식)을 이용하여 처리해 보도록 할 것
dataIn= '../dataIn/'

myfile = open(dataIn + 'text01.txt', 'r', encoding='UTF-8')
allLines = myfile.readlines()
sentences = [line.strip() for line in allLines]
print('sentences')
print(sentences)
# sentences = ['교육 표준화 일정 프로그래밍', '프로그래밍 창업 친구 일정 운전 운전', '창업 친구 대출']

myfile.close()

# 각각의 단어의 개수를 세어서 BOW로 인코딩한 벡터(vector)를 생성해 줍니다.
from sklearn.feature_extraction.text import CountVectorizer

# df : document frequency(특정 단어가 나타나는 문서의 개수)
# min_df=2 : df >= 2인 단어들만 추출하겠습니다.
vectorizer = CountVectorizer(min_df=1)
# vectorizer = CountVectorizer(min_df=1, stop_words=['광고'])
# vectorizer=CountVectorizer(min_df=1)
print('\ntype(vectorizer)')
print(type(vectorizer))

# fit 함수는 sentences에 대한 학습을 수행하여 단어들에 대한 사전을 만들어 줍니다.
matrix = vectorizer.fit(sentences)
print('\ntype(matrix)')
print(type(matrix))

# vocabulary_ 속성은 단어 사전을 보여 줍니다.
# 단어 별로 '가나다' 순으로 정렬을 수행한 다음, 숫자 색인 번호를 매겨 사전 형식으로 만들어 줍니다.
print('\nmatrix.vocabulary_')
print(matrix.vocabulary_)

print('\n단어 사전들을 정렬하기')
print(sorted(matrix.vocabulary_.items()))

print('\n단어(token) 목록 보기')
feature = vectorizer.get_feature_names_out()
print(type(feature))
print(feature)

print('불용어(stopword) 목록 보기')
print(vectorizer.get_stop_words())

print('# 색인별로 정렬이 된 토큰들에 대한 빈도 수를 출력해 줍니다.')
for data in sentences:
    myarray = vectorizer.transform([data]).toarray()
    # 정렬된 단어 사전 목록과 동시에 같이 보아야 합니다.
    print(data)
    # print(type(myarray))
    print(myarray)
    print('-'*30)
# end for

# [[0 1 1]]
# '창업'라는 단어는 0번, '일정'이라는 단어는 1번, '프로그래밍'이라는 단어는 1번 출력됩니다.
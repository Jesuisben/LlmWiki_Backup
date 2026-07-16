'''
코드 설명
데이터 수집: emails 리스트에 예시로 스팸과 일반 메일 제목을 넣었습니다. 실제 데이터를 사용하면 됩니다.
전처리: Okt를 사용해 한글 텍스트를 토큰화합니다.
벡터화: CountVectorizer를 이용해 텍스트를 숫자 벡터로 변환합니다.
모델 학습: MultinomialNB (Naive Bayes) 모델을 사용해 학습합니다.
예측: 새로운 이메일 제목이 들어오면 해당 제목이 스팸인지 일반 메일인지 예측합니다.
추가 설명
KoNLPy는 한국어 자연어 처리를 돕는 라이브러리입니다. 여기서 사용된 Okt는 자주 쓰이는 형태소 분석기입니다.
CountVectorizer는 텍스트 데이터를 숫자 벡터로 변환하여 머신러닝 모델에 입력할 수 있게 합니다.
MultinomialNB는 텍스트 데이터에 자주 사용되는 나이브 베이즈 모델입니다.
이 코드를 통해 이메일 제목이 스팸인지 여부를 베이지언 필터 방식으로 판별할 수 있습니다. 실제로는 더 많은 데이터를 학습시켜 정확도를 높일 수 있습니다.
'''
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from konlpy.tag import Okt

import pandas as pd

import os

# 코엔엘파이(konlpy)가 자바 경로를 찾습니다.  
# 설정할 JAVA_HOME 경로
# java_home_path = 'C:\\Program Files\\Java\\jdk-12.0.2\\bin'
java_home_path = 'C:\\Users\\ICT02-000\\.jdks\\ms-21.0.10\\bin'

# 환경 변수 설정
os.environ["JAVA_HOME"] = java_home_path

# 환경 변수 확인
print("JAVA_HOME is set to:", os.environ["JAVA_HOME"])

dataIn = './../dataIn/'
dataOut = './../dataOut/'
myframe = pd.read_csv(dataIn + 'mailList.csv')

# emails : 메일 제목과 유형을 tuple 요소로 담고 있는 list
# df.itertuples(index=False)는 데이터프레임의 각 행을 튜플 형태로 반환합니다.
emails = [tuple(row) for row in myframe.itertuples(index=False)]

# 한글 토큰화를 위한 함수
okt = Okt()

# morphs 함수 : 형태소로 나누어 줍니다.
sample = '오늘 일정 확인'
result = okt.morphs(sample)
print('result')
print(result)
print('문자열 결합')
print(' '.join(result))

# token : 작은 절편/조각
# 형태소 분석을 마친 토큰 집합을 하나의 문자열로 결합해 줍니다.
def tokenize(text):
    # 명사만 추출하려면 nouns()를 사용해 주세요.
    return ' '.join(okt.morphs(text))
# end def

# 데이터 전처리 (토큰화)
emails_tokenized = [
    (tokenize(subject), label)
    for subject, label in emails
]

# 데이터 전처리 (토큰화)
print('emails_tokenized')
print(emails_tokenized)


# 이메일 제목과 라벨(일반, 스팸인지)을 분리합니다.
# 변수 emails_tokenized를 unpacking시켜 튜플로 변형해 줍니다.
x, y = zip(*emails_tokenized)

print('x data')
print(x[0:5])

print('y data')
print(y[0:5])

# Bag of Words를 사용하여 텍스트 데이터를 벡터화시킵니다.
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(x)
print('x')
print(x)
print(f'document(sample) size = {x.shape[0]}') # 문서(샘플) 개수
print(f'extracted unique word size = {x.shape[1]}') # 총 단어 개수

'''
<Compressed Sparse Row sparse matrix of dtype 'int64'
	with 439 stored elements and shape (86, 139)>	
  Coords	Values
  (0, 107)	1
  (0, 43)	1
  
   여기서 86은 문서(또는 샘플)의 수를 나타내고, 139는 각 문서에서 추출된 고유한 단어(특징)의 수를 의미합니다.


  Coords	Values
  (0, 107)	1       <-- 0번째 문서에서 107번째 단어가 1번 출현했습니다.    
   
'''

# 학습 데이터와 테스트 데이터를 분리합니다.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Naive Bayes 분류기를 이용하여 데이터를 학습합니다.
# MultinomialNB 클래스는 범주형 데이터에 분류를 위한 `나이브 베이즈` 클래스입니다.
model = MultinomialNB()
model.fit(x_train, y_train)

# 테스트 데이터로 예측
prediction = model.predict(x_test)

# 정확도 출력
score = accuracy_score(y_test, prediction)
print(f'정확도 : {score:.4f}')

# 새로운 이메일에 대하여 어떤 유형의 메일인지 분류해 봅니다.
check_file = open(dataIn + 'checkedMail.csv', mode='r', encoding='UTF-8')
test_mail_list = [onemail.strip() for onemail in check_file.readlines()]

for new_email in test_mail_list :
    print('#'*30)
    new_email_tokenized = tokenize(new_email)
    new_email_vec = vectorizer.transform([new_email_tokenized])
    print('new_email_vec')
    print(new_email_vec)
    prediction = model.predict(new_email_vec)
    print(f"'{prediction[0]}' 메일 : '{new_email}'")
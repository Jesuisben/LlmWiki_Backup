# 기본 라이브러리 불러오기
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 그래프의 폰트를 'Malgun Gothic'으로 설정하여 한글 폰트가 잘 보이도록 함
plt.rc('font', family='Malgun Gothic')
# 그래프에서 음수 기호를 제대로 표시하도록 설정
plt.rcParams['axes.unicode_minus'] = False

# [Step 1] 데이터 준비
# Seaborn에서 제공하는 Titanic 데이터셋을 불러와서 분석을 시작합니다.
# Seaborn의 load_dataset 함수를 사용하여 Titanic 데이터셋을 데이터프레임으로 불러옵니다.
df = sns.load_dataset('titanic')
# 데이터셋의 처음 5개 행을 출력하여 데이터의 구조를 확인합니다.
print('\n# df.head()')
print(df.head())

# [Step 2] 데이터 탐색
# 데이터의 구조와 통계적 특성을 살펴봅니다.

print('\n# 데이터 자료형 확인')
# 각 열의 데이터 자료형을 확인합니다.
print('\n# df.info()')
print(df.info())


print('\n# 데이터 통계 요약 정보 확인')
# 수치형 데이터에 대한 기본적인 통계 요약 정보를 출력합니다.
print(df.describe())

print('\n# 데이터 통계 요약 정보 확인 (범주형)')
# 범주형 데이터에 대한 기본적인 통계 요약 정보를 출력합니다.
print(df.describe(include='object'))

print('\n# 누락 데이터 확인')
# 각 열에 대해 누락된 데이터의 개수를 확인합니다.
print(df.isnull().sum())

print('\n# 중복 데이터 확인')
# 중복된 데이터가 있는지 확인합니다.
print(df.duplicated().sum())

print('\n# 종속 변수')
# 'survived' 열의 값을 카운트하여 생존자와 사망자의 수를 확인합니다.
print(df['survived'].value_counts())

print('\n# 종속 변수 - 시각화')
# 생존 여부에 대한 막대 그래프를 시각화합니다.
ax = sns.countplot(data=df, x='survived')
# x축의 라벨을 '사망'과 '생존'으로 설정합니다.
ax.set_xticks([0, 1])
ax.set_xticklabels(['사망', '생존'])

# 막대 가운데 숫자값 추가
for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x = p.get_x() + width / 2
    y = p.get_y() + height / 2
    ax.annotate(f'{height}', (x, y), ha='center', va='center', color='white', fontsize=12)

plt.title('종속 변수 시각화', size=15)
dataOut = '../dataout/'
plt.savefig(dataOut + 'image01.png')

# 'survived'와 'pclass'별로 'age'의 분포를 시각화합니다.
g = sns.FacetGrid(df, col='survived', row='pclass', hue='sex')
g.map(sns.kdeplot, 'age', alpha=0.5, fill=True)
g.add_legend()
plt.savefig(dataOut + 'image02.png')

# 'sibsp' 열을 기준으로 히스토그램을 시각화합니다. (동반한 형제 또는 배우자의 수)
sns.displot(x='sibsp', kind='hist', hue='survived', data=df, multiple='fill')
plt.savefig(dataOut + 'image03.png')

# 'parch' 열을 기준으로 히스토그램을 시각화합니다. (동반한 부모나 자녀의 수)
sns.displot(data=df, x='parch', kind='hist', hue='survived', multiple='fill')
filename = dataOut + 'histogram.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')

# 'embarked' 열과 'age'의 관계를 시각화하는 박스플롯을 생성합니다.
plt.figure()
sns.boxplot(data=df, x='embarked', y='age', hue='survived')
filename = dataOut + 'boxplot.png'
plt.savefig(filename)
print(filename + ' 파일이 저장되었습니다.')

'''
[Step 3] 데이터 전처리
데이터의 정합성을 높이기 위해 전처리 작업을 수행합니다.
'''

# 중복된 데이터 제거
print('중복 제거 이전: ', df.shape)
df = df.drop_duplicates()
print('중복 제거 이후: ', df.shape)

# NaN값이 많은 'deck' 열과 'embark_town' 열을 삭제합니다.
rdf = df.drop(['deck', 'embark_town'], axis=1)
print(rdf.columns.values)

# 'age' 열에 NaN값이 있는 행을 삭제합니다.
rdf = rdf.dropna(subset=['age'], how='any', axis=0)
print(len(rdf))

# 'embarked' 열의 NaN값을 가장 많이 출현한 값으로 치환합니다.
# 'embarked' 열의 최빈값을 구합니다.
# 방법01 : 범주형 발생 최빈도 구하기
most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
print(most_freq)

# 방법02 : 범주형 발생 최빈도 구하기
most_freq2 = rdf['embarked'].mode()[0]
print(most_freq2)

# 'embarked' 컬럼의 결측치 정보를 최빈도 값으로 치환합니다.
rdf['embarked'] = rdf['embarked'].fillna(most_freq)

# describe 메소드를 활용하여 범주형 변수의 통계적 요약 정보를 출력합니다.
print('\n# 결측치를 최빈값으로 치환 이후')
print('count 행 위주로 확인 요망')
print(rdf.describe(include='object'))

print('\n# 결측치가 있는 지 다시 확인')
print(rdf.isnull().sum())

'''
[Step 4] 변수 선택
분석에 사용할 열(특성)을 선택하고, 범주형 데이터를 원핫 인코딩하여 수치형 데이터로 변환합니다.
'''

# 분석에 사용할 열을 선택합니다.
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head())

# 'sex' 열을 원핫 인코딩하여 수치형 데이터로 변환합니다.
onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

# 'embarked' 열을 원핫 인코딩하여 수치형 데이터로 변환합니다.
onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_embarked], axis=1)

# 원본 열 'sex'와 'embarked'를 제거합니다.
ndf = ndf.drop(['sex', 'embarked'], axis=1)
print(ndf.head())

'''
[Step 5] 데이터셋 구분 - 훈련용(train dataIn)/ 테스트용(test dataIn)
훈련용 데이터와 테스트용 데이터를 분리합니다.
'''

# 독립 변수(x)와 종속 변수(Y)를 정의합니다.
independent_variable = ['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 'town_C', 'town_Q', 'town_S']
x = ndf[independent_variable]
y = ndf['survived']


# 데이터 정규화 : 거리 기반의 알고리즘은 표준화가 필요합니다.
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x) 


# 데이터셋을 훈련용과 테스트용으로 나눕니다 (7:3 비율).
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)

print(f'train data 개수 : {x_train.shape}')
print(f'test data 개수 : {x_test.shape}')

# [Step 6] knn 분류 모형 - sklearn 사용
# knn 분류 모형을 학습시키고 성능을 평가합니다.

# sklearn 라이브러리에서 knn 분류 모형을 가져옵니다.
from sklearn.neighbors import KNeighborsClassifier

# knn 분류 모형 객체를 생성합니다 (k=5로 설정).
knn = KNeighborsClassifier(n_neighbors=5)

# 훈련 데이터를 사용하여 모형을 학습시킵니다.
knn.fit(x_train, y_train)

# 테스트 데이터를 사용하여 예측을 수행합니다.
prediction = knn.predict(x_test)

print('정답 데이터와 예측 데이터를 같이 보기')
bool_result = prediction == y_test

result_frame = pd.DataFrame([prediction, y_test, bool_result])
result_frame = result_frame.T
result_frame.columns = ['예측', '정답', '결과']

print('\n# result_frame.head()')
print(result_frame.head(10))

# 모형의 성능을 평가하기 위해 Confusion Matrix를 계산합니다.
from sklearn import metrics
knn_matrix = metrics.confusion_matrix(y_test, prediction)
print(knn_matrix)

# Confusion Matrix를 시각화합니다.
plt.figure(figsize=(8, 6))
sns.heatmap(knn_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Negative', 'Positive'],
            yticklabels=['Negative', 'Positive'])

plt.title('Confusion Matrix')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.savefig(dataOut + 'image06.png')

# 모형 성능 평가 지표를 계산하여 출력합니다.
knn_report = metrics.classification_report(y_test, prediction)
print(knn_report)
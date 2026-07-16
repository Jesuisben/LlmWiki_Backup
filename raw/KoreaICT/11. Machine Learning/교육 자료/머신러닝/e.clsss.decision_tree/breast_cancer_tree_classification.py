'''
파일을 읽어 들이고, 데이터의 형상을 우선 확인합니다.
데이터 자료형, 통계 요약 정보, 누락 데이터, 중복 데이터 등의 정보를 확인합니다.
종속 변수를 이진 변수로 변환합니다.(2는 benign(양성), 4는 malignant(악성))
각 변수(특성)들에 대하여 히스토그램을 이용한 시각화를 수행합니다.
pairplot() 함수를 사용하여 산점도와 KDE(커널 밀도 추정) 플롯을 그립니다.
bare_nuclei 열에서 '?'을 결측치로 변경 후 행을 삭제합니다.
나머지 문자열을 숫자형으로 변환합니다.
독립 변수 데이터를 정규화시키고 훈련용과 검증용으로 데이터 셋을 7대3으로 분리합니다.
DecisionTreeClassifier 모델을 생성합니다.
'''
# 기본 라이브러리 불러오기
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

import seaborn as sns

# [Step 1] 데이터 준비/ 기본 설정
# Breast Cancer 데이터 셋 가져오기 (출처: UC Irvine Machine Learning Repository)
# https://archive.ics.uci.edu/ 사이트 방문

# uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.dataIn'
dataIn, dataOut = '../dataIn/', '../dataout/'

uci_path = dataIn + 'breast-cancer-wisconsin.data.txt'
df = pd.read_csv(uci_path, index_col='id')

# 이 데이터셋의 열들은 주로 세포학적 특성을 측정하여 종양이 양성인지 악성인지 분류하는 데 사용됩니다.
# 각 열은 암 진단에 중요한 특정 세포학적 특성을 나타내며, class 열은 최종 진단 결과를 나타냅니다.

# 열 이름 지정(이론 문서의 bread cancer 데이터 셋 참조 요망)
# df.columns = ['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
#            'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses', 'class']

print(f'데이터 셋의 크기 : {df.shape}')

# [Step 2] 데이터 탐색

print('\n# 데이터 살펴 보기')
print(df.head())

print('\n# 데이터 자료형 확인')
print(df.info())

print('\n# 데이터 통계 요약 정보 확인')
print(df.describe(include='all'))

print('\n# 누락 데이터 확인')
print(df.isnull().sum())

print('\n# 중복 데이터 확인')
print(df[df.duplicated()])

print('\n# 중복 데이터 개수')
print(df.duplicated().sum())

# 종속 변수를 이진 변수로 변환합니다.(2는 benign(양성), 4는 malignant(악성))
print('\n# 종속 변수 확인')  
print(df['class'].value_counts())

df['class'] = df['class'].map({2:0, 4:1})

print('\n# 종속 변수 확인(비율)') # 0은 양성, 1은 악성 데이터
print(df['class'].value_counts(normalize=True))


# 히스토그램을 이용한 시각화를 수행합니다.
df.hist(figsize=(15, 12));
plt.savefig(dataOut + 'image01.png')

# 여기서부터 코딩 시작

# seaborn pairplot 시각화
# 서로 다른 변수 쌍에 대해 산점도(scatter plot)를 생성하고,
# 동일 변수에는 히스토그램 또는 KDE(커널 밀도 추정) 플롯을 대각선에 배치할 수 있습니다.
df_copy = df.copy() # 원본을 변경하지 않고 복사본을 이용합니다.
df_copy['class'] = df_copy['class'].map({0:'음성', 1:'악성'})
concern = ['clump', 'cell_size', 'cell_shape', 'chromatin','class'] # 관심 컬럼
sns.pairplot(data=df_copy[concern], hue='class')
plt.savefig(dataOut + 'pairplot.png')

# [Step 3] 데이터 전처리

# 중복 데이터 제거
print('중복 제거 이전: ', df.shape)
df = df.drop_duplicates()
print('중복 제거 이후: ', df.shape)


# bare_nuclei : 세포핵이 비어 있는(bare) 핵의 수를 나타내며, 값이 높으면 악성 종양의 가능성이 증가할 수 있습니다.
# bare_nuclei 열을 분석을 위하여 '문자열'대신 '숫자'형으로 변환합니다.
# bare_nuclei 열의 고유값 확인
print('bare_nuclei 열의 고유값: ', df['bare_nuclei'].unique())

print(df['bare_nuclei'].value_counts())

df['bare_nuclei'] = df['bare_nuclei'].replace('?', np.nan)    # '?'을 np.nan으로 변경
df = df.dropna(subset=['bare_nuclei'], axis=0)  # 누락 데이터 행을 삭제
df['bare_nuclei'] = df['bare_nuclei'].astype('int') # 문자열을 숫자형으로 변환

print('\n# 데이터 통계 요약 정보 확인')
print('df.describe()')
print(df.describe())

# [Step 4] 데이터셋 구분 - 훈련용(train dataIn)/ 검증용(test dataIn)
print('\n# 속성(변수) 선택')
train_features = ['clump', 'cell_size', 'cell_shape', 'adhesion', \
                  'epithlial', 'bare_nuclei', 'chromatin', 'normal_nucleoli']

x = df[train_features] # 독립(설명) 변수
y = df['class'] # 종속(예측) 변수_label


# 독립 변수 데이터를 정규화
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x)


# train dataIn 와 test data로 구분(7:3 비율)
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=10)

print(f'\n전체 행 개수 : {len(df)}')
print(f'train 데이터 개수 : {x_train.shape}')
print(f'test 데이터 개수 : {x_test.shape}')


# [Step 5] Decision Tree 분류 모형 - sklearn 사용
# sklearn 라이브러리에서 Decision Tree 분류 모형 가져오기

# 모형 객체 생성 (criterion='entropy' 적용)
# 기준(criterion)을 엔트로피로, 노드의 최대 깊이를 5로 지정합니다.
model = DecisionTreeClassifier(criterion='entropy', max_depth=5)

# train data를 가지고 모형 학습
model.fit(x_train, y_train)

# test data를 가지고 prediction을 예측 (분류)
prediction = model.predict(x_test)

print(prediction[0:10])
print(y_test.values[0:10])

# 모형 성능 평가 - Confusion Matrix 계산
tree_matrix = confusion_matrix(y_test, prediction)
print('tree_matrix')
print(tree_matrix)

# Confusion Matrix 시각화
plt.figure(figsize=(8, 6))
sns.heatmap(tree_matrix, annot=True, fmt='d', cmap='Greens',
            xticklabels=['Negative', 'Positive'],
            yticklabels=['Negative', 'Positive'])

plt.title('Confusion Matrix')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.savefig(dataOut + 'confusion_matrix.png')

# 모형 성능 평가 - 평가 지표 계산
tree_report = classification_report(y_test, prediction)
print(tree_report)



print('\n# 특성 중요도를 큰 값부터 출력합니다.')
print(model.feature_importances_)
print(train_features)

# 위 2개의 변수로 데이터 프레임 만들기
features = pd.DataFrame(model.feature_importances_, index=train_features, columns=['Importance'])
features = features.sort_values(by='Importance', ascending=False)
print(features)

# Importance 컬럼의 가장 큰 값의 색인(index) 찾기
max_index = features['Importance'].idxmax()
print(f'Importance 컬럼에서 가장 중요한 결정 요소 : {max_index}')
print(f'해당 색인의 값 : {features.loc[max_index, "Importance"]}')

print('\n# 특성 중요도에 대한 시각화')
plt.figure(figsize=(10, 6))

sns.barplot(x=features.Importance, y=features.index, hue=features.index, legend=False, palette='viridis')

plt.title('특성 중요도 시각화')
plt.xlabel('Importance')
plt.ylabel('Features')

# 그림 결과를 보면 "세포 크기의 균일성"(cell_size 컬럼)이 악성인지 양성인지 판단하는 가장 중요한 변수로 해석됩니다.
plt.savefig(dataOut + 'barplot.png')

print('\n# 의사 결정 트리 시각화')
plt.figure(figsize=(20, 10))
plot_tree(model,
               feature_names=train_features,
               class_names=['Benign', 'Malignant'],
               filled=True,
               rounded=True,
               fontsize=12)

plt.title('Decision Tree Visualization')
plt.savefig(dataOut + 'image05.png')

# print('model')
# print(model)

#  트리의 구조 정보 출력
print(f"트리의 최대 깊이 : {model.get_depth()}")
print(f"리프 노드 개수 : {model.get_n_leaves()}")

# 2. 트리의 출력
print("하이퍼 파라미터 및 설정 정보 : \n", model.get_params())

# 3. 특성 중요도 출력
print("특성 중요도 출력 :\n", model.feature_importances_)

# 4. 트리의 결정 규칙 출력
# tree.export_text(): 트리의 각 분기 규칙을 텍스트 형태로 출력합니다.
tree_rules = export_text(model, feature_names=train_features)
print(tree_rules)
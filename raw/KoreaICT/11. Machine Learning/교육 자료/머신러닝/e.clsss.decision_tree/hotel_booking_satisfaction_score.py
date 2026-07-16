# 데이터 불러 오기
import pandas as pd

dataIn = '../dataIn/'

df = pd.read_csv(dataIn + 'Europe Hotel Booking Satisfaction Score.csv')
print('df.head()')
print(df.head())

# 탐색적 데이터 분석 및 전처리하기
# 전체적인 데이터 살펴보기
print('\ndf.info()')
print(df.info())

print('\ndf.columns')
print(df.columns)

# 2 결측치 확인하기
print('\ndf.isnull().sum()')
print(df.isnull().sum())

#  호텔 와이파이 서비스 항목 설문조사 빈도수 구하기
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

import seaborn as sns

dataOut = '../dataOut/'

sns.countplot(x='Hotel wifi service', data=df)
plt.savefig(dataOut + 'Hotel wifi service.png')

# 데이터 속성 상관 관계 파악하기
plt.figure(figsize=(15,10))
sns.heatmap(df.iloc[:, 1:].corr(numeric_only=True), annot=True, cmap='Blues')
plt.savefig(dataOut + 'correlation_heatmap.png')

# 특징(feature)과 타겟(target) 설정하기
x = df.iloc[:, 6:16]
y = df.iloc[:, -1]
train_features = x.columns

#  훈련 데이터, 테스트 데이터 분할하기
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y, random_state=42)

print('\n')
print('x_train.shape=' + str((x_train.shape)))
print('y_train.shape=' + str((y_train.shape)))
print('x_test.shape=' + str((x_test.shape)))
print('y_test.shape=' + str((y_test.shape)))

# [3] 모델 생성하기
# 결정트리 모델 학습하기
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

from sklearn.tree import plot_tree
plt.figure(figsize=(20, 10))
TREE_MAX_DEPTH = 2
plot_tree(model, feature_names=x.columns, max_depth=TREE_MAX_DEPTH, filled=True)
plt.savefig(dataOut + 'plot_tree.png')

print('\n# 특성 중요도를 큰 값부터 출력합니다.')
features = pd.DataFrame(model.feature_importances_,
                        index=train_features,
                        columns=['Importance'])
features = features.sort_values(by='Importance', ascending=False)
print(features)

# Importance 컬럼의 가장 큰 값의 색인(index) 찾기
max_index = features['Importance'].idxmax()
print(f'\nImportance 컬럼의 가장 큰 값의 색인 : {max_index}')
print(f'해당 색인의 값 : {features.loc[max_index, "Importance"]}')

print('\n# 특성 중요도 시각화')
plt.figure(figsize=(10, 6))
sns.barplot(x=features.Importance, y=features.index,
            hue=features.index, legend=False,
            palette='viridis')
plt.title('특성 중요도 시각화')
plt.xlabel('Importance')
plt.ylabel('Features')
# 그림 결과를 보면 "세포 크기의 균일성"(cell_size 컬럼)이 악성인지 양성인지 판단하는 가장 중요한 변수로 해석됩니다.
plt.savefig(dataOut + 'n_features.png')

print("\n훈련 데이터를 이용한 모델 분류 정확도 : ", model.score(x_train, y_train))

# [4] 모델 평가 및 예측하기
# 모델 평가하기
print("테스트 데이터 성능평가 : ", model.score(x_test, y_test))

#  테스트 데이터 예측하기
prediction = model.predict(x_test)
print(prediction[:5])
print(y_test[:5])

from sklearn.metrics import confusion_matrix

prediction = model.predict(x_test)
conf_matrix = confusion_matrix(y_test, prediction)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='d')
plt.title('Hotel satisfaction classification')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig(dataOut + 'confusion_matrix.png')

# [5] 모델 활용하기
# 5.1 새로운 데이터프레임 생성하기
df_new = pd.read_csv(dataIn + 'hotel_satisfaction_new.csv')
print('\ndf_new.head()')
print(df_new.head())

# 5.2 새로운 데이터 예측하기
print('\nmodel.predict(df_new)')
print(model.predict(df_new))

from sklearn.tree import export_text
tree_rules = export_text(model, feature_names=x.columns, max_depth=TREE_MAX_DEPTH)
print('\ntree_rules')
print(tree_rules)
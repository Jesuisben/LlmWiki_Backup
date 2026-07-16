import pandas as pd

dataIn, dataOut = '../dataIn/', '../dataOut/'

filename = dataIn + 'likelyhood.csv'



myframe = pd.read_csv(filename)

x = myframe[['muscle', 'height', 'grade', 'speech', 'book', 'travel', 'skin']]
print('x[:10]')
print(x[:10])

y = myframe[['likelyhood']]
print('y[:10]')
print(y[:10])

# print(y.head())
print(y.value_counts())

# print(y.unique())

# 각 컬럼들의 데이터 분포 확인
print(x.describe())

# 데이터 들의 분포가 너무 크므로, 정규화가 필요합니다.
def min_max_normalization(lst):
    normalized = []

    for value in lst :
        normalized_num = (value-min(lst))/(max(lst)-min(lst))
        normalized.append(normalized_num)

    return normalized
    # end for

for col in x.columns:
    # print(x[col])
    x.loc[:, col] = min_max_normalization(x[col])
    x[col] = x[col].astype(float)
    # x[col] = min_max_normalization(x[col])

print(x.describe())

# 데이터 셋 분리하기
from sklearn.model_selection import train_test_split
# train_data, test_data, train_labels, test_labels = train_test_split(x, y, test_size=0.2, random_state=100)
train_data, test_data, train_labels, test_labels = train_test_split(x, y, test_size=0.3)

print('학습용 데이터 개수 : %d' % len(train_data))
print('테스트용 데이터 개수 : %d' % len(test_data))
print('학습용 데이터 label : %d' % len(train_labels))
print('테스트용 데이터 label : %d' % len(test_labels))

# 모델 생성하기
from sklearn.neighbors import KNeighborsClassifier

neighbors_count = 3
classifier = KNeighborsClassifier(n_neighbors=neighbors_count)

train_labels = train_labels.values.ravel()
classifier.fit(train_data, train_labels)

scores = classifier.score(test_data, test_labels)
print('scores : %.2f' % scores)

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

k_list = range(1, 4)
accuracies = []

for k in k_list :
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(train_data, train_labels)
    accuracies.append(classifier.score(test_data, test_labels))

plt.plot(k_list, accuracies)
plt.xlabel='k'
plt.ylabel='Test Accuracy'
plt.title='Likelyhood Classifier Accuracy'
plt.savefig(dataOut + 'image01.png')


# Predicting the Test set results
y_pred = classifier.predict(test_data)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(test_labels, y_pred)
print('cm')
print(cm)

import seaborn as sns

myframe=pd.DataFrame(cm)
sns.heatmap(myframe, annot=True, cmap='YlGnBu', fmt='g')

plt.savefig(dataOut + 'image02.png')
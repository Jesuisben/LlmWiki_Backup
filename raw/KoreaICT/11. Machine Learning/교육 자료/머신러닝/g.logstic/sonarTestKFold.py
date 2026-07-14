import pandas as pd

dataIn = './../dataIn/'
filename = dataIn + 'surgeryTest.csv'

df = pd.read_csv(filename, header=None)

data = df.values 
table_col = data.shape[1]

y_column = 1
x_column = table_col - y_column

x = data[:, 0:x_column].astype(float)
y_raw = data[:, x_column:].ravel() #  'R' 또는 'M' 중에서 한개의 값

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(y_raw)
y = le.transform(y_raw).astype(float)

n_fold = 10 # 교차할  겹의 갯수
seed = 0 # 랜덤 시드값

from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)

cost = [] # for loss value(손실 함수)
accuracy = [] # for accuracy(정확도)

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers.core import Dense

print('반복문을 실행 중입니다.')
cnt = 0 # 카운터 변수
for train, test in skf.split(x, y):
    cnt += 1    
    print(str(cnt) + '번째 실행중...')
    model = Sequential()
    model.add(Dense(units=24, input_dim=x_column, activation='relu'))
    model.add(Dense(units=10, activation='relu'))
    model.add(Dense(units=y_column, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    # x[train], y[train]는 이번 순번에서 실습할 훈련용 데이터 셋을 의미합니다.
    model.fit(x[train], y[train], epochs=200, batch_size=5, verbose=0)

    # 학습 완료 후 테스트 데이터를 이용하여 평가를 진행합니다.
    score = model.evaluate(x[test], y[test], verbose=0)
    
    cost.append( score[0] )
    accuracy.append( score[1] )
# end for

print('손실 함수')
print(cost)
print('-'*30)

print('손실 함수의 평균')
print('%.3f' % (sum(cost)/n_fold))
print('-'*30)

print('정확도')
print(accuracy)
print('-'*30)

print('정확도의 평균')
print('%.3f' % (sum(accuracy)/n_fold))
print('-'*30)

print('finished')


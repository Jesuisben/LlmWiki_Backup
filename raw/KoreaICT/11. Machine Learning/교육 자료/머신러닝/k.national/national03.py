'''
Keras 버전
'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# 입력 데이터
X = np.array([
    [1,0],
    [1,1],
    [0,1],
    [0,0]
])

y = np.array([1,1,0,0])

model = Sequential([
    Dense(4, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(X, y, epochs=100, verbose=0)

print(model.predict(X))
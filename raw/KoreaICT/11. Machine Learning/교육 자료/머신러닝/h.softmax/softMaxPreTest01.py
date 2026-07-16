x=[2.0, 1.0, 0.1]
y=[] # 지수 함수의 연산 결과를 저장합니다.

import numpy as np
for idx in range(len(x)):
    y.append(np.exp(x[idx]))

mysum=np.sum(y)
print('총합 : ', mysum)

prop_total=0.0 # 확률의 총합을 저장할 변수
prop_data=[]
for idx in range(len(y)):
    prop=y[idx]/mysum
    prop_total += prop
    prop_data.append(prop)
    print('%f, %f' % (x[idx], prop))

print('확률의 총합 : %f' % (prop_total))

# 가장 큰 값을 저장하고 있는 인덱스 찾기
arr=np.array(x)
print(type(arr))

# argmax : argument matrix
maxidx=np.argmax(arr)
print('최대 값을 가지고 있는 인덱스 번호 :', str(maxidx))

import matplotlib.pyplot as plt

plt.pie(prop_data, labels=prop_data, shadow=False, startangle=90, normalize=False)
imagefilename='softMaxPreTest01_image.png'

dataIn = '../dataIn/'
dataOut = '../dataOut/'

plt.savefig(dataOut + imagefilename)

print(imagefilename + ' 파일 저장됨')
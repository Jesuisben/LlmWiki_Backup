import numpy as np

x=[26, 28, 30, 32]
y=[148, 164, 168, 183]

def predict(x):
    return 6 * x + 10

def rmse(predict, ylabel):
    # predict : 예측 값, ylabel : 정답 데이터
    pred=np.array(predict)
    ylabel=np.array(ylabel)

    result=((pred-ylabel)**2).mean()
    result=np.sqrt(result)
    return result

predict_result=[] # 예측 값 리스트

# 모든 x값을 한 번씩 대입하여 predict_result 리스트완성.
for idx in range(len(x)):
    predict_result.append(predict(x[idx]))
    print('입력 : %f'%(x[idx]))
    print('출력 : %f'%(y[idx]))
    print('예측 : %f'%(predict(x[idx])))
    print('-' * 40)

print('rmse 최종값 : ' + str(rmse(predict_result, y)))

print ((324+196+484+361)/4)
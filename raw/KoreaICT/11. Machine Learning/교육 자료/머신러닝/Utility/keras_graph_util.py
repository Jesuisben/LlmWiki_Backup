import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

import pandas as pd
import numpy as np

dataOut = './../dataOut/'

def make_graph_probability(nrow, ncol, prediction, true_label, image, class_names, file_name):
    '''
    :param nrow, ncol: 서브 플롯팅 행/열 개수
    :param prediction: 예측 확률을 저장하고 있는 배열
    :param true_label: 실제 정답 데이터
    :param image : 그리고자 하는 이미지 배열
    :param class_names: 정답(label) 데이터의 품목 이름(string)
    :param file_name : 결과물을 저장할 파일 이름
    :return:
    '''
    plt.figure(figsize=(2*2*nrow, 2*ncol))

    for idx in range(nrow * ncol):
        prediction_label = np.argmax(prediction[idx])  # 예측된 값
        if prediction_label == true_label[idx]:  # 맟춘 경우 파랑색으로 그리기
            mycolor = 'blue'
        else:
            mycolor = 'red'
        # end if

        # 이미지 그리기
        plt.subplot(nrow, 2*ncol, 2*idx+1)
        plt.xticks([])
        plt.yticks([])
        plt.axis('on')
        plt.imshow(image[idx], cmap=plt.cm.binary)  # 이미지 그리기

        # 이미지 하단의 라벨 형식은 '예측값 확률%(정답)'입니다.
        pred_caption = class_names[prediction_label]  # 예측값
        prob = 100.0 * np.max(prediction[idx])  # 확률값
        answer = class_names[true_label[idx]]  # 정답
        plt.xlabel("{} {:6.2f}% ({})".format(pred_caption, prob, answer), color=mycolor)

        # 확률 그래프 그리기
        plt.subplot(nrow, 2 * ncol, 2 * idx + 2)
        plt.xticks([])
        plt.yticks([])
        thisplot = plt.bar(range(10), prediction[idx], color='#777777')
        plt.ylim([0.0, 1.0])
        thisplot[prediction_label].set_color('red') # 예측이 틀림(빨강)
        thisplot[true_label[idx]].set_color('blue')  # 예측이 맞음(파랑)

        plt.tight_layout()
        plt.axis('on')
    # end for

    filename = dataOut + file_name + ''
    plt.savefig(filename)
    print(filename + ' 파일이 저장되었습니다.')
# end def make_graph_probability



def result_dataframe(prediction, y_test, file_name):
    # 예측 확률을 이용하여, 예측치와 정답을 DataFrame으로 만들어 줍니다.
    '''
    :param prediction: 예측 확률 정보를 담고 있는 2차원 배열 (행: 샘플, 열: 클래스)
    :param y_test: 정답 데이터
    :return: DataFrame (예측 확률, 예측 값, 정답을 담은 데이터프레임)
    '''
    # 예측 확률이 가장 높은 값을 기준으로 예측 값을 생성
    pred_value = np.argmax(prediction, axis=-1)
    print(pred_value)

    # 예측 확률 배열을 샘플별로 유지한 상태로 전치(transpose)
    prediction_flat = pd.DataFrame(prediction)
    print(prediction_flat)

    # 예측 값과 정답을 DataFrame으로 변환
    df = pd.DataFrame({
        '예측': pred_value,
        '정답': y_test
    })

    # 예측 확률을 샘플별로 열에 추가
    for i in range(len(prediction_flat.columns)):
        df[f'확률_{i}'] = prediction_flat[i]

    print(df)

    df.to_csv(dataOut + file_name, index=False, encoding='CP949')
    # df.to_csv(dataOut + file_name, index=False, encoding='UTF-8')

    print(file_name + ' 파일이 저장되었습니다.')
    # return df
# end def result_dataframe

def plot_gray_image(chart_data, labels, num_rows, num_cols, file_name, class_names):
    # 넘겨 받은 행과 열 정보를 이용하여 서브 플롯팅을 해줍니다.
    '''
    :param chart_data: 그리고자 하는 이미지 정보
    :param labels: 정답 데이터
    :param num_rows: 서브 플롯팅을 위한 행 개수
    :param num_cols: 서브 플롯팅을 위한 열 개수
    :param file_name: 저자될 이미지 파일 이름
    :param class_names: 정답(label) 데이터의 품목 이름(string)
    :return: None
    '''
    plt.figure(figsize=(10, 10))
    plt.grid(False)
    plt.axis('off')
    plt.tight_layout()

    for idx in range(num_rows * num_cols):
        # num_rows 행 num_cols 열의 (idx+1) 번째 cell에 그리겠습니다.
        plt.subplot(num_rows, num_cols, (idx+1))
        plt.xticks([])
        plt.yticks([])
        plt.imshow(chart_data[idx], cmap=plt.cm.binary) # 흑백으로 그리기
        plt.xlabel(class_names[labels[idx]])
    # end for

    filename = dataOut + file_name + ''
    plt.savefig(filename)
    print(filename + ' 파일이 저장되었습니다.')
# end def plot_gray_image

def graph_accuracy_validation(fit_hist, file_name):
    # fit() 메소드 실행 결과를 이용하여 accuracy와 검증용 accuracy를 그래프로 그려 줍니다.
    accuracy = fit_hist.history['accuracy'] # accuracy
    val_accuracy = fit_hist.history['val_accuracy'] # validation accuracy

    plt.figure()

    plt.plot(accuracy, 'b--', label='accuracy')
    plt.plot(val_accuracy, 'r--', label='val_accuracy')
    plt.legend()
    plt.title('epoch에 따른 정확도 정보', size=15)

    filename = dataOut + file_name + '.png'
    plt.savefig(filename)
    print(filename + ' 파일이 저장되었습니다.')
# end def graph_accuracy_validation

def graph_loss_validation(fit_hist, file_name):
    # fit() 메소드 실행 결과를 이용하여 손실 함수와 검증용 손실 함수를 그래프로 그려 줍니다.
    loss = fit_hist.history['loss'] # 손실 함수

    # fit() 함수의 validation_split 매개 변수와 관련이 있습니다.
    val_loss = fit_hist.history['val_loss'] # 검증용 손실 함수

    plt.figure()

    plt.plot(loss, 'b--', label='loss')
    plt.plot(val_loss, 'r--', label='val_loss')
    plt.legend()
    plt.title('epoch에 따른 손실 정보', size=15)

    filename = dataOut + file_name + '.png'
    plt.savefig(filename)
    print(filename + ' 파일이 저장되었습니다.')
# end def graph_loss_validation

def graph_accuracy_loss(fit_hist, file_name, fig_size=(8, 6)):
    # fit_history 객체 정보를 이용하여 손실 함수와 정확도에 대한 그래프를 그려 줍니다.
    # fit_hist : fit_history 객체, filename : 저장될 파일 이름, fig_size : 그림 크기

    # loss_values : 매 epoch마다 추출된 `손실 함수`의 결과를 저장하고 있습니다.
    loss_values = fit_hist.history['loss']
    print('\n손실 함수 데이터')
    print(loss_values)

    # accuracy_values : 매 epoch마다 추출된 `정확도`의 결과를 저장하고 있습니다.
    accuracy_values = fit_hist.history['accuracy']
    print('\n정확도 데이터')
    print(accuracy_values)

    # 그래프 그리기
    plt.figure(figsize=fig_size)
    epochs = range(1, len(loss_values) + 1)  # x축 눈금

    # 좌측 손실 함수 그래프
    plt.subplot(1, 2, 1)
    plt.plot(epochs, loss_values, 'ro', label='training loss')
    plt.title('훈련시 손실 그래프')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend() # plot() 함수의 label 매개 변수와 연관 있음

    # 우측 정확도 그래프
    plt.subplot(1, 2, 2)
    plt.plot(epochs, accuracy_values, 'bo', label='training accuracy')
    plt.title('훈련시 정확도 그래프')
    plt.xlabel('epochs')
    plt.ylabel('accuracy')
    plt.legend()

    filename = dataOut + file_name + '.png'
    plt.savefig(filename)
    print(filename + ' 파일이 저장되었습니다.')
# end def graph_accuracy_loss

def model_information(model):
    # 해당 모델의 여러 가지 정보를 출력합니다.
    print(f'\ninput layer : {model.inputs}')
    print(f'\noutput layer : {model.outputs}')
    print(f'\nlayers info : {model.layers}')

    print(f'\nmodel summary : ')
    model.summary()

    # compile() 함수의 metrics 매개 변수와 관련이 있습니다.
    print(f'\n평가 지표 : {model.metrics_names}')
# def model_information


import numpy as np
import os, shutil # shell utility
from tqdm import tqdm

print('파일을 복사합니다... 잠시만 기다려 주세요.')

# 원본 이미지 파일이 들어 있는 폴더(강아지와 고양이 각 2,000개 이미지)
originalDataFolder = r'..\datasets\cats_and_dogs'

# 훈련용, 검증용, 테스트용 폴더의 상위 폴더
targetFolder = r'..\datasets\cats_and_dogs_random'

if os.path.exists(targetFolder):
    # 해당 폴더가 이미 존재하는 경우 하위 폴더 및 파일 모두를 삭제합니다.
    shutil.rmtree(targetFolder)
# end if

os.mkdir(targetFolder) # 해당 폴더 생성

upperFolder = ['train', 'validation', 'test']  # 상위 폴더
lowerFolder = ['cats', 'dogs']  # 하위 폴더

# 각각의 용도에 맞는 이미지 추출 인덱스의 범위를 저장하고 있는 사전
rangeDict = {'train':(0, 1000), 'validation':(1000, 1500), 'test':(1500, 2000)}

image_size = 2000 # 강아지/고양이 각각의 이미지 개수
animalRandom = np.random.permutation(image_size)
# print(animalRandom)

# 훈련용, 검증용, 테스트용 데이터를 위한 하위 폴더를 생성합니다.
for upp in upperFolder:
    uppFolderPath = os.path.join(targetFolder, upp)
    os.mkdir(uppFolderPath)  # 상위 폴더 만들기

    # 강아지와 고양이를 위한 각각의 폴더 생성
    for low in lowerFolder:
        lowFolderPath = os.path.join(uppFolderPath, low)
        os.mkdir(lowFolderPath)  # 하위 폴더 만들기

        minRange = rangeDict[upp][0]  # 추출할 이미지 하한 인덱스
        maxRange = rangeDict[upp][1]  # 추출할 이미지 상한 인덱스

        # 주의 : animalRandom 항목이 range()가 아니고 numpy이므로 슬라이싱 기법으로 추출해야 합니다.
        # low[0:len(low) - len('s') : 폴더 이름에서 끝 's' 글자 떼어 내기
        fileName = [low[0:len(low)-len('s')] + '.{}.jpg'.format(idx) for idx in animalRandom[minRange:maxRange]]
        # print(fileName)

        print('\n' + lowFolderPath + ' 폴더에 파일을 복사 중입니다.')
        for fname in tqdm(fileName):
            source = os.path.join(originalDataFolder, fname)
            destination = os.path.join(lowFolderPath, fname)
            shutil.copyfile(source, destination)
    # end inner for
# end outer for

print('각 폴더 내의 파일 개수 확인')
for upp in upperFolder:
    uppFolderPath = os.path.join(targetFolder, upp)

    for low in lowerFolder:
        lowFolderPath = os.path.join(uppFolderPath, low)
        files = os.listdir(lowFolderPath)
        print(upp + '\\' + low + ' 폴더 내 파일 개수 : ' + str(len(files)))
    # end inner for
# end outer for
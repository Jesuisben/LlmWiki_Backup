import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec

# 소설 '토지'를 읽어 와서, 형태소 분석을 수행한 다음 model 파일로 저장해 봅니다.

dataIn, dataOut = '../dataIn/', '../dataOut/'
# utf-16 인코딩으로 파일을 열고 글자를 출력하기 --- (※1)
fp = codecs.open(filename= dataIn + 'BEXX0003.txt', mode='r', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')
body = soup.select_one('body > text')
text = body.getText()
# print( text )

# 텍스트를 한 줄씩 처리하기 --- (※2)
okt = Okt()
results = []

lines = text.split('\r\n')
# print( lines )

for line in lines:
    # 형태소 분석하기 --- (※3)
    # 단어의 기본형 사용
    malist = okt.pos(line, norm=True, stem=True)
    #     print( malist )

    r = []

    for word in malist:
        # 어미/조사/구두점 등은 대상에서 제외
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            r.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)
#     print(rl)

# 파일로 출력하기  --- (※4)
# toji.wakati 파일은 형태소 분석(Morphological Analysis)과 불필요한 품사 제거가 완료된 텍스트 파일입니다.
wakati_file = 'toji.wakati'
with open(dataOut + wakati_file, 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(results))

print('파일 ', wakati_file, ' 저장 완료')

# Word2Vec 모델 만들기 --- (※5)
data = word2vec.LineSentence(wakati_file)

model = word2vec.Word2Vec(data, vector_size=200,
                          window=10, hs=1, min_count=2, sg=1)

saved_file_name = dataOut + 'toji.model'

model.save(saved_file_name)

print('파일 ', saved_file_name, ' 저장 완료')

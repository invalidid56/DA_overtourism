# 강준서 invalidid56@snu.ac.kr
# '오버투어리즘', '관광 쓰레기' 관련 기사 분석하여 인사이트 도출
# (1) TF-iDF 분석, (2) word2vec 분석으로 쓰레기가 관광 문제의 큰 축임을 증명한다
# (3) 워드클라우드 분석하여 시각화


import pandas as pd
from konlpy.tag import Okt
from gensim.models.word2vec import Word2Vec


keywords = ['오버 투어리즘']
tagger = Okt()

for kw in keywords:
    corpus = list(pd.read_csv('NaverNews_{0}.csv'.format(kw))['content'].values)

    corpus = [tagger.nouns(line) for line in corpus]

    model = Word2Vec(corpus, min_count=1, workers=4)

    model.wv.most_similar()


밀집지역과 폐기물

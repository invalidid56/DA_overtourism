from konlpy.tag import Okt, Komoran

tagger = Komoran(userdic='userdic.txt')
print(tagger.pos('플로깅이 유행이다'))
print(tagger.nouns('플로깅이 유행이다'))

import re

def remove_special_chars(sentence):
    sentence = re.sub("[^\w'_]", " ", sentence)
    return sentence

def create_BOW(sentence):
    bow = {}
    sentence_preprocessed = remove_special_chars(sentence)
    splitted_sentence = sentence_preprocessed.split()
    filtered_sentence = [token for token in splitted_sentence if len(token) > 1]
    
    for token in filtered_sentence:
        bow.setdefault(token, 0)
        bow[token] += 1
    return bow


# re.compile은 정규식 객체를 만듬
# r은 raw string으로 \를 나타낼때 \\ 두번 붙일 필요가 없다.
# []는 범위
# \w는 [a-zA-Z0-9_]
# sub는 문자열에서 지정된 패턴을 찾아서 replace하는 함수
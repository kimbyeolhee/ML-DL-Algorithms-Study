import pandas as pd

def load_data():
    training_sentences = [[], []]

    # 데이터 로드 및 Na값 제거
    df = pd.read_csv('./ratings.txt', header=0, delimiter='\t')
    df = df.dropna(axis=0)
    df.reset_index(drop=True, inplace=True)

    for i in range(len(df)):
        if df['label'][i] == 0:
            training_sentences[0].append(df['document'][i])
        else:
            training_sentences[1].append(df['document'][i])
    return [' '.join(training_sentences[0]), ' '.join(training_sentences[1])]

if __name__ == '__main__':
    temp = load_data()

    print(temp[0][:10])
    print(temp[1][:10])
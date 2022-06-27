import csv
import MeCab

mecab = MeCab.Tagger()


with open('review.sorted.uniq.refined.tsv', encoding='utf-8') as f:
    tr = csv.reader(f, delimiter='\t')
    data = list(tr)
f.close()

with open('review.sorted.uniq.refined.tok.tsv', 'w', encoding='utf-8', newline='') as f:
    tw = csv.writer(f, delimiter='\t')

    for row in data:
        sentiment = row[0]

        row = mecab.parse(row[1])
        target = row.replace("EOS", "").rstrip()
        sent = ""
        for i in target.split('\n'):
            temp = i.split(',')[0].split('\t')
            sent += (temp[0] + " ")
        tw.writerow([sentiment, sent])
f.close()
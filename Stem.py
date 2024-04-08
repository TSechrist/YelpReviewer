# import these modules
# run `pip install nltk` in Terminal prior to running Main
from nltk.stem import PorterStemmer

def stem(text):
    ps = PorterStemmer()
    # self.text = text
    stemmedList = []

    # words = word_tokenize(text)

    for w in text:
        stemmedList.append(ps.stem(w))

    # print(stemmedList)
    return stemmedList
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

text = """ Hello my name is arvnid currently pursing MCA in JSSATE college.Hello my name Andrew Tate is boxer who who who is four time kickboxing world champion.Hello my name is arvnid currently pursing MCA in JSSATE college.Hello my name Andrew Tate is boxer who who who is four time kickboxing world champion.Hello my name is arvnid currently pursing MCA in JSSATE college.Hello my name Andrew Tate is boxer who who who is four time kickboxing world champion."""

stopWords = set(stopwords.words("english"))
words = word_tokenize(text)
sentences = sent_tokenize(text)  # Tokenize sentences

summary = ""
freqTable = dict()
for word in words:
    word = word.lower()
    if word not in stopWords:
        summary = summary+ " " + word
# print(freqTable)

print(summary)
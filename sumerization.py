import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

text = """ Hello my name is arvnid currently pursing MCA in JSSATE college.Hello my name Andrew Tate is boxerwho is four time kickboxing world champion."""

sentences = sent_tokenize(text)  # Tokenize sentences
stopWords = set(stopwords.words("english"))

words = word_tokenize(text)
sentences = sent_tokenize(text)  # Tokenize sentences

freqTable = dict()
for word in words:
    word = word.lower()
    if word not in stopWords:
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
# print(freqTable)

sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq
        
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text
average = int(sumValues / len(sentenceValue))

summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence

print(summary)
import subprocess
import whisper
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

model = whisper.load_model("small")

subprocess.run(["ffmpeg","-i","input.mp4","-y","OUTPUT.mp3"])

result = model.transcribe("OUTPUT.mp3")["text"]

stopWords = set(stopwords.words("english"))
words = word_tokenize(result)
freqTable = dict()

for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

sentences = sent_tokenize(result)
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

average = int(sumValues / len(sentenceValue))

summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
        
print("Video To Text :\n ",result)
print("\nSummary of the video:\n",summary)

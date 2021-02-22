import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


def tokenize():
    # Tokenizing
    print("Enter a sentence")
    sentence = input()

    tokens = nltk.tokenize.word_tokenize(sentence)
    print(tokens)


def stop_word():
    # StopWord
    print("Enter a sentence")
    sentence = input()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    tokens = word_tokenize(sentence)
    list_stop_word = set(stopwords.words('indonesian'))

    removed = []
    for t in tokens:
        if t not in list_stop_word:
            removed.append(t)

    print(removed)


def stemming():
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    print("Enter a sentence")
    sentences = input()
    sentence = stemmer.stem(sentences)

    print(sentence)


print("1 for tokenizing\n"
      "2 for stop word\n"
      "3 for stemming")
print("Choose number:")
number = input()
if number == "1":
    tokenize()
elif number == "2":
    stop_word()
elif number == "3":
    stemming()
else:
    print("NOPE")

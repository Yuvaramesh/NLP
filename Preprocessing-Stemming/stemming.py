import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
sentence=input("enter the sentence:")
words=word_tokenize(sentence)
for word in words:
    stem_word=ps.stem(word)
    print(word ,":" ,stem_word)

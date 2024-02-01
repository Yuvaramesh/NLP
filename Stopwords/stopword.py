import nltk

nltk.download('punkt')

nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.corpus import stopwords

data = "This is a new exercise."

stop_words = set(stopwords.words('english'))

words = word_tokenize(data.lower())

words_filtered = []

for w in words:

if w not in stop_words:

words_filtered.append(w)

print("Original Words:\n", words)

print("Stopwords:\n", stop_words)

print("Filtered Words:\n", words_filtered)

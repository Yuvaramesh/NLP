
import nltk

def tokenize_text(text): #tokenize_text(text) is the user-defined func

tokens=nltk.word_tokenize(text) #word_tokenize(text) is built-in func

return tokens

sample_inputs=["Hi this is sample input",

"This is the first sample input",

"Okay fine,Let's begin",

"Dive in and Learn together",

"Stay happy forever"]

for text in sample_inputs:

print("Text:",text)

print("Tokens:",tokenize_text(text))

print("-------------")

import re

def detect_word_pattern(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        print("Word Patterns Detected")
        for i in matches:
            print("Matches:", i)
    else:
        print("No Word Patterns Detected")
        
num_patterns = int(input("Enter the number of patterns you want to test: "))
sample_inputs = []
for _ in range(num_patterns):
    pattern_input = input("Enter the pattern: ")
    text_input = input("Enter the text: ")
    sample_inputs.append((pattern_input, text_input))
    
for pattern, text in sample_inputs:
    print("Pattern =", pattern)
    print("Text =", text)
    detect_word_pattern(pattern, text)
    print("----------------------------------------------------------------------")

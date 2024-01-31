# REGULAR EXPRESSION

### ALGORITHM:

### 1. Start the program
### 2. Import the re module for working with regular expression
### 3. Define the function detect word pattern that takes two parameters pattern (the regular expression pattern) and test (the target teat to search for the pattern)** 
### 4. a.  Inside the detect_word pattern function: Use re.findall() to find all occurrences of the pattern within the text Showr the matches in the matches variable.
### b. If matches are found (ie, the matches list is not empty) Print "Word patterns detected:" Iterate over the matches list and print each detected word pattern
### c. If no matches are found (ie, the matches list is empty), print "Ne word patterns detected."
### 5. Define a list called sample inputs that contains multiple tuples. Each tople represents a sample input and consists of a pattern and a corresponding tend to test.

### 6. i. Use a for loop to iterate through each tuple in the sample_inputs list 1. Extract the pattern and text from the current tuple.

### ii. Print the pattern and test for reference.

### iii. Call the detect word pattern function with the pattern and tot as argumenta.
 
### iv. Print a line of dashes to separate the output for each sample

### 7. End the program.


## Function detect_word_pattern(pattern, text):

This function uses the re.findall method to find all occurrences of the specified pattern in the given text.
If matches are found, it prints a message indicating that word patterns are detected, followed by the actual matches.
If no matches are found, it prints a message stating that no word patterns are detected.

## User Input Section:

The code begins by prompting the user to enter the number of patterns they want to test (num_patterns).
It then iterates through each pattern, taking user input for both the pattern and the corresponding text.
The pattern and text inputs are stored as tuples in the sample_inputs list.

## Processing User Inputted Patterns and Texts:

The code then iterates through each tuple in sample_inputs.
For each tuple, it prints the pattern and text.
It calls the detect_word_pattern function with the current pattern and text.
Finally, it prints a separator line to distinguish between different test cases.

## Output:

The output includes information about each test case, indicating the pattern, text, and whether word patterns are detected.
If word patterns are detected, it displays the actual matches found in the text.

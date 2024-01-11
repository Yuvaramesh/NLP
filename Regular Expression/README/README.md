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

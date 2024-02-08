# Stemming Algorithm (PorterStemmer)

### The PorterStemmer algorithm is a widely used stemming algorithm that reduces words to their root form. Here's a simplified overview of the algorithm:

  ### Preprocessing:
  **Convert the word to lowercase.
        Remove any apostrophes and hyphens.**
### Suffix Removal:
  **Check if the word ends with one of the following suffixes:
            "-ed", "-ing", "-ies"
            "-s", "-es", "-ly"
        If a matching suffix is found, remove it from the word.**

  ### Vowel Check:
  **Count the number of vowels in the word.**

    Double Consonant Reduction:
        If the word ends with a double consonant (e.g., "ss", "tt"), and the preceding vowel is short (not followed by another vowel), remove the final consonant.

    Consonant-Vowel-Consonant (CVC) Reduction:
        If the word ends with a consonant-vowel-consonant (CVC) pattern and the preceding vowel is short, remove the final consonant.

    "Y" to "I" Conversion:
        If the word ends with a "y" preceded by a consonant, change the "y" to "i".

    Ending Removal:
        Remove the following suffixes:
            "-ational", "-ization", "-tional", "-ence", "-ance", "-ment", "-ent", "-ism", "-ate", "-ive", "-ize"
        If the word ends with one of these suffixes and the preceding vowel is short, also remove the vowel.

    Postprocessing:
        If the word is reduced to a single letter, restore it to its original form.

    Output:
        The resulting word is the stemmed form of the original word.

This algorithm is applied sequentially to the input word until no further changes can be made. It's important to note that stemming algorithms are heuristic and may not always produce the desired results.

For more detailed information and exceptions to the rules, refer to the original Porter Stemming Algorithm paper.

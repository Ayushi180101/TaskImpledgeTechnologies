# TaskImpledgeTechnologies

Compounded Test Words Finder

Description:
This Python script is designed to find the longest and second-longest compounded test words from a given list. A compounded test word is a word that can be constructed by concatenating two or more words from the same list of test words.
It begins by importing the time module. It defines a recursive function, is_compounded_or_not, which checks if a given word can be formed by concatenating two or more words from the same list. Two main functions, longest_compounded_test_word, and second_longest_compounded_test_word, find the longest and second-longest compounded test words, respectively. The script then enters the __main__ block, initializing a timer and reading test words from "Input_01.txt." It calculates and prints the longest and second-longest compounded test words and the processing time. The process is repeated for "Input_02.txt." Adjustments may be needed based on the input data, and correct file paths must be provided. The code structure demonstrates a modular approach to identifying compounded test words in different datasets.

Functions:
The script includes the following functions:
•	is_compounded_or_not(test_word, original_test_word, test_word_set): Checks whether a given test word is compounded.
•	longest_compounded_test_word(test_words): Finds the longest compounded test word from a list of test words.
•	second_longest_compounded_test_word(test_words, longest_test_word): Finds the second-longest compounded test word from a list of test words, excluding the longest.

Example:
For Text file 01: 
Longest Compound test_word: example_longest_test_word 
Second Longest Compound test_word: example_second_longest_test_word 
Time taken to process input: 123.45 milliseconds 
For Text file 02: 
Longest Compound test_word: another_longest_test_word 
Second Longest Compound test_word: another_second_longest_test_word 
Time taken to process input: 67.89 milliseconds 

Input Files:
The script expects input text files (Input_01.txt and Input_02.txt) containing a list of test words, with each word on a separate line.

How to run the code? :
•	Open the code file a.py along with the text files (Input_01.txt and Input_02.txt).
•	If you haven't already, install the "Python" extension for VS Code. You can do this by clicking on the Extensions view icon in the Activity Bar on the side of the window (or by pressing Ctrl+Shift+X), searching for "Python," and installing the one provided by Microsoft.
•	Execute the script using the following command: python a.py


Notes:
•	Make sure to have the correct file names and paths for the input files in the script.
•	Ensure that Python is added to your system's PATH environment variable.
•	If you encounter any issues, check the VS Code documentation or Python extension documentation for troubleshooting tips.





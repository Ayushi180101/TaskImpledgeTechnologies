import time

def is_compounded_or_not(test_word, original_test_word, test_word_set):
    if test_word in test_word_set and test_word != original_test_word:
        return True
    for i in range(1, len(test_word)):
        prefix = test_word[:i]
        suffix = test_word[i:]
        if prefix in test_word_set and is_compounded_or_not(suffix, original_test_word, test_word_set):
            return True
    return False

def longest_compounded_test_word(test_words):
    test_word_set = set(test_words)
    res = ""

    for test_word in test_words:
        if is_compounded_or_not(test_word, test_word, test_word_set) and len(test_word) > len(res):
            res = test_word
    return res

def second_longest_compounded_test_word(test_words, longest_test_word):
    test_word_set = set(test_words)
    res = ""

    for test_word in test_words:
        if test_word != longest_test_word and is_compounded_or_not(test_word, test_word, test_word_set) and len(res) < len(test_word):
            res = test_word
    return res

if __name__ == "__main__":
    start_time = time.time()

    print(f"For Text file 01:")
    # Read input file
    with open("Input_01.txt", "r") as file:
        test_word_list = [line.strip() for line in file]
    

    # Find longest and second longest compounded test_words
    longest_test_word = longest_compounded_test_word(test_word_list)
    second_longest_test_word = second_longest_compounded_test_word(test_word_list, longest_test_word)

    # Calculate time taken
    end_time = time.time()
    processing_time = round((end_time - start_time) * 1000, 2)

    # Display results
    print(f"Longest Compound test_word: {longest_test_word}")
    print(f"Second Longest Compound test_word: {second_longest_test_word}")
    print(f"Time taken to process input: {processing_time} milliseconds")
    
    start_time = time.time()
    
    print(f"For Text file 02:")
    # Read input file
    with open("Input_02.txt", "r") as file:
        test_word_list = [line.strip() for line in file] 
        
    
    # Find longest and second longest compounded test_words
    longest_test_word = longest_compounded_test_word(test_word_list)
    second_longest_test_word = second_longest_compounded_test_word(test_word_list, longest_test_word)

    # Calculate time taken
    end_time = time.time()
    processing_time = round((end_time - start_time) * 1000, 2)    
        
        
    print(f"Longest Compound test_word: {longest_test_word}")
    print(f"Second Longest Compound test_word: {second_longest_test_word}")
    print(f"Time taken to process input: {processing_time} milliseconds")
    
        
    
    
    
    
    
    
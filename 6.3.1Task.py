"""
Write a function that takes a string as input and returns a tuple containing two elements:

A set containing all the unique words in the input string, ignoring case and punctuation.

A dictionary where the keys are the unique words and the values are the number of occurrences of
each word in the input string.
"""


def punctuation_lower_filter(string):
    """
    this function take string filtered from punctuation and ignore the lower case
    :param string:
    :return:filtered string
    """
    # punctuation marks
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # traverse the given string and if any punctuation
    # marks occur replace it with null
    for word in string.lower():
        if word in punctuations:
            string = string.replace(word, "")

    # return string without punctuation and ignoring case
    return string.lower()


def filtered_data(data):
    """
    this function call the data filter function and pass the string to filtered it
     and define set and dictionary to return a dictionary of
    word and count of each word and set of unique word only
    :param data:string
    :return: tuple of dictionary contains word as a key  and their count as a value and
    the second element in  the tuple is set of unique word
    """
    counts_word = dict()
    unique_word = set()
    data_filter = punctuation_lower_filter(data)
    words = data_filter.split()
    for word in words:
        if word in counts_word:
            counts_word[word] += 1
        else:
            counts_word[word] = 1
    for word in words:
        if counts_word[word] == 1:
            unique_word.add(word)
    return unique_word, counts_word


input_string = "The quick brown fox jumps over the lazy dog. The dog is not amused."
# punctuation_lower_filter(input_string)
# output_string,countword=filtered_data(input_string)
# print(output_string)
# print(countword)
print(filtered_data(input_string))

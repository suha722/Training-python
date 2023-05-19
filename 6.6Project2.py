"""
Project 2 - Building a Vocabulary Quiz
Project Description
In this project, you will build a vocabulary quiz application that tests a user's knowledge of words and
their definitions. The application will read a list of words and their definitions from a file and store them in
a dictionary. The quiz will randomly select a word from the dictionary and prompt the user to enter the definition.
The user's
 score will be displayed at the end of the quiz.

"""

import random


def get_definition_and_delete(word_list, word_dict):
    """
    this function recive the list of word and their definition and delete the if choices
    :param word_list: a list of  word
    :param word_dict: a dictionary of the definition
    :return: a tuple of word and their definition
    """
    random_index = random.randrange(len(word_list))
    word = word_list.pop(random_index)
    definition = word_dict.get(word)
    return word, definition



word_and_definition = lambda the_row: the_row.split(",", 1)


def read_vocabulary(first_file, second_file):
    """
    this function read the file which  contains the word and definition and write the unique word without
    repeater in the second file
    :param first_file: csv file contain word and definition
    :param second_file: the file which write the unique word
    :return: return a line how read it
    """
    try:
        fh = open(first_file, "r")
        wd_list = fh.readlines()
        wd_list.pop(0)
        wd_set = set(wd_list)
        fh = open(second_file, "w")
        fh.writelines(wd_set)
        return wd_set
    except FileNotFoundError:
        print("the file not found!")

if __name__ == "__main__":
    wd_set = read_vocabulary("Vocabulary_list.csv", "Vocabulary_set.csv")
    word_dict = dict()
    score = 0
    number_question = 0
    for row_string in wd_set:
        word, definition = word_and_definition(row_string)

        word_dict[word] = definition

    while True:
        wd_list = list(word_dict)
        choice_list = []

        for x in range(4):
            word, definition = get_definition_and_delete(wd_list, word_dict)
            choice_list.append(definition)
        random.shuffle(choice_list)
        print("|__________________________|")
        print("|What does", word, "mean?")
        print("|__________________________|")
        print_choice = [print(idx + 1, "_", choice) for idx, choice in enumerate(choice_list)]
        try:
            choice = int(input('Enter your option: 1,2,3 or 4; 0 to exit '))
            if choice in [1, 2, 3, 4, 0]:

                if choice_list[choice - 1] == definition:
                    print("Correct!\n")
                    score += 1
                    number_question += 1
                elif choice == 0:
                    print("Your score is :", score, "/", number_question)
                    exit(0)
                else:
                    print("Incorrect")
                    number_question += 1
            else:
                print("Please enter 1,2,3,4 or 0 only!")
        except ValueError as v:
            print("Opps! choice from option and number only.")

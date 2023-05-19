dict_question = {}
dic_question_answer = {}
score_dict={}

import random


def check_answer(question_id, answer, username):
    pass


def ask_question(your_name):
    q_ids = list(dict_question.keys())
    random.shuffle(q_ids)

    for id in q_ids:
        question = dict_question[id]
        print(f"{question['question']}")

        for choice in question['choices']:
            print(choice)

        answer = input('Enter answer: ').capitalize()
        check_answer(id, answer, your_name)


def get_score(your_name):
    pass


def start_quiez():
    your_name=input("Enter your name please: ")
    score_dict[your_name]=0
    ask_question(your_name)
    get_score(your_name)
def readquastion():
    """
    returns:this fuction read the qustion from file
    return answer(string): return the answer of question
    """

    score=0
    list_choice=[]
    try:
        with open("questions.txt", "r") as file:
            with open("answers.txt","r")as fileanswer:
                with open("True_false_answer.txt","r")as t_f_answer:
                    counter = 0
                    for line in file:
                        line = str(line).capitalize()
                        if line.startswith('A.') or line.startswith('B.') or line.startswith(
                                'C.') or line.startswith('D.') or line.startswith('True') or line.startswith(
                                'False'):
                            dict_question[counter]['choices'].append(line.strip())
                        else:
                            counter += 1
                            question = line.strip()
                            dict_question[counter] = {
                                'question': question, 'choices': [], 'answer': ''}
                    print(dict_question)



    except FileNotFoundError:
        print("Sorry the file not found!")
    except Exception as e:
        print("An error occurred:", e)
    return dic_question_answer

def read_answer():
    counter = 0
    try:
        with open("answers.txt", 'r') as file:
            for line in file:
                counter += 1
                answer = line.strip()
                dict_question[counter]['answer'] = answer
            print(dict_question)

    except FileNotFoundError:
        print(f'file {file.name} not found')


    except FileNotFoundError:
        print("Sorry the file not found!")
    except Exception as e:
        print("An error occurred:", e)
readquastion()
read_answer()


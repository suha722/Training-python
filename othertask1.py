"""
Task 1
Suppose we have a list of tuples that contains the name and age of people. We want to filter out the people
whose age is less than 18, then calculate the average age of the remaining people, and finally, generate a set
of the first letters of their names.
"""
# [('Bob', 17), ('David', 16)]
name = 0
age = 1

def people_filter(people):
    """
    this function take a list of tuple of information about people and filter this data depand on
     the age and find average of people how age greater than 18 and set of first letter of their names
    :param people: set of tuple
    :return:  of average people how age greater than 18 and list of poeple how less than 18 and set
    of first letter of their names

    """
    people_less_18 = []
    avarge = 0
    sum = 0
    set_first_letters=set()
    number_people = 0
    for person in people:
        set_first_letters.add(person[name][0])
        if person[age] < 18:
            people_less_18.append(person)
        else:
            number_people += 1
            sum += person[age]
    avarge = sum / number_people
    return people_less_18, avarge ,set_first_letters


data_of_people = [("Alice", 25), ("Bob", 17), ("Charlie", 21), ("David", 16), ("Eve", 19)]
people_less_18, avarge_grate_18,setletter = people_filter(people=data_of_people)
print("THe people less than 18 is :",people_less_18)
print("The average of people greater than 18 is : ",avarge_grate_18)
print("The first letter of their name ",setletter)

'''
Saving a Python dictionary as a JSON file Create a Python dictionary that contains information about
 a book, such as its title, author, and publisher.
 Write a Python program that saves the dictionary as a JSON file called book.json.
'''
import csv
import json

'''
def convert_data_to_json_file(book):
    try:
        with open("books.json", "w") as json_file:
            json.dump(book, json_file,indent=4)
    except json.JSONEncodedError as e:
        print("the error in encodedd: ", e)



def convert_file_csv_to_json_file(file_name):
    json_array = []
    try:
        with open(file_name, "r") as file:
            csv_data = csv.DictReader(file)
            for row in csv_data:
                json_array.append(row)

            with open("book.json", "a") as json_file:
                json.dump(json_array, json_file,indent=4)

        print(json_array)

    except FileNotFoundError:
        print("file not found!")
    # except json.JSONEncodedError as e:
    #     print("the error in encodedd: ", e)


book = {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "publisher": "Pan Books"
}
convert_data_to_json_file(book)
convert_file_csv_to_json_file("books.csv")'''


# Update a key in the JSON data. For example, you could update the person's age to 36. Write the updated
# JSON data back to the file.
'''def update_json_data(json_file, key, value):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
            data[key] = value
            with open(json_file, "w") as update_file:
                json.dump(data, update_file)
            print(data)
    except json.JSONEncoder as e :
        print("the proplem in encoder the file",e)
    except json.JSONDecodeError as e:
        print("the proplem in decoder the file",e)


update_json_data("books.json", "age", 47)
#Add a new key-value pair to the JSON data. For example, you could add_book a new key-value pair for
 the person's occupation. (occupation -> Software Developer)
'''
def add_new_to_json_data(json_file, key, value):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
            data[key]=value
            with open(json_file, "w") as update_file:
                json.dump(data, update_file)
            print(data)
    except json.JSONEncoder as e :
        print("the proplem in encoder the file",e)
    except json.JSONDecodeError as e:
        print("the proplem in decoder the file",e)
add_new_to_json_data("books.json","occupation","software develpment")

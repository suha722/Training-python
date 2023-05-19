import argparse
import json

parser = argparse.ArgumentParser(description="command-line tool that reads a JSON file containing a list of products")
parser.add_argument('-f', '--file', help=" the path to the JSON file containing the product data")
parser.add_argument('-a', '--add_book', help="add_book a new product to the JSON data", action="store_true")
parser.add_argument('-u', '--update', help="update an existing product in the JSON data", action="store_true")
parser.add_argument('-d', '--delete', help="delete a product from the JSON data", action="store_true")
parser.add_argument('-l', '--list', action="store_true", help=" list all the products in the JSON data")
parser.add_argument('-n', '--name', type=str, help="the name of product")
parser.add_argument('-p', '--price', type=float, help="the price of product")
parser.add_argument('-num', '--input_number', type=int, help="the input_number of product")
args = parser.parse_args()


def show_list(json_file):
    """
    this functon open the json file and loaded to the data and print in the list formatted
    :param json_file: the json file
    :return: print the contents of the file in order way
    """
    with open(json_file, "r") as file:
        data = json.load(file)
        length=len(data)
        for i in range(length):
            view_line = str(i) + " . " + data[i]['name'] + " _ $" + str(data[i]['price'])
            print(view_line)


def update(json_file, num, name, price):
    """
    this fuction make updated for the contents of the json file and after update reload the new data
    :param json_file:
    :param num: the numbe rof dictionary in the list you want to be updated
    :param name: the new name of  the product
    :param price: the new price of product
    :return:the new of dictionary add_book to contents of json file
    """

    with open(json_file, "r") as file:
        data = json.load(file)
        data[num]["name"] = name
        data[num]["price"] = price

        with open(json_file, "w") as updatefile:
            json.dump(data, updatefile, indent=4)
    print("success to update!")


def add(json_file, name, price):
    """
    this function receive name and price of product you want to add_book to json file
    :param json_file: the file of json
    :param name: the name of product you want to add_book
    :param price: the price of product you want to add_book
    :return: the new of dictionary add_book to contents of json file
    """
    with open(json_file, "r") as file:
        data = json.load(file)
        new = {"name": name, "price": price}
        if new["name"] is not None and new["price"] is not None:
            data.append(new)
        else:
            print("we must enter name and price of the product!")
        with open(json_file, "w") as updatefile:
            json.dump(data, updatefile, indent=4)



def delete_product(json_file, number):
    """
    this function delete the dictionary in the list of index of the input_number entered
    :param json_file: file contains of list of dictionary
    :param number: the index of dictionary you want to delete
    :return: the re load the data after update to the json file
    """

    with open(json_file, "r") as file:
        data = json.load(file)
        if number in range(len(data)):
            data.pop(number)
            print("success to deleted ^^")
        else:
            print("The input_number is out of range of !")
        with open(json_file, "w") as updatefile:
            json.dump(data, updatefile, indent=4)



if args.list:
    show_list(args.file)

if args.add:
    add(args.file, args.name, args.price)

if args.update:
    update(args.file, args.number, args.name, args.price)

if args.delete:
    delete_product(args.file, args.number)

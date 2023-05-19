import csv
import re
import os


class InvalidDataError(Exception):
    pass


def read_csv_file(csv_file):
    valid_data = []
    error = []
    # Verify that the file exists and can be read
    pattern = re.compile(csv_file)
    dir = "C:/Users/ADMIN\PycharmProjects/pythonProject/Week5/"
    for filepath in os.listdir(dir):
        if pattern.match(filepath):
            with open(csv_file, "r") as csvfile:
                csv_data = csv.reader(csvfile)
                for data in csv_data:
                    # Verify that the name column contains only letters and spaces
                    # Skip the header row of the CSV file
                    if str(data).__contains__("Name"):
                        # print(str(data))
                        search = re.search(r"\[\'\w+\'\,\s\'\w+\'\,\s\'\w+\'\]", str(data))

                        if search != []:
                            print("The heading is good")
                        else:
                            print("The name of column must contains only letters and spaces")
                    else:
                        # verify number of column
                        count = re.split(r"\,", str(data))
                        if len(count) > 3:
                            error.append(tuple(count))
                            print(f"Warning this have more than three column {count}!")
                        else:
                            # verify age between 18 and 120
                            age = int(count[1].replace("'", " "))
                            if age > 120 or age < 18:
                                print(f"The age of {count} is invalid verify it !")
                                error.append(tuple(count))
                                # raise InvalidDataError(f"The age of {count[0].replace('[','')} is invalid verify it !")
                            else:
                                # verify salary is positive and less than a million
                                salary = float(count[2].replace("'", " ").replace("]", ""))
                                if salary < 0 or salary > 1000000:
                                    error.append(tuple(count))
                                else:
                                    vailed = tuple(data)
                                    valid_data.append(vailed)
                                # raise InvalidDataError(f"The salary of {count[0].replace('[','')} is invalid verify it !")

    return valid_data, error


try:
    vaileddata, invaileddata = read_csv_file("csv_file")
    print("\nThis vailed data :\n", vaileddata)

    if len(invaileddata) != 0:
        raise InvalidDataError(f"This row are invalid\n {invaileddata}")
except InvalidDataError as e:
    print("Opps! ", e)
except FileNotFoundError as e:
    print("Opps! ", e)

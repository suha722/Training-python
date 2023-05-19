"""

Task - Password Checker
Write a Python program that prompts the user to enter a password and checks if the password meets certain
requirements. If the password is invalid, the program should raise a custom exception InvalidPasswordError
 with a message indicating the reason for the failure.
The password must meet the following requirements:

The password must contain at least 8 characters.
The password must contain at least one uppercase letter.
The password must contain at least one lowercase letter.
The password must contain at least one digit.

"""
import json
import random
import secrets
import string
from threading import Timer
import time


class InvalidPasswordError(Exception):
    count = 0


class Password:
    # list_input=[]
    def check_password(self, password):
        if len(password) >= 8:
            InvalidPasswordError.count += 1
        else:
            print("The password must be at least 8 characters")

        for char in password:
            if char.isupper():
                InvalidPasswordError.count += 1
                break
        else:
            print("The password must contain at least one uppercase letter.")
        for char in password:
            if char.islower():
                InvalidPasswordError.count += 1
                break
        else:
            print("The password must contain at least one lowercase letter.")
        for char in password:
            if char.isdigit():
                InvalidPasswordError.count += 1
                break
        else:
            print("The password must contain at least  one digit.")
        if InvalidPasswordError.count < 4:
            raise InvalidPasswordError("Sorry invalied password!")
        else:
            print("Thank you the password is valid ")
        return InvalidPasswordError.count

    def generate_password(self):
        length = [10, 5, 8, 9, 4, 12]
        pwd_length = random.choice(length)
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits + special_chars
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
        return pwd

    def write_password_in_file(self):
        finshed=func()
        if finshed == True:
            print("")
            with open("Bank.json", "w") as file:
                # for pasw in list_input:
                json.dump(list_input,file,indent=4)
                file.write("\n")
        for word in list_input:
            print(word, Password.check_password(self,word))
    def password_arrangement(self):
        # count_error=0
        # for passw in range(len(list_input)):
        for word in list_input:

            if Password.check_password(self,word) ==0:
                with open("strong.txt","a")as file:
                    file.write(word)
                    file.write("\n")
            if Password.check_password(self,word)==1:
                with open("accept.txt","a")as file:
                    file.write(word)
                    file.write("\n")
            if Password.check_password(self,word)==2:
                with open("medium.txt","a")as file:
                    file.write(word)
                    file.write("\n")
            if Password.check_password(self,word)==3:
                with open("weak.txt","a")as file:
                    file.write(word)
                    file.write("\n")
            if Password.check_password(self,word)==4:
                with open("forbidden.txt","a")as file:
                    file.write(word)
                    file.write("\n")



    #
    # write_password_in_file()


if __name__ == '__main__':
    list_input = []
    password = Password()

    try:
        def func():
            print("The all password is written in the bank of word after the time thank you!")
            return True


        # Schedule a timer for 3 seconds

        t = Timer(3.0, func)

        start_time = time.time()

        # Start the timer
        t.start()

        end_time = time.time()

        if end_time - start_time < 3.0:
            for i in range(200):
                list_input.append(password.generate_password())
            print(list_input)

        else:
            print("5 seconds already passed. Timer finished calling func()")
        password.write_password_in_file()
        # password.password_arrangement()


    except InvalidPasswordError as e:
        print(e)

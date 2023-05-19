"""
Modifications for 4.1.1 Task:
Person: instead of employee, you need to use a person object. You are free to design Person Class.
Input Sheet: You need to support an input sheet file for the task (JSON or CSV) that has the following line format:
<Account Type> <Name> <Account Number> <Current Balance>
This sheet is going to be the input of your task - you need to process it and create needed accounts as specified.
You need to perform some operations using a function called operations that calls some implemented functions.
 By the end of each run, you are asked to output two files
Statistics.log: this files needs to show the following
Accounts that are in minus --> <Account Number> <Value> <Notified by email (optional)>
Business accounts (decide on how you want to write business account data)
Operations.log this file needs to log each operation that was made during the run
<Operation Name> <Account> <Old Balance> <New Balance>
Note: Do not use the example usage, take the input sheet to create account and operations functions to call the
whole flow. In case you did not finish all of this within online coding - take this as a Homework

"""
import json
from abc import ABCMeta,abstractmethod

class Account(metaclass=ABCMeta):
    """
    abstreact class have three class inherited from it
    """

    def __init__(self, number, balance, ownername):
        """
        This is abtrsact method equal constructor for class account
        :param number: the input_number of account
        :param balance: the balance of account
        :param ownername: the name of owner account
        """
        self.number = number
        self.balance = balance
        self.ownername = ownername


class CheckingAccount(Account):
    def __init__(self, number, balance, ownername):
        """
        This is abtrsact method equal constructor for class Cheking account and this account inherit from Account
        :param number: the input_number of account
        :param balance: the balance of account
        :param ownername: the name of owner account
        """
        super().__init__(number, balance, ownername)


    def withdraw(self, amount):
        """

        This function make with drow from account deband on the amount are passed
        :param amount: the amount of monay you waant to with drow
        :return: the new balance after this operation
        """
        result=0
        if amount > self.balance:
            print(f"you don't have this amount of many your monay is only : {self.balance}")
        else:
            result=self.balance -amount
            return result


class SavingsAccount(Account):
    def __init__(self, number, balance, ownername):
        super().__init__(number, balance, ownername)

    def compound_interest(self,balance,rate):
        return balance + (balance * rate)


class BusinessAccount(Account):

    def __init__(self, number, balance, ownername):
        super().__init__(number, balance, ownername)

    def add_person(self, obj):
        obj.persons.append(f"{obj.name} , {obj.age} , {obj.email}")
        return obj.persons


class Person:
    count = 0
    persons = []

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        Person.count += 1

    def number_of_person(self):
        print("The person input_number ", Person.count)


class Bank:

    def __init__(self, pathfile):
        self.pathfile = pathfile

    def read_sheet(self):

        with open(self.pathfile, "r") as file:
            data = json.load(file)
            length = len(data)
        return length, data

    def sorting_data(self):
        buss = []
        save = []
        check = []
        length, listread = Bank.read_sheet(self)
        for i in range(length):
            if listread[i]["Account Type"] == "Business":
                buss.append(listread[i])
            if listread[i]["Account Type"] == "Saving":
                save.append(listread[i])

            if listread[i]["Account Type"] == "Checking":
                check.append(listread[i])

        return buss, check, save

    def create_account(self, account_type=None, number=None, balance=None, name=None):
        if type(account_type)==str and type(number)==int and type(balance)==int and type(name)==str:
            length, readlist = Bank.read_sheet(self)
            for index, item in enumerate(readlist):
                # todo : edit list
                if item['Account Number'] != number:
                    dictnew = {"Account Type": account_type, "Name": name, "Account Number": number, "Current Balanc": balance}
                    readlist.append(dictnew)
                    with open(self.pathfile, "w") as file:
                        json.dump(readlist, file, indent=4)
                else:
                    print("Sorry the account input_number must be unique")
                break
        else:
            print("please enter a valid attrepute!")

    def delete_accounts(self, account_number):
        if type(account_number)==int:
            length, readlist = Bank.read_sheet(self)

            for index, item in enumerate(readlist):
                if item['Account Number'] == account_number:
                    del readlist[index]
                    with open(self.pathfile, "w") as file:
                        json.dump(readlist, file, indent=4)
                    break
            else:
                print("This input_number not in the list !!")


        else:
            print("The account input_number must be integer")
    def view_account(self):
        length, readlist = Bank.read_sheet(self)
        for index, item in enumerate(readlist):
            print(item)

    def search_account(self,account_number):
        if type(account_number)==int:
            length, readlist = Bank.read_sheet(self)

            for index, item in enumerate(readlist):
                if item['Account Number'] == account_number:
                    print("We find this account the details is :")
                    print(item)
                    break
            else:
                print("Sorry this account not in the Bank !!")



        else:
            print("The account input_number must be integer")


def operation():
    result=0
    bank=Bank("Input_sheet.json")
    check=CheckingAccount(8,1200,"Huda")
    buss=BusinessAccount(8,1900,"Saaed")
    save=SavingsAccount(9,1200,"Shahd")
    length, data = bank.read_sheet()
    amount = int(input("Enter the amount you want "))
    for i in range(length):
        if data[i]["Account Type"]=="Saving":
            res=save.compound_interest(data[i]["Current Balanc"],0.2)
            write_operation("compound_interest",data[i]["Account Number"],data[i]["Current Balanc"],res)
        if data[i]["Account Type"]=="Checking":
            check.withdraw(amount)
            if amount < data[i]["Current Balanc"]:
                result=data[i]["Current Balanc"]-amount
                write_operation("withdraw", data[i]["Account Number"],data[i]["Current Balanc"],result)

        if data[i]["Current Balanc"] < 0:
            account_in_minis(data[i]["Account Number"],data[i]["Current Balanc"])
        if data[i]["Account Type"] == "Business":
            write_business_account(data[i]["Account Number"])

def write_operation(op_name,acc_number,before_value,after_value):
    file2.write(f"{op_name}  account input_number is {acc_number} \n"
                f"The balance before {op_name} is: {before_value}\n"
                f"And after {op_name} is : {after_value}")
    file2.write("\n")
def account_in_minis(account_number, account_balance):
    # file1 = open("statics.log", "a")
    file1.write(f"This account balance is in minus\n"
                f"The account input_number is :{account_number}\n"
                f"the current balance of account is :{account_balance}\n")
    file1.write("\n")
def write_business_account(account_number):
    # file1 = open("statics.log", "a")
    file1.write(f"This account is business account \nAnd the input_number is {account_number}\n")

b = Bank("Input_sheet.json")
b.create_account("Saving",3,1200,"Hade")
file1 = open("statics.log", "a")
file2 = open("operation.log", "a")




'''b.view_account()
b.search_account(1)
length, lists = b.read_sheet()
s, ss, sss = b.sorting_data()
print("The bussness list is :", s)
print("The checking  list is :", ss)
print("The saving  list is :", sss)
print(length, lists)
b.create_account()
b.delete_accounts(1)

print(lists)
'''

# p=Person("test1",33,"sohaardah@gmial.com")
# b=BusinessAccount(12,1223,"suha")
# p.number_of_person()
# print(b.add_person(p))
operation()
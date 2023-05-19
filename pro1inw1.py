accounts={}
acc2={"Name":"Ibrahim","balance":1000,"input_number":4444}
ch=0
print("________________Welcom to My bank __________________")
print(" if you want to creat account press 0 ")
print(" if you want to enter an amount into u account press 1 ")
print(" if you want to  pull some amount from u account press 2 ")
print(" if you want to  check balance for account press 3 ")
print(" if you want to  transfer to account 2 press 4 ")
print(" if you want to  exit from account 5 ")


while True:
    #create account
    ch = int(input("plz enter 0 or  1 or 2 or 3 or 4 or 5 for what u want"))
    print("***************************************************")
    if ch ==0:
        accounts["Name"]=input("plz enter u name")
        accounts["initial_balance"]=float(input("plz enter u initial_balance"))
        accounts["Number"]=int (input("plz enter u account input_number"))
    #allaccount.append(accounts)
    # deposit to accounts
    if ch ==1:
        add = float(input("enter how much u want to add_book"))
        if add<0:
            print("what do you mean plz enter positive input_number !!!!!!!!!!")


        else:
            number=int (input("plz enter u account input_number to add_book"))
        # for c in accounts:
            if number==accounts["Number"]:
                accounts["initial_balance"] +=add
            else:
                print("SOOORY the input_number not found-_-!!!!!!")

    #pull from accounts

    if ch ==2:
        pull = float(input("enter how much u want to pull"))
        number = int(input("plz enter u account input_number to pull"))
        # for a in accounts:
        if number == accounts["Number"]:
            if accounts["initial_balance"]>pull:
                 accounts["initial_balance"] -=pull
            else :
                print("you don't have much monay")
        else :
            print("SOOORY the input_number not found-_-!!!!!!")
    #check balance
    if ch == 3:
        number = int(input("plz enter u account input_number to check "))
            # for a in accounts:
        if number == accounts["Number"]:
            print("Current balance for account input_number :", accounts["Number"]," is : ",accounts["initial_balance"])

        else:#if the input_number not same from
            print("SOOORY the account not found-_-!!!!!!")

    if ch ==4:
        tr=float(input("how you want to transfer "))
        n=int(input("plz enter the input_number of account 2 to transfer "))
        if n==acc2["input_number"]:
            if accounts["initial_balance"] > tr :
                acc2["balance"]+=tr
                accounts["initial_balance"]-=tr
                print("success to transfer to another account thanks^^ the details of account2 ","\n",acc2)
            else:
                print("you don't have this monay!!!")
        else:
            print("The input_number is not in bank!!!!!")
    if ch == 5:
        print("Good bye ^^")
        break

    if ch not in [0,1,2,3,4,5]:
        print("plz enter the choose from the option!!!!!")


    print("Account details is : \n",accounts)
    #  print(allaccount)



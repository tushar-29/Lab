import json

def send_data(mydict, choice):
    with open('data.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

    if choice == 1:
        json_data[mydict['id']] = mydict
    else:
        json_data[mydict['id']]['balance'] = mydict['balance']
    with open('data.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile)


def BankingPage(c_data):
    while True:
        print("-------------------------------------------------------------")
        print(f"\n\nNAME : {c_data['name']}\nACC. NO. : {c_data['acc_no']}")
        print("Balance : Rs", c_data['balance'], ".00")
        print("1)Deposit\n2)Withdrawal\n3)LogOut")
        choice = input("Enter your choice : ")

        if choice == '1':
            amt = int(input("\n\n\tDEPOSIT\nEnter the amount to be deposit : Rs."))
            c_data['balance'] += amt
            input(f"Rs.{amt}.00 has been deposited. [press enter]")

        elif choice == '2':
            amt = int(input("\n\n\tWITHDRAWAL\nEnter the amount to be withdrawal : Rs."))
            if c_data['balance'] < amt:
                input(f"Insufficient balance [press enter]")
                continue
            else:
                c_data['balance'] -= amt
                input(f"Rs.{amt}.00 has been withdrawal. [press enter]")

        elif choice == '3':
            break
        else:
            input("\nWrong choice [press enter]")
    send_data(c_data, 2)


def CreateBankAcc():
    while True:
        print("-------------------------------------------------------------")
        print("\n\nFill the form :\n")
        login_id = input('Login id : ')
        if login_id in data:
            print("\nLogin id already exist [press enter]")
            return
        password = input('Login id : ')
        name = input('Name : ')
        acc_no = int(input('acc_no : '))
        bal = int(input('Enter the initial deposit amount : Rs.'))

        data[login_id] = {
            'id': login_id,
            'password': password,
            'name': name,
            'acc_no': acc_no,
            'balance': bal
        }
        send_data(data[id], 1)
        input("\nAccount creation success [press enter]")


def LoginPage():
    while True:
        print("-------------------------------------------------------------")
        print("\n\n\tLOGIN PAGE\n")
        login_id = input("Enter your login id : ")
        password = input("Enter your password : ")

        if login_id in data:
            if data[login_id]['password'] == password:
                BankingPage(data[login_id])
            else:
                input("\nError : Wrong Password [press enter]")
        else:
            input("\nError : Incorrect Login Id [press enter]")


def Main():
    while True:
        print("\n\n\tWELCOME TO BANK\n")
        print("1) Create your bank account\n2)Login")
        choice = input("Enter your choice : ")
        if choice == '1':
            CreateBankAcc()
        elif choice == '2':
            LoginPage()
        else:
            input("\nWrong choice [press enter]")



with open('data.json', 'r') as file:
    data = json.load(file)

Main()
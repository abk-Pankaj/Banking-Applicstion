#Banking application
def check_amt():
    print("===================================")
    print(f"Your current balance is {balance}")
    print("===================================")

def deposite_amt(amount):
    global balance
    if amount > 0:
        balance += amount

def withdraw_amt(amount):
    global balance
    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient balance. Transaction cancelled.")
    else:
        balance -= amount
        print(f"Withdrawal of {amount} successful. Remaining balance: {balance}")


balance = 0
people_list = [{
                'name': 'Pankaj',
                'age': 18

            },]
login = False


#starting Interface



print("Welcome To ABC Bank")
print("If your are registered Costumer please login or if your new please Sign Up\n1. Login\n2. Sign up ")

user = int(input("Enter your option(1-2): "))



if user == 2:
    """
    adding Costumers registration detain Details
    """
    # login = True

    while True:
        print("Provide your Correct Basic Details")

        name = input("Enter your name: ")
        age = int(input("Enter your Age: "))

        print(f"Your name is {name} and you are {age} old")
        print("To Summit click 1.\nTo edit Click 2.")

        appli_sub = int(input())

        if appli_sub == 1:
            print("Thanks for choosing ABC Bank")

            list_costumer = {
                'name': name,
                'age': age

            }

            people_list.append(list_costumer)
            print("Registration successful!")
            print(f"Welcome to ABC Bank {name} ")

            break

        elif appli_sub == 2:
            continue






elif user == 1:
    while True:
        if not people_list:
            print("No registered customers yet. Please sign up first.")
        else:
            login_name = input("Enter your name: ")
            login_age = int((input("Enter your age: ")))

            found = False
            for person in people_list:
                if person['name'] == login_name and person['age'] == login_age:
                    print("========================================")
                    print(f"Welcome back, {login_name}!")
                    print("========================================")
                    found = True
                    break

            if not found:
                print("Login failed. Please check your details or sign up first.")
                continue
                login = True
            else:
                break



if login == False:
    while True:
        print("\nChoose an option:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = (input("Enter choice: "))

        if choice == '1':
            check_amt()
        elif choice == '2':
            print("===============================================")
            amt = int(input("Enter Your Amount for Deposite: "))
            print("===============================================")

            print(f"Your amount of {amt} has been Deposited")

            deposite_amt(amt)
        elif choice == '3':
            print("===============================================")
            amt = int(input("Enter Your Amount for Withdrawn: "))
            print("===============================================")
            withdraw_amt(amt)
        elif choice == '4':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice, try again.")

















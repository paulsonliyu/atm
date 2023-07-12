from atm import Bank

def main():
    print('Welcome to the ATM!\n')
    print('Enter your information: ')
    username = input('Name: ')
    age = input('Age: ')
    gender = input('Gender: ')
    user = Bank(username, age, gender)

    while True:
        print('\nWhat would you like to do?')
        print('1. Deposit\n2. Withdraw\n3. View Details\n4. Quit')
        choice = int(input('Enter choice: '))

        if choice == 1:
            amount = int(input('Enter deposit amount: $'))
            user.deposit(amount)
        elif choice == 2:
            amount = int(input('Enter withdraw amount: $'))
            user.withdraw(amount)
        elif choice == 3:
            user.view_information()
        elif choice == 4:
            print('\nThank you!')
            quit()


if __name__ == '__main__':
    main()

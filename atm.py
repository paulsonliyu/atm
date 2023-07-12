class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print('\nPersonal Information:')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')


class Bank(User):
    def __init__(self, name, age, gender, ):
        super().__init__(name, age, gender)
        self.amount = 0
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f'\nAccount balance has been updated: ${self.balance}')

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f'\nInsufficient Funds | Balance Available : ${self.balance}')
        else:
            self.balance -= self.amount
            print(f'\nAccount balance has been updated: ${self.balance}')

    def view_information(self):
        self.show_details()
        print(f'Account balance: ${self.balance}')



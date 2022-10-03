import sys
import re
import time

def main():
    while True:
        name = sys.argv[1]
        acc_number = sys.argv[2]
        phone_number = sys.argv[3]

        new_acc = SavingsAccount(name, acc_number, phone_number)
        customers = []
        accounts = {}
        accounts['name'] = new_acc.name
        accounts['acc_number'] = new_acc.acc_number
        customers.append(accounts)
        mybank = Bank('me', 'me', new_acc)
        
        command = input("command: ")
        new_command = command.split(' ')
        if new_command[0] == 'deposit':
            new_acc.deposit(int(new_command[1]))
            print(new_acc.balance)
            print(new_acc.history)
        elif new_command[0] == 'withdraw':
            new_acc.withdraw(int(new_command[1]))
            print(new_acc.balance)
            print(new_acc.history)
        print(customers)
        continue


class Bank:
    def __init__(self, stakeholders, employees, customers):
        self.name = 'mybank'
        self.stakeholders = stakeholders
        self.employees = employees
        self.customers = customers

class Accounts:
    def __init__(self, name, acc_number, phone_number):
        self.name = name
        self.acc_number = acc_number
        self.phone_number = phone_number
        self.balance = 0
        self.history = []

    def deposit(self, ammount):
        self.balance += ammount
        self.history.append(f'deposited {ammount}')
        
    def withdraw(self, ammount):
        self.balance -= ammount
        self.history.append(f'deposited {ammount}')

class CurrentAccount(Accounts):
    def __init__(self ,name, acc_number, phone_number):
        super().__init__(name, acc_number, phone_number)

    def deposit(self, ammount):
        self.balance += ammount
        
    def withdraw(self, ammount):
        self.balance -= ammount

    def check(self, ammount):
        time.sleep(100)
        self.balance -= ammount

    def __str__(self):
        return str(self.name)

class SavingsAccount(Accounts):
    def __init__(self ,name, acc_number, phone_number):
        super().__init__(name, acc_number, phone_number)

    def deposit(self, ammount):
        self.balance += ammount
        self.history.append(f'deposited {ammount}')
        
    def withdraw(self, ammount):
        self.balance -= ammount
        self.history.append(f'deposited {ammount}')

    def __str__(self):
        return str(self.name)
    
class KidsAccount(Accounts):
    def __init__(self ,name, acc_number, phone_number):
        super().__init__(name, acc_number, phone_number)

    def deposit(self, ammount):
        self.balance += ammount
        
    def withdraw(self, ammount):
        self.balance -= ammount

    def __str__(self):
        return str(self.name)


if __name__ == '__main__':
    main()


# module_10_3 Блокировки и обработка ошибок

'''
Задание:
Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.

Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации
общего ресурса.

Пример работы:
def deposit_task(account, amount):
  for _ in range(5):
    account.deposit(amount)

def withdraw_task(account, amount):
  for _ in range(5):
    account.withdraw(amount)
account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

Вывод в консоль:
Deposited 100, new balance is 1100
Deposited 100, new balance is 1200
Deposited 100, new balance is 1300
Deposited 100, new balance is 1400
Deposited 100, new balance is 1500
Withdrew 150, new balance is 1350
Withdrew 150, new balance is 1200
Withdrew 150, new balance is 1050
Withdrew 150, new balance is 900
Withdrew 150, new balance is 750


Примечание:

    Используйте класс Lock из модуля threading для блокировки доступа к общему ресурсу.
    Ожидается создание двух потоков, один для пополнения счета, другой для снятия денег.
    Используйте with (lock object): в начале каждого метода, чтобы использовать блокировку
'''

import threading

class BankAccount:
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdrew {amount}, new balance is {self.balance}')
            else:
                print(f'Insufficient funds for withdrawal of {amount}')

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)

account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

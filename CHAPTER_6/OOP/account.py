class Account:
    num_acnt = 0

    @classmethod
    def get_num_acnt(cls):
        return cls.num_acnt

    def __init__(self, name, money):
        self.user = name
        self.balance = money
        Account.num_acnt += 1

    def deposit(self, money):
        if money < 0:
            return
        self.balance += money

    def withdraw(self, money):
        if money > 0 and money <= self.balance:
            self.balance -= money
            return money
        else:
            return None

    def transfer(self, other, money):
        mon = self.withdraw(money)
        if mon:
            other.deposit(mon)
            return True
        else:
            return False

    def __str__(self):
        return 'user : {}, balance : {}'.format(self.user, self.balance)


if __name__ == "__main__":
    my_acnt = Account('greg', 5000)
    your_acnt = Account('john', 1000)

    print('object created')
    print(my_acnt)
    print(your_acnt)
    print()

    my_acnt.deposit(500)

    print('deposit')
    print(my_acnt)
    print()

    print('withdraw')
    money = my_acnt.withdraw(1500)

    if money:
        print('withdrawn money : {}'.format(money))
    else:
        print('Not enough to withdraw')
    print()

    print('class member')
    print(Account.num_acnt)
    print()

    print('class method')
    n_acnt = Account.get_num_acnt()

    print('The number of accounts : {}'.format(n_acnt))
    print()

    print("message passing")
    print(my_acnt)
    print(your_acnt)
    res = my_acnt.transfer(your_acnt, 2000)
    if res:
        print('transfer succeeded')
    else:
        print('transfer failed')
    print(my_acnt)
    print(your_acnt)

#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = float(discount)
        self.total = 0.0
        self.items =[]
        self.transactions = []


    def add_item(self, title, price, quantity=1):
        self.total += (price * quantity)
        self.transactions.append(price * quantity)
        for i in range(quantity):
            self.items.append(title)
        return self.total

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total * ((100 - self.discount)/100)
            print("After the discount, the total comes to $800.")
            return self.total
    
    def void_last_transaction(self):
        self.transactions.pop()
        if len(self.transactions) == 0:
            return 0.0
        self.total = sum(self.transactions)
        return self.total

    

x = CashRegister()
x.add_item("mac", 1000)
x.add_item("meme", 500)
x.add_item("lon", 300)
x.apply_discount()
print(x.void_last_transaction())
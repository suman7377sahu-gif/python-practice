# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways
from random import randint

class Train :

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book (self,fro, to):
        print(f"Your ticket has been confirmed from {fro} to {to}.")
    def getStatus (self):
        print(f"The train number {self.trainNo} is running on time.")
        
    def getFare(self, fro, to):
        print(f"Tran number {self.trainNo} is booked with fare of {randint(299,5999)} rs. from {fro} to {to}")

t = Train(15866)
t.book("Berhampur","Sikkim")
t.getStatus()
t.getFare("Berhampur","Sikkim")
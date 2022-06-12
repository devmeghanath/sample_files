class Vehicle:
    def general_usage(self):
        print('for Transportation')

class Car(Vehicle):
    def __init__(self):
        print('I am Car')
        self.wheel=4
        self.roof=True

    def specific_purpose(self):
        print('for office use')

class Bike(Vehicle):
    def __init__(self):
        print('I am Bike')
        self.wheel=2
        self.roof=False
    def specific_purpose(self):
        print('for trip use')

        
cbr=Bike()   
cbr.general_usage()
cbr.specific_purpose()

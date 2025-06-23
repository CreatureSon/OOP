import random

class Bug:

    def __init__(self, wings, legs):
        self.wings = wings
        self.legs = legs
        self.miles = 0

    def plan_flight(self):
        self.miles = random.randint(1,10)
    
    def fly(self):
        return self.miles

def main():

    bee = Bug(2, 6)
    bee.plan_flight()
    print(bee.fly())

    ant = Bug(0,6)
    ant.plan_flight()
    print(ant.fly())

    grasshopper = Bug(2,6)
    grasshopper.plan_flight()
    print(grasshopper.fly())

main()
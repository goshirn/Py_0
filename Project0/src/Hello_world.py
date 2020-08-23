#!/usr/bin/env python3
import sys

class Person():
    def __init__ (self):
        self.age_constant = 25
        self.age = None
        self.name = None

    def getInput(self):
        self.setAge(input("Input your age: "))
        self.setName(input("Input your name: "))
        #self.setName("aaa")
        print(self.age)
        print(self.name)

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def age_check(self):
        if int(self.age) < self.age_constant:
            print("You're young")
        else:
            print ("You're old")

def main():
    #age_check(sys.argv[1])
    person1 = Person()
    person1.getInput()
    person1.age_check()

if __name__ == '__main__':
    main()

class Person:
    def __init__ (self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printFullName(self):
        fullName = self.firstName + " " + self.lastName
        return fullName
    

if __name__ == '__main__':
    Name = Person("Solid", "Snake")
    print(Name.printFullName())
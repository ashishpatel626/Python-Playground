class cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def combine(self):
        return self.make + self.model + str(self.year);



if __name__ == '__main__':
    honda = cars('honda ', 'insight ', 2019)
    print(honda.combine())

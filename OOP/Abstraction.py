from concurrent.futures import process
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(Computer):
    def process(self):
        print("its running")

class Programmer:
    def work(self, com):
        print("solving bugs")
        com.process()
        
class Whiteboard:
    def write(self):
        print("its writing")

com1 = laptop()
com2 = Whiteboard()
prog1 = Programmer()

prog1.work(com1)
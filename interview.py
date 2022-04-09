from  hashlib import sha256

# Problem 1
# Write a program to print all permutations of a given String. For example, if given String is "GOD" then your program should print all 6 permutations // of this string, e.g. "GOD," "OGD," "DOG," "GDO," "ODG," and "DGO." ----------***
'''
from itertools import permutations

string = ("Book")
'''



#write a function that checks if two provided strings are anagrams of each other; letter casing shouldn’t matter. Also, consider only characters, not //spaces or punctuation. For example
#function('finder', 'Friend')  --> trued
#function('hello', 'bye') --> false -------------**
w1 = "ship"
w2 = "ship "

def hashConversion(word):
    for i in w1:
        h = sha256(i.encode())
        l = hash(h)
    return(l)

print(hashConversion(w1))
print(hashConversion(w2))
'''
def anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False
        
print(anagram("pihs", "ship"))
'''
'''
#Problem 3
#Write a program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and print "Buzz" for the multiples of five. When number is divided by both three and five, print "fizz buzz"
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz") 
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(str(i))
'''
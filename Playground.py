def reverse_string(string: str) -> str:
    reversed_string = ""
    for x in string[:: -1]:
        reversed_string += x

    return reversed_string

# def missing_number(array: list[int]):
#     n = len(array) + 1
#     actual_sum = sum(array)
#     expected_sum =  
            
def Palindrome(string: str):
    string = string.lower().replace(' ', '').replace(',', '').replace(':', '')
    if string[::-1] == string:
        return True
    return False

def fizz_buzz(n: int):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def two_sum(array: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(array):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def function():
    try:
        return float('hello')
    except ValueError:
        return 'invalid type'
       
    

if __name__ == '__main__':
    # print(reverse_string('hello'))
    # print(missing_number([1, 2, 4, 5, 6]))
    # print(Palindrome('A man, a plan, a canal: Panama'))

    # fizz_buzz(15)
    # print(two_sum([2, 7, 11, 15], 9))
    print(function())


'''

'''
print('..Ваше решение:....')

def print_numbers(last_number):
    i = 0
    number = last_number
    while i < last_number: # <= привязка к last_number, как в примере - сбило с толку, а надо было i > 0
        print(number) 
        number = number - 1
        i = i + 1
    print('finished!')
print_numbers(4)

print('..Решение учителя:....')

def print_numbers(last_number):
    i = last_number
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')
print_numbers(4)

print('=======================================================')
'''
# Python: Цикл While
print('... 1 ...\n')

def print_hello(n):
    counter = 0
    while counter < n:
        print('Hello!')
        counter = counter + 1
print_hello(3)
print('... 2 ...\n')

def print_numbers(last_number):
    i = 1
    while i <= last_number:
        print(i)
        i = i + 1
    print('finished!')

print_numbers(4)
print('... ... ... ... ...\n')

def print_numbers(number):
    i = number
    while i  > number: # <= условие
        print('i') 
        i = i - 1
    print('finished!')
print_numbers(5)
'''
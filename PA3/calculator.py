# assignment: programming assignment 3
# author: Michael Coe
# date: 11/3/2020
# file: calculator.py is a program that emulates a simple
# calculator that can add, subtract, multiply or divide two numbers
# input: integers and floats
# output: interactive messages

# returns True if argument is a valid float
def isfloat(token):
    dot = False
    minus = False
    for char in token:
        if char.isdigit():  # allow many digits in a string
            continue
        elif char == ".":  # allow only one dot in a string
            if not dot:
                dot = True
            else:
                return False
        elif char == "-" and token[0] == "-":  # allow one minus in front
            if not minus:
                minus = True
            else:
                return False
        else:  # do not allow any other characters in a string
            return False
    return True


# formats number to 2 decimal points and eliminates extra zeros
def format(num, precision=2):
    num = str(round(num, precision))
    while (num[-1] == '0' or num[-1] == '.') and not (num == '-0') and not num.isdigit():
        num = num[:len(num) - 1]
    if num == '-0':
        num = '0'
    return num

# completes basic addition and prints result
def add(num1, num2):
    sums = float(num1) + float(num2)
    print(f'{num1} + {num2} = {format(sums)}')


# completes basic subtraction and prints result
def subtract(num1, num2):
    dif = float(num1) - float(num2)
    print(f'{num1} - {num2} = {format(dif)}')


# completes basic multiplication and prints result
def multiply(num1, num2):
    product = float(num1) * float(num2)
    print(f'{num1} x {num2} = {format(product)}')


# completes basic division and prints result
def divide(num1, num2):
    quotient = float(num1) / float(num2)
    print(f'{num1} / {num2} = {format(quotient)}')


# program start!
done = False
print('Welcome to Calculator Program!')
while done == False:
    mathtype = 'g'
    while 'aAsSmMdD'.find(mathtype) == -1 or len(mathtype) != 1:
        mathtype = input('''Please choose one of the following operations:
Addition - A
Subtraction - S
Multiplication - M
Division - D
>
''')
        # decides math type
        if mathtype == "A" or mathtype == 'a':
            print('You chose addition.')
        elif mathtype == "S" or mathtype == 's':
            print('You chose subtraction.')
        elif mathtype == "M" or mathtype == 'm':
            print('You chose multiplication.')
        elif mathtype == "D" or mathtype == 'd':
            print('You chose division.')
        else:
            print('You did not choose a valid operator.')

    # makes sure first number is a number
    num1 = input('Please enter the first number:\n')
    while not isfloat(num1):
        num1 = input('''You did not choose a number.
        Please enter the first number:
        ''')
    num1 = format(float(num1))
    print(f'The first number is {num1}.')
    # makes sure second number is a number
    num2 = input('Please enter the second number:\n')
    while not isfloat(num2):
        num2 = input('''You did not choose a number.
        Please enter the second number:
        ''')
    num2 = format(float(num2))
    print(f'The second number is {num2}.')

    # executes the math operation
    if mathtype == "A" or mathtype == 'a':
        add(num1, num2)
    elif mathtype == "S" or mathtype == 's':
        subtract(num1, num2)
    elif mathtype == "M" or mathtype == 'm':
        multiply(num1, num2)
    elif mathtype == "D" or mathtype == 'd':
        if num2 == '0':
            print('The division by zero is prohibited!')
        else:
            divide(num1, num2)
    # asks user if they wish to continue using the program
    isdone = input('Do you want to continue? [Y/N]:\n')
    if isdone == 'N' or isdone == 'n':
        done = True
        print('Goodbye!')

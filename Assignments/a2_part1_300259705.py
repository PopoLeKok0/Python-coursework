import math
import random

def elementary_school_quiz(flag, n):
    '''
    (int,int) -> string
    Preconditions: flag is 0 or 1, n is 1 or 2.
    Prompts the person for the answer, checks if their answer is correct and returns the number of questions answered correctly.
    '''
    a = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    b = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if flag == 0 and n == 1:
        print('Question 1:')
        c = input("2 to what is " + str(2 ** a) + " i.e. what is the result of log_2(" + str(2 ** a) + ")" + "? ")
        if a == math.log2(2 ** float(c)):
            print('1')
        else:
            print('0')

    if flag == 0 and n == 2:
        print('Question 1:')
        d = input("2 to what is " + str(2 ** a) + " i.e. what is the result of log_2(" + str(2 ** a) + ")" + "? ")
        print('Question 2:')
        e = input("2 to what is " + str(2 ** b) + " i.e. what is the result of log_2(" + str(2 ** b) + ")" + "? ")

        if a == math.log2(2 ** float(d)) and b == math.log2(2 ** float(e)):
            print('2')
        elif a == math.log2(2 ** float(d)) or b == math.log2(2 ** float(e)):
            print('1')
        else:
            print('0')

    if flag == 1 and n == 1:
        print('Question 1:')
        f = input("What is the result of 2^" + str(a) + "? ")
        if math.log2(float(f)) == a:
            print('1')
        else:
            print('0')

    if flag == 1 and n == 2:
        print('Question 1:')
        g = input("What is the result of 2^" + str(a) + "? ")
        print('Question 2:')
        k = input("What is the result of 2^" + str(b) + "? ")
        if math.log2(float(g)) == a and math.log2(float(k)) == b:
            print('2')
        elif math.log2(float(g)) == a or math.log2(float(k)) == b:
            print('1')
        else:
            print('0')

def high_school_quiz(a, b, c):
    '''
    (number,number,number) -> string
    Displays correct and meaningful solutions given any three real numbers for coefficients a, b and c.
    '''
    discriminant = b ** 2 - 4 * a * c
    if a == 0 and b == 0 and c == 0:
        print('The quadratic equation ' + str(b) + '·x' + " + " + str(c) + ' = 0')
        print('is satisfied for all numbers x')
    elif a == 0 and b == 0:
        print('The quadratic equation ' + str(b) + '·x' + " + " + str(c) + ' = 0')
        print('is satisfied for no number x')
    elif a == 0:
        print('The linear equation ' + str(b) + '·x' + " + " + str(c) + ' = 0')
        print('has the following root/solution: ' + str((-c / b)))
    else:
        if discriminant > 0:
            x_1 = ((-b + math.sqrt(discriminant)) / (2 * a))
            x_2 = ((-b - math.sqrt(discriminant)) / (2 * a))
            print('The quadratic equation ' + str(a) + '·x^2' + " + " + str(b) + '·x' + " + " + str(c) + ' = 0')
            print('has the following real roots:\n' + str(x_1) + " and " + str(x_2))
        elif discriminant < 0:
            x_3 = str((-b) / (2 * a)) + " + i " + str(math.sqrt(-(discriminant)) / (2 * a))
            x_4 = str((-b) / (2 * a)) + " - i " + str(math.sqrt(-(discriminant)) / (2 * a))
            print('The quadratic equation ' + str(a) + '·x^2' + " + " + str(b) + '·x' + " + " + str(c) + ' = 0')
            print('has the following two complex roots:\n' + str(x_3) + " \n and \n" + str(x_4))
        elif discriminant == 0:
            x = (-b) / (2 * a)
            print('The quadratic equation ' + str(a) + '·x^2' + " + " + str(b) + '·x' + " + " + str(c) + ' = 0')
            print('has only one solution, a real root:\n' + str(x))
        elif a == 0:
            print('The quadratic equation ' + str(b) + '·x' + " + " + str(c) + ' = 0')
            print('has the following root/solution: ' + str((-b / a)))

print(5 * "*" + len(" __Welcome to my math quiz-generator__") * "*")
print("*" + 4 * " " + len("__Welcome to my math quiz-generator__") * " " + "*")
print("*  " + "__Welcome to my math quiz-generator__" + "  *")
print("*" + 4 * " " + len("__Welcome to my math quiz-generator__") * " " + "*")
print(5 * "*" + len("__Welcome to my math quiz-generator__") * "*" + "*")

name = input("What is your name? ")

status = input("Hi " + name + ". Are you in? Enter \n1 for elementary school\n2 for high school\n3 or other character(s) for none of the above?\n")

if status == '1':

    print(5 * "*" + len("_" + name + ", welcome to my quiz-generator for elementary school students.__") * "*" + 2 * "*")
    print("*" + 4 * " " + len("_" + name + ", welcome to my quiz-generator for elementary school students.__") * " " + " " + "*")
    print("*  " + 2 * "_" + str(name) + ", welcome to my quiz-generator for elementary school students.__" + "  *")
    print("*" + 4 * " " + len("_" + name + ", welcome to my quiz-generator for elementary school students.__") * " " + " " + "*")
    print(5 * "*" + len("_" + name + ", welcome to my quiz-generator for elementary school students.__") * "*" + 2 * "*")
    flag = int(input('what would you like to practice? Enter\n0 for inverse of exponentiation\n1 for exponentiation\n'))
    if flag != 0 and flag != 1:
        print('Invalid chose. Only 0 or 1 is accepted.')
    else:

        n = int(input('How many practice questions would you like to do? Enter 0, 1, or 2: '))
        if n == 0:
            print('Zero questions. OK. Good bye')
        elif (n == 0 or n == 1 or n == 2) and (flag == 0 or flag == 1):
            elementary_school_quiz(flag, n)
        elif (n != 0 and n != 1 or n != 2) and (flag == 0 or flag == 1):
            print('Only 0,1, or 2 are valid choices for the number of questions.')


elif status == '2':
    print(4 * "*" + len(" __quadratic equation, a·x^2 + b·x + c= 0, solver for " + str(name) + "__") * "*" + "*")
    print("*" + 3 * " " + len(" __quadratic equation, a·x^2 + b·x + c= 0, solver for " + str(name) + "__") * " " + "*")
    print("* " + " __quadratic equation, a·x^2 + b·x + c= 0, solver for " + str(name) + "__" + "  *")
    print("*" + 3 * " " + len(" __quadratic equation, a·x^2 + b·x + c= 0, solver for " + str(name) + "__") * " " + "*")
    print(4 * "*" + len(" __quadratic equation, a·x^2 + b·x + c= 0, solver for " + str(name) + "__") * "*" + "*")
    flag = True
    while flag:
        question = input(name + ", would you like a quadratic equation solved? ")
        question = str.strip(str.lower(question))
        "yes" in question
        if question != "yes":
            flag = False
        else:
            print("Good choice!")
            a = int(input("Enter a number the coefficient a: "))
            b = int(input("Enter a number the coefficient b: "))
            c = int(input("Enter a number the coefficient c: "))
            high_school_quiz(a, b, c)
else:
    print("Ah\n" + str(name) + " you are not a target audience for this software.")

print("Good bye " + name + "!")
        

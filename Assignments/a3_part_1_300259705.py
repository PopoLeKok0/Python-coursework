def split_tester_helper_1(N, d):
    '''
    (str,str) -> None
    '''
    for i in range(0, len(N) - int(d), int(d)):
        a = N[i:i + int(d)]
        print(a, end=', ')
    print(N[len(N) - int(d):len(N)])


def split_tester_helper_2(N, d):
    '''
    (str,str) -> False or None
    '''
    for i in range(0, len(N), int(d)):
        a = N[i:i + int(d)]
        if a == N[len(N) - int(d):len(N)]:
            break
        else:
            pass
        b = N[i + int(d):i + 2 * int(d)]
        if int(b) > int(a):
            pass
        else:
            return False


def split_tester(N, d):
    '''
    (str,str) -> bool()
    Preconditions: These two strings should be such that each looks like a positive integer and such that the
    number of digits in N is divisible by the integer represented by d.
    return True if the sequences is strictly increasing and False otherwise.
    '''
    split_tester_helper_1(N, d)
    if len(N) % int(d) == 0:
        pass
    elif len(N) % int(d) != 0:
        return False
    if split_tester_helper_2(N, d) == False:
        return False
    else:
        return True


print(5 * "*" + len("__Welcome to my increasing-splits tester__") * "*" + 2 * "*")
print("*" + 4 * " " + len("__Welcome to my increasing-splits tester__") * " " + " " + "*")
print("*  " + "__Welcome to my increasing-splits tester__" + "   *")
print("*" + 4 * " " + len("__Welcome to my increasing-splits tester__") * " " + " " + "*")
print(5 * "*" + len("__Welcome to my increasing-splits tester__") * "*" + 2 * "*")

name = input('What is your name? ')
print(5 * "*" + len("_" + str.strip(name) + ", welcome to my increasing-splits tester.__") * "*" + 2 * "*")
print("*" + 4 * " " + len("_" + str.strip(name) + ", welcome to my increasing-splits tester.__") * " " + " " + "*")
print("*  " + 2 * "_" + str.strip(str(name)) + ", welcome to my increasing-splits tester.__" + "  *")
print("*" + 4 * " " + len("_" + str.strip(name) + ", welcome to my increasing-splits tester.__") * " " + " " + "*")
print(5 * "*" + len("_" + str.strip(name) + ", welcome to my increasing-splits tester.__") * "*" + 2 * "*")

flag = True
while flag:
    question = input(str.strip(name) + ", would you like to test if a number admits an increasing-split of give size? ")
    question = (question.strip()).lower()
    if question == 'no':
        flag = False
        print(5 * "*" + len(" __Good bye " + str.strip(name) + "!_") * "*" + 2 * "*")
        print("*" + 4 * " " + len(" __Good bye " + str.strip(name) + "!_") * " " + " " + "*")
        print("* " + " __Good bye " + str.strip(name) + "!" + 2 * "_" + "   *")
        print("*" + 5 * " " + len(" __Good bye " + str.strip(name) + "!_") * " " + "*")
        print(5 * "*" + len(" __Good bye " + str.strip(name) + "!_") * "*" + 2 * "*")
        break

    elif question == 'yes':
        flag == True
        print('Good choice!')
        N = str.strip(input('Enter a positive integer: '))
        if N.isalpha() or '.' in N:
            print('The input can only contain digits. Try again.')


        elif int(N) <= 0:
            print('The input has to be a positive integer.Try again.')

        if not (N.isalpha() or '.' in N) and int(N) > 0:
            d = str.strip(input('Input the split. The split has to divide the length of ' + str(N) + ' i.e. ' + str(len(N)) + '\n'))
            if d.isalpha() or '.' in d:
                print('The input can only contain digits. Try again.')
            if not (d.isalpha() or '.' in d):
                if int(d) <= 0:
                    print('The input has to be a positive integer.Try again.')
            if not (d.isalpha() or '.' in d):
                if int(d) > 0:
                    if len(N) % int(d) != 0:
                        print(str(d) + " does not divide " + str(len(N)) + '. Try again.')

            if not (N.isalpha() or '.' in N) and int(N) > 0 and not (d.isalpha() or '.' in d) and len(N) % int(d) == 0:
                if int(d) > 0:
                    if split_tester(N, d) == True:

                        print('the sequence is increasing')

                    else:
                        print('the sequence is not increasing')

    else:
        print('Please enter yes or no. Try again.')

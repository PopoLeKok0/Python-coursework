########################
# Question 2.1
########################

def sum_odd_divisors(n):
    '''
    (int) -> int or None
    returns the sum of all the postive odd divisors of n.
    '''
    if n == 0:
        return None
    else:
        sum_i = 0
        for i in range(1, abs(n) + 1):
            x = abs(n) % i
            if x == 0 and i % 2 != 0:
                sum_i += i
        return sum_i


########################
# Question 2.2
########################

def series_sum():
    '''
    (None) -> number
    prompts the user for an non-negative integer n. If the user enters a negative
    integer the function should return None otherwise the function should return the sum of the following series
    1000 + 1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ... + 1/n2 for the given integer n.
    '''
    y = int(input('Please enter a non-negative integer: '))
    sum_ = 0
    for i in range(1, y + 1):
        x = 1 / i ** 2
        sum_ += x
    return sum_ + 1000


########################
# Question 2.3
########################

def pell(n):
    '''
    (int) -> (int) or None
    If n is negative, pell returns None. Else, pell returns the nth Pell number.
    '''
    if n == 0 or n == 1 or n == 2:
        return n
    elif n < 0:
        return None
    else:
        Pn_1 = 2
        Pn_2 = 1
    for i in range(3, n + 1):
        Pn = 2 * Pn_1 + Pn_2
        Pn_2 = Pn_1
        Pn_1 = Pn_2
        Pn_1 = Pn
    return Pn


########################
# Question 2.4
########################

def e_to_j_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'efghij':
            counter += 1
    return counter


def F_to_X_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'FGHIJKLMNOPQRSTUVWX':
            counter += 1
    return counter


def two_to_six_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in '23456':
            counter += 1
    return counter


def others_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in '\!,':
            counter += 1
    return counter


def countMembers(s):
    '''
    (str) -> int
    returns the number of characters in s, that are extraordinary.
    '''
    return e_to_j_counter(s) + F_to_X_counter(s) + others_counter(s) + two_to_six_counter(s)


########################
# Question 2.5
########################

def casual_number(s):
    '''
    (str) -> int or None
    return an integer representing a number in s.
    If s does not look like a number the function should return None.
    '''
    the_number = ''
    for ch in s:
        if ch == ",":
            pass
        elif ch in "-0123456789":
            the_number += ch
        else:
            return None
    if the_number == '-' or '--' in the_number:
        return None
    else:

        return int(the_number)


########################
# Question 2.6
########################

T = 1024
y = 598
ex_mark = 121
a = 42
N = 6
U = 1


def T_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'T':
            counter += 1
    return counter


def y_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'y':
            counter += 1
    return counter


def ex_mark_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in '!':
            counter += 1
    return counter


def a_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'a':
            counter += 1
    return counter


def N_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'N':
            counter += 1
    return counter


def U_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'U':
            counter += 1
    return counter


def alienNumbers(s):
    '''
    (str) -> int
    returns the integer value represented by s.
    '''
    return T_counter(s) * T + y_counter(s) * y + ex_mark_counter(s) * ex_mark + a_counter(s) * a + N_counter(
        s) * N + U_counter(s) * U


########################
# Question 2.7
########################

T = 1024
y = 598
ex_mark = 121
a = 42
N = 6
U = 1


def T_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'T':
            counter += 1
    return counter


def y_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'y':
            counter += 1
    return counter


def ex_mark_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in '!':
            counter += 1
    return counter


def a_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'a':
            counter += 1
    return counter


def N_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'N':
            counter += 1
    return counter


def U_counter(s):
    '''
    (str) -> int
    '''
    counter = 0
    for char in s:
        if char in 'U':
            counter += 1
    return counter


def alienNumbers(s):
    '''
    (str) -> int
    returns the integer value represented by s.
    '''
    return T_counter(s) * T + y_counter(s) * y + ex_mark_counter(s) * ex_mark + a_counter(s) * a + N_counter(
        s) * N + U_counter(s) * U


########################
# Question 2.8
########################

def encrypt(s):
    '''
    (str) -> str
    returns a string which is the encrypted version of s.
    '''
    if len(s) <= 1:
        return s
    reversed_sentence_incomplete = ''
    ns = ''
    for i in range(len(s) - 1):
        reversed_sentence_incomplete += s[len(s) - 1 - i]
        reversed_sentence = reversed_sentence_incomplete + s[0]
        first_pair = reversed_sentence[0] + reversed_sentence[len(reversed_sentence) - 1]
    if len(s) % 2 == 0:
        for i in range(1, len(reversed_sentence) - 1):
            ns += reversed_sentence[i] + reversed_sentence[len(reversed_sentence) - (i + 1)]
            if s[int(len(s) / 2 - 1)] in ns:
                break
    elif len(s) == 3:
        for i in range(1, len(reversed_sentence) - 1):
            ns = s[1]
    elif len(s) % 2 != 0:
        for i in range(1, len(reversed_sentence) - 1):
            ns += reversed_sentence[i] + reversed_sentence[len(reversed_sentence) - (i + 1)]
            if reversed_sentence[len(reversed_sentence) - 2] in ns:
                break
    if len(s) % 2 == 0 or len(s) == 3:
        return first_pair + ns
    else:
        return first_pair + ns + reversed_sentence[int((len(reversed_sentence) - 1) / 2)]


########################
# Question 2.9
########################

def oPify(s):
    '''
    (str) -> str
    returns a string with the letters o and p inserted between every pair of consecutive characters of s.
    '''
    sentence = ''
    first_pair = ''
    if len(s) == 2:
        for i in range(len(s) - 1):
            if s[i].isalpha() and s[i + 1].isalpha():
                if s[i].isupper() and s[i + 1].isupper():
                    sentence += s[i] + 'OP' + s[i + 1]
                elif s[i].isupper() == False and s[i + 1].isupper() == False:
                    sentence += s[i] + 'op' + s[i + 1]
                elif s[i].isupper() == False and s[i + 1].isupper():
                    sentence += s[i] + 'oP' + s[i + 1]
                elif s[i].isupper() and s[i + 1].isupper() == False:
                    sentence += s[i] + 'Op' + s[i + 1]
            else:
                sentence += s[i] + s[i + 1]
    elif len(s) % 2 == 0:
        for i in range(len(s)):
            if s[i].isalpha() and s[i + 1].isalpha():
                if s[i].isupper() and s[i + 1].isupper():
                    sentence += s[i] + 'OP'
                elif s[i].isupper() == False and s[i + 1].isupper() == False:
                    sentence += s[i] + 'op'
                elif s[i].isupper() == False and s[i + 1].isupper():
                    sentence += s[i] + 'oP'
                elif s[i].isupper() and s[i + 1].isupper() == False:
                    sentence += s[i] + 'Op'
            else:
                sentence += s[i]

    elif len(s) == 3:
        for i in range(0, 1):
            if s[0].isalpha() and s[1].isalpha():
                if s[0].isupper() and s[1].isupper():
                    first_pair += s[0] + 'OP'
                elif s[0].isupper() == False and s[1].isupper() == False:
                    first_pair += s[0] + 'op'
                elif s[0].isupper() == False and s[1].isupper():
                    first_pair += s[0] + 'oP'
                elif s[0].isupper() and s[i + 1].isupper() == False:
                    first_pair += s[0] + 'Op'
            else:
                first_pair += s[0]

        for i in range(1, len(s) - 1):
            if s[i].isalpha() and s[i + 1].isalpha():
                if s[i].isupper() and s[i + 1].isupper():
                    sentence += s[i] + 'OP' + s[i + 1]
                elif s[i].isupper() == False and s[i + 1].isupper() == False:
                    sentence += s[i] + 'op' + s[i + 1]
                elif s[i].isupper() == False and s[i + 1].isupper():
                    sentence += s[i] + 'oP' + s[i + 1]
                elif s[i].isupper() and s[i + 1].isupper() == False:
                    sentence += s[i] + 'Op' + s[i + 1]
            else:
                sentence += s[i] + s[i + 1]
    elif len(s) % 3 == 0:
        for i in range(len(s) - 1):
            if s[i].isalpha() and s[i + 1].isalpha():
                if s[i].isupper() and s[i + 1].isupper():
                    sentence += s[i] + 'OP'
                elif s[i].isupper() == False and s[i + 1].isupper() == False:
                    sentence += s[i] + 'op'
                elif s[i].isupper() == False and s[i + 1].isupper():
                    sentence += s[i] + 'oP'
                elif s[i].isupper() and s[i + 1].isupper() == False:
                    sentence += s[i] + 'Op'
            else:
                sentence += s[i]
    if len(s) == 3 or len(s) == 2 or len(s) % 2 == 0:
        return first_pair + sentence
    else:
        return first_pair + sentence + s[len(s) - 1]


########################
# Question 2.10
########################

def nonrepetitive_tester(s):
    '''
    (str) -> False or None
    '''
    for k in range(1, len(s)):
        for i in range(k, len(s)):
            a = s[(i - k):i]
            b = s[i:(i + k)]
            if a != b:
                pass
            elif a == b:
                return False


def nonrepetitive(s):
    '''
    (str) -> bool()
    returns True if s is nonrepetitive and False otherwise.
    '''
    if len(s) < 2:
        return True
    elif len(s) == 2:
        if s[0] == s[1]:
            return False
        else:
            return True
    elif len(s) > 2:
        if nonrepetitive_tester(s) == False:
            return False
        else:
            return True


        
        
    
    
    
       

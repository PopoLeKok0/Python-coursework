########################
# Question 1
########################

import math

def min_enclosing_rectangle(radius, x, y):
    '''
    (number,number,number) -> (number,number)
    Return the x- and y-coordinates of the bottom-left corner of the smallest rectangle that contains a circle.
    Precondition: the radius should be positive or else the function returns None.
    '''
    x_ = x - radius
    y_ = y - radius

    if (radius >= 0 and x >= radius and y >= radius):
        return x_, y_
    elif (radius >= 0 and x <= radius and y >= radius):
        return x_, -y_
    elif (radius >= 0 and x >= radius and y <= radius):
        return x_, y_
    elif (radius >= 0 and x <= radius and y <= radius):
        return x_, y_
    else:
        return None

########################
# Question 2
########################

import math

def vote_percentage(results):
    '''
    (str) -> float
    Returns the percentage of ’yes’ (among all ’yes’ and ’no’).
    Preconditions: enter at least one 'yes' or 'no', and only enter 'yes', 'no' and/or abstained.
    '''
    a = results.count('yes')
    b = results.count('no')
    c = a + b
    a_ = (a / c)
    return a_

########################
# Question 3
########################

def vote():
    '''
    () -> None
    Prints the outcome of the vote.
    Preconditions: enter at least one 'yes' or 'no', and only enter 'yes', 'no' and/or abstained.
    '''
    results = input('Enter the yes, no, abstained votes one by one and then press enter:\n ')
    p = vote_percentage(results)
    if p == 1:
        print('proposal passes unanimously')
    elif p >= 2 / 3:
        print('proposal passes with super majority')
    elif p >= 1 / 2:
        print('proposal passes with simple majority')
    else:
        print('proposal fails')

########################
# Question 4
########################

import math
def l2lo(w):
    '''
    number -> (number,number)
    Returns a pair of numbers (l,o) such that w = l + o/16.
    Precondition: w>=0
    '''
    l=int(w)
    o=16*(w-l)
    return l,o








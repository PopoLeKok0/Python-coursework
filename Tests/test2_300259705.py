'''
I understand the importance of professional integrity in my education and future career
in engineering or computer science. I hereby certify that I have done and will do all work
on this examination entirely by myself, without outside assistance or the use of unauthorized
information sources. Furthermore, I will not provide assistance to others.
'''

# READ THE ABOVE STATEMENT
#
# Mouad Ben lahbib 300259705
#
# By putting your name here you are signing the statement above and
# agreeing to the TEST 2 (integrity rules) listed on the first page of the test

#########################
# QUESTION 1:
#########################

# Why does the code in the image crash? You must answer in plain English.
# Answers resembling Python's error messages will not be accepted.
# Put your answer on the line below that starts with #.
# Your answer must not have more than 15 words.

# because list.sort() returns None, can't be printed. Unlike sorted() that returns a new sorted list.


    
# QUESTION 2A)
#########################

# How many stars does the program print when expressed in terms of big O notation?
#
# A) O(1)
# B) O(log n)
# C) O(n^{1/3})
# D) O(n)
# E) O(n*log n)
# F) O(n^2)

# Choose the most accurate answer by
# writing A, B, C, D, E or F for your answer in the comment below this line:
#D


#########################
# QUESTION 2B)
#########################

# How many dollar signs does the program print when expressed in terms of big O notation?
#
# A) O(1)
# B) O(log n)
# C) O(n^{1/3})
# D) O(n)
# E) O(n*log n)
# F) O(n^2)

# Choose the most accurate answer by
# writing A, B, C, D, E or F for your answer in the comment below this line:
#C

#########################
# QUESTION 3
#########################

def nyasa(L):
    '''list of str->int

    Precondition: len(L)>0 and no two words in L are the same
    
    Returns the number of pairs of words in L that have the same length

    For example, in a list ["rat", "war", "sol", "ads"] the answer is 6 since
    all possible pairs of given words have the same length:
    "rat" and "war", "rat" and "sol", "rat" and "ads",
    "war" and "sol", "war" and "ads" and "sol" and "ads"
    
    >>> nyasa(["rat", "war", "sol", "ads"])
    6
    >>> nyasa(["rat", "jazzy", "war", "solei", "pizza"])
    4
    >>> nyasa(["at", "jazz", "war", "solei"])
    0
    '''
    counter=0
    for i in range(len(L)):
        for d in range(i+1,len(L)):
            if (len(L[i])==len(L[d])):
                counter+=1
    
    return counter
            

#########################
# QUESTION 4
#########################
def baikal(L):
    '''(list of int) -> bool
    Preconditions: len(L)>=2

    The function should return True if 
    1st and 2nd element differ by 1, and
    2nd and 3rd element differ by 2, and
    3rd and 4th element differ by 3, and 
    ...
    (n-1)st and nth element differ by (n-1)
    Otherwise it returns False.

    For example, for a list [4,5,3,0,-4] the function should return True
    since 4 and 5 differ by 1; and, 5 and 3 differ by 2; and, 3 and 0 differ by 3;
    and 0 and -4 differ by 4.

    For example, for a list [4,5,-7] the function should return False
    since 4 and 5 differ by 1; but 5 and -7 differ by 12 (and it should be 2)

    >>> baikal([4,5,3,0,-4])
    True
    >>> baikal([4,5,-7])
    False'''
    for i in range(len(L)):
        if (abs(int(L[i])-int(L[i+1]))==1) and (abs(int(L[i+1])-int(L[i+2]))==2) and (abs(int(L[i+2])-int(L[i+3]))==3):
            return True
        else:
            return False
        


#########################
# QUESTION 5
#########################            
    
def tanganyika(L):
    '''(list of int)->list

    Precondition: len(L)>=1
    This function should return a new list Q where Q should be the same as L
    except that where ever L has multiple zeros in a row Q should have only one zero.
    >>> tanganyika([1,2,0,0,0,3,0])
    [1, 2, 0, 3, 0]
    >>> tanganyika([1,2,0,0,0,3,0,0,0,0])
    [1, 2, 0, 3, 0] 
    >>> tanganyika([0,0,1,0,2,0,0,0,3,0,0,0,0])
    [0, 1, 0, 2, 0, 3, 0]
    >>> tanganyika([1,2,0,3,0])
    [1, 2, 0, 3, 0]
    '''
    Q=[]
    for i in range(len(L)):
       if L[i-1]==L[i]==0:
           pass
       else :
           Q.append(L[i])
    
    return Q


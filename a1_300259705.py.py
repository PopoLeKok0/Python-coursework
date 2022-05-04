# Family name: Mouad Ben lahbib
# Student number: 300259705
# Course: IT1 1120
# Assignment Number 1
# year 2021

########################
# Question 1
########################

import math
def ms2kh(s):
    '''
    (number) -> number
    Returns the speed expressed in kilometres/hour given the same speed, s, expressed in miles/hour.
    '''
    kilometers_per_hour = s*1.60934
    return kilometers_per_hour

########################
# Question 2
########################

import math

def pythagorean_pair(a,b):
   '''
   (int,int) -> bool
   Returns True if a and b are pythagorean pair and False otherwise.
   '''
   c = math.sqrt(int(a)* int(a) + int(b)* int(b))
   a = math.sqrt(int(c)* int(c) - int(b)* int(b))
   b = math.sqrt(int(c)* int(c) - int(a)* int(a))
   return c == int(c)

########################
# Question 4
########################

def safe(n):
    '''
    int -> bool
    Preconditions: n>=0
    Returns True if n (a 2 digits number) is safe (does not contain a 9 as a digit, and cannot be divided by 9) and False otherwise.
    '''
    s=str(n)
    return not '9' in s and not n%9==0

########################
# Question 5
########################

def quote_maker(quote,name,year):
    '''
    (str,str,str) -> str
    Returns a sentence, of the following form: In year, a person called name said: “quote”.
    '''
    return "In "+ str(year)+", a person called " + name + " said: " +'"' + quote + '"'

########################
# Question 6
########################

def quote_maker(quote, name, year):
    return "In " + str(year) + ", a person called " + name + " said: " + '"' + quote + '"'

def quote_displayer():
    '''
    () -> none
    Prompts the user for a quote, name, and year, then prints a sentence using the same format as specified in the previous question.
    '''
    quote = input('Give me a quote: ')
    name = input('Who said that?: ')
    year = input('What year did she/he say that? ')
    print(quote_maker(quote, name, year))

########################
# Question 7
########################

def rps_winner():
    '''
    () -> str
    Prompts the user for choice of player 1 and then choice of player 2, and then it displays the result for player 1.
    Enter words (rock,paper,scissors) in lower case.
    '''
    player_1=input("What choice did player 1 make? \nType one of the following options: rock, paper, scissors: ")
    player_2=input("What choice did player 2 make? \nType one of the following options: rock, paper, scissors: ")
    a= print("Player 1 wins. That is "+ str((player_1== "scissors" and player_2== "paper") or (player_1== "paper" and player_2== "rock") or (player_1== "rock" and player_2== "scissors")))
    b= print("It is a tie. That is not "+ str(not(player_1== "paper" and player_2== "paper" or player_1== "scissors" and player_2== "scissors" or player_1== "rock" and player_2== "rock")))
    return a and b

########################
# Question 8
########################

import math
def fun(x):
    '''
    (number) -> number
    preconditions: x>=0
    takes as input a positive number x and solves the following equation for y and returns y. The equation is 10^y=x+3.
    '''
    y= (math.log(x+3))/(4*math.log(10))
    return y

########################
# Question 9
########################

def ascii_name_plaque(x):
    '''
    (str) -> none
    draws a name plaque.
    '''
    print(("*" *(int(len(x))+12)))
    print(("*"+" "*(int(len(x))+10)+"*"))
    print("*"+" "*4+ "_" + x + "_" +" "*4+"*")
    print(("*"+" "*(int(len(x))+10)+"*"))
    print(("*" *(int(len(x))+12)))

########################
# Question 10
########################

import turtle
def draw_train():
    '''
    Draws with Turtle graphics a train.
    '''
    b= print("couldn't finish it :'(")
    return b

########################
# Question 11
########################

import math

def alogical(n):
    '''
    (number) -> int
    Preconditions: n<=1
    Returns the minimum number of times that a number n needs to be devided by 2 in order to get a number <= 1.
    '''
    minimum_times = math.log2(n) + 0.5
    return round(minimum_times)

########################
# Question 12
########################

import math


def cad_cashier(price, payment):

    '''
    (number,number) -> number
    Preconditions: payment>=price
    Returns a real number with 2 decimal places representing the change the customer should get in Canadian dollars.
    '''
    change_not_rounded = payment - price
    change_rounded = round((round(change_not_rounded / 0.05) * 0.05), 2)
    return change_rounded

########################
# Question 13
########################

import math


def cad_cashier(price, payment):
    change_not_rounded = payment - price
    change_rounded = round((round(change_not_rounded / 0.05) * 0.05), 2)
    return change_rounded


def min_CAD_coins(price, payment):
    '''
    (number,number) -> (int,int,int,int,int)
    Preconditions: payment>=price
    Returns five numbers (t,l,q,d,n) that represent the smallest number of coins (toonies, loonies, quarters,dimes, and nickels)
    that add up to the amount owed to the customer).
    '''

    p = cad_cashier(price, payment)

    one_t = 200
    one_l = 100
    one_q = 25
    one_d = 10
    one_n = 5

    t = round(p * 100) // one_t
    l = round(p * 100 - t * one_t) // one_l
    q = round(p * 100 - (l * one_l + t * one_t)) // one_q
    d = round(p * 100 - (q * one_q + l * one_l + t * one_t)) // one_d
    n = round(p * 100 - (d * one_d + q * one_q + l * one_l + t * one_t)) // one_n
    return t, l, q, d, n
    






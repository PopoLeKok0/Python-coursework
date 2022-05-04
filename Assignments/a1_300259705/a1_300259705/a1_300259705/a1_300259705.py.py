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
    kilometers_per_hour = int(s)*1.609344
    return kilometers_per_hour

########################
# Question 2
########################

import math
def pythagorean_pair(a,b):
 c = math.sqrt(int(a)* int(a) + int(b)* int(b))
 a = math.sqrt(int(c)* int(c) - int(b)* int(b))
 b = math.sqrt(int(c)* int(c) - int(a)* int(a))
 return c == int(c)

########################
# Question 8
########################

import math
def fun(x):
    y= (math.log(x+3))/(4*math.log(10))
    return y

########################
# Question 5
########################

def quote_maker(quote,name,year):
    return "In "+ str(year)+", a person called " + name + " said: " +'"' + quote + '"'

########################
# Question 4
########################

def safe(x):
 s=str(x)
 return not '9' in s and not x%9==0

########################
# Question 6
########################

def quote_maker(quote, name, year):
    return "In " + str(year) + ", a person called " + name + " said: " + '"' + quote + '"'

def quote_displayer():
    quote = input('Give me a quote: ')
    name = input('Who said that?: ')
    year = input('What year did she/he say that? ')
    print(quote_maker(quote, name, year))

########################
# Question 9
########################

def ascii_name_plaque(x):
    print(("*" *(int(len(x))+12)))
    print(("*"+" "*(int(len(x))+10)+"*"))
    print("*"+" "*4+ "_" + x + "_" +" "*4+"*")
    print(("*"+" "*(int(len(x))+10)+"*"))
    print(("*" *(int(len(x))+12)))
    
########################
# Question 11
########################

import math
def alogical(n):
    minimum_times= math.log2(n)+0.5
    return round(minimum_times)


''''
I understand the importance of professional integrity in my education and future career
in engineering or computer science. I hereby certify that I have done and will do all work
on this examination entirely by myself, without outside assistance or the use of unauthorized
information sources. Furthermore, I will not provide assistance to others.
'''

# READ THE ABOVE STATEMENT
#
# PUT YOUR NAME AND STUDENT NUMBER HERE
#
#
# By putting your name here you are signing the statement above and
# agreeing to the TEST 3 (integrity rules) listed on the first page of the test


#########################
# QUESTION 1.a
######################### 

#Given a non-empty list L of integers, and given an integer k,
# what does the function thar do?

#(A) It returns True if L is empty and False otherwise.
#(B) It returns True if at least k of the elements of L are positive, and False otherwise.
#(C) It returns True if the first element of L is positive and False otherwise.
#(D) It returns True every k-th element of L is positive, starting with 1st.
#(E) It returns True if the first element and the k-th element of L are positive and False otherwise.
#(F) This program goes into infinite loop.
#
# WRITE A, B, C, D, E or F for YOUR ANSWER ON THE NEXT LINE
#E

#########################
# QUESTION 1.b
#########################

# What is the hight of recursion of function thar? Below n=len(L).
# Pick the most correct answer
# (A) O(1)
# (B) O(log n)
# (C) O(log(n/k))
# (D) O(n/k)
# (E) O(n)

# WRITE A, B, C, D, or E for YOUR ANSWER ON THE NEXT LINE
#E

#########################
# QUESTION 2
#########################

class Date:
    def __init__(self,day=1,month=1):
        self.day=day
        self.month=month
    def __repr__(self):
        return 'Date('+str(self.day)+', '+str(self.month)+')'
    def __str__(self):
        return 'Day: '+str(self.day)+', '+'Month: '+str(self.month)
    def days_in_month(self):
        if self.month==1 or self.month==3 or self.month==5 or self.month==7 or self.month==8 or self.month==10 or self.month==12:
            return 31
        elif self.month==2:
            return 28
        else:
            return 30
    def bogus(self):
        if self.month==0 or self.day==0:
            return True
        elif self.month>12 or self.day>self.days_in_month():
            return True
        else: return False
    def __lt__(self,other):
        if self.month<other.month:
            return True
        elif self.month>other.month:
            return False
        elif self.month==other.month:
            if self.day<other.day:
                return True
            else:
                return False
            
        
'''
>>> d1=Date(13, 5)
>>> d1
Date(13, 5)
>>> print(d1)
Day: 13, Month: 5
>>> d2=Date()
>>> d2
Date(1, 1)
>>> print(d2)
Day: 1, Month: 1
>>> d1.days_in_month()
31
>>> d3=Date(11,2)
>>> print(d3)
Day: 11, Month: 2
>>> d3.days_in_month()
28
>>>
>>> d1.bogus()
False
>>> d2.bogus()
False
>>> d3.bogus()
False
>>> d4=Date(13,14)
>>> d4.bogus()
True
>>> d5=Date(0,5)
>>> d5.bogus()
True
>>> d6=Date(29,2)
>>> d6.bogus()
True
>>>
>>> d1=Date(17, 12)
>>> d2=Date(29, 12)
>>> d1<d2
True
>>> d2>d1
True
>>> d3=Date(30, 4)
>>> d3<d1
True
'''

class Month:
    def __init__(self,month):
        self.month=month
    def days():
        lis=[]
        i=0
        while i>=Date.days_in_month(2):
              i+=1
              lis.append('Date('+str(i)+', '+str(self.month)+')')
        return lis
            
    

'''
>>> m=Month(2)
>>> m.days
[Date(1, 2), Date(2, 2), Date(3, 2), Date(4, 2), Date(5, 2), Date(6, 2), Date(7, 2), Date(8, 2), Date(9, 2), Date(10, 2), Date(11, 2), Date(12, 2), Date(13, 2), Date(14, 2), Date(15, 2), Date(16, 2), Date(17, 2), Date(18, 2), Date(19, 2), Date(20, 2), Date(21, 2), Date(22, 2), Date(23, 2), Date(24, 2), Date(25, 2), Date(26, 2), Date(27, 2), Date(28, 2)]
>>> len(m)
28
>>> 
>>> r=Month(5)
>>> r.days
[Date(1, 5), Date(2, 5), Date(3, 5), Date(4, 5), Date(5, 5), Date(6, 5), Date(7, 5), Date(8, 5), Date(9, 5), Date(10, 5), Date(11, 5), Date(12, 5), Date(13, 5), Date(14, 5), Date(15, 5), Date(16, 5), Date(17, 5), Date(18, 5), Date(19, 5), Date(20, 5), Date(21, 5), Date(22, 5), Date(23, 5), Date(24, 5), Date(25, 5), Date(26, 5), Date(27, 5), Date(28, 5), Date(29, 5), Date(30, 5), Date(31, 5)]
>>> len(r)
31
'''      

#########################
# QUESTION 3
#########################


def atacama(L,n):
    '''(list of int, int) -> dict
    Precondition: n is positive

    >>> atacama([10,1,10,2,10],2)
    {'group 1': 30, 'group 2': 3}
    >>> atacama([0,10,100,1,20,300,2],3)
    {'group 1': 3, 'group 2': 30, 'group 3': 400}
    >>> atacama([1,2,3,4,5,6,7],4)
    {'group 1': 6, 'group 2': 8, 'group 3': 10, 'group 4': 4}
    >>> atacama([20,10,7],5)
    {'group 1': 20, 'group 2': 10, 'group 3': 7, 'group 4': 0, 'group 5': 0}
    >>> atacama([20,10,7],1)
    {'group 1': 37}
    '''
    group_1=0
    group_2=0
    group_3=0
    group_4=0
    group_5=0
    for i in range(0,len(L),n):
        group_1+=L[i]
    if n>1:
        for d in range(1,len(L),n):
            group_2+=L[d]
        if n>2:
            for i in range(2,len(L),n):
                group_3+=L[i]
        if n>3:
            for i in range(3,len(L),n):
                group_4+=L[i]
        if n>4:
            for i in range(4,len(L),n):
                group_5+=L[i]
    dic={'group_1':group_1,'group_2':group_2,'group_3':group_3,'group_4':group_4,'group_5':group_5}
    if dic['group_1']==0:
        del dic['group_1']
    if dic['group_2']==0:
        del dic['group_2']
    if dic['group_3']==0:
        del dic['group_3']
    if dic['group_4']==0:
        del dic['group_4']
    if dic['group_5']==0:
        del dic['group_5']
    if n>4 and ('group_4' not in dic) and ('group_5' not in dic):
        dic['groupe_4']=0
        dic['groupe_5']=0
    return dic
    
    

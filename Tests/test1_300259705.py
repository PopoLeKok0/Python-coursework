'''
I understand the importance of professional integrity in my education and future career
in engineering or computer science. I hereby certify that I have done and will do all work
on this examination entirely by myself, without outside assistance or the use of unauthorized
information sources. Furthermore, I will not provide assistance to others.
'''

#name: Mouad Ben lahbib
#student number: 300259705


def danube(s):
     '''
     (str)-> (str)
     Precondition: s contains only letters A,B,C,F
     '''
     a = s.count('A')
     b = s.count('B')
     c = s.count('C')
     f = s.count('F')
     k = a + b + c + f
     a_ = (a/k)*100
     b_ = (b/k)*100
     c_ = (c/k)*100
     f_ = (f/k)*100
     print(str(a_)+'%, '+str(b_)+'%, '+str(c_)+'%, '+str(f_)+'%, '+'of the students got A, B, C and F respectively.')
     median=s
     if a_ ==100:
         print('Median is A')
     elif b_ ==100:
         print('Median is B')
     elif c_ ==100:
         print('Median is C')
def irtysh(n):
     '''
     (n) -> str
     Preconditions: n=1 or n a positive 5 digit integer
     '''
     pass
     if n==1:
        count=0
        a=input('Enter a positive integer: ')
        count=0
        for i in range(1,int(a)+1):
            x= int(a)% i
            if x==0:
               count+=1
            if count==3:
                return 'True'
            else:
                return 'False'
     elif n!=1:
         b=n%1000//100
         return str(b)

def helper(s1,s2):
    '''
    (str,str) -> str
    Preconditions: s1 and s2 are strings containg digits only
    '''
    if (int(s1)%2==0 and int(s2)%2==0) or (int(s1)%2!=0 and int(s2)%2!=0):
        print(int(s1)+int(s2))
    else :
        print(int(s2)*int(s1))


def yangtze(s):
     '''
     (str) -> (str)
     Preconditions: len(s) is not zero & len(s)%3==0
     and s contains digits only
     '''
     s1=''
     s2=''
     for i in range(len(s)-3):
         n=s[i]
         n_2=s[i+1:i+3]
         s1+=n
         s2+=n_2
     print('the string made of substrings of length one is: '+ s1)
     print('the string made of substrings of length two is: '+ s2)
     helper(s1,s2)

          
 

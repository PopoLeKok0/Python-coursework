import string

def m(i):
    if i==1:
        return 1/3
    elif i==2:
        return 1/3+2/5
    elif i==3:
        return 1/3+2/5+3/7
    else:
        return m(i-1)+i/(2*i+1)
#main
for i in range(1,11):
    print('m(i)= '+str(m(i)))
    
def count_digits(n):
    if n>=0 and n<10:
        return 1
    elif n>=10 and n<100:
        return 2
    elif n>=100 and n<1000:
        return 3
    else:
        return count_digits(n/10)+1
    
def is_palindrome(w):
    w=w.lower()
    n=len(w)
    if n==1:
        return True
    elif n==2:
        if w[0]==w[1]:
            return True
        else:
            return False
    elif n==3:
        if w[0]==w[2]:
            return True
        else:
            return False
    elif n==4:
        if w[0]==w[n-1] and w[1]==w[n-2]:
            return True
        else:
            return False
    else:
        return is_palindrome(w[1:n-1])
    
def make_clean(text):
    '''
    (str)->(str)
    removes punctuation, non-alphabetical words from a text and returns a clean one.
    '''
    for ch in (string.punctuation):
        text=text.replace(ch,'')
    word=text.split(' ')          
    text=list(word)
    while True:
          try:
            text.remove("")
          except ValueError:
            break
    i=-1
    while i<len(text)-1:
        i+=1
        if (text[i].isalpha()==False ):
            text.remove(text[i])
    text=' '.join(text)
    return text

def is_palindrome_v2(w):
    w=make_clean(w)
    d=is_palindrome(w)
    return d
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)


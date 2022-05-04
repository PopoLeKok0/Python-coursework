import string
def is_valid_file_name():
    '''None->str or None'''
    file = None
    try:
        file=input("Enter the name of the file: ").strip()
        file=open(file)
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file=None
    return file 

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    file=None
    while file==None:
        file=is_valid_file_name()
    return file
   
def make_clean(text):
    '''
    (str)->(str)
    removes punctuation, small or non-alphabetical words from a text and returns a clean one.
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
        if (len(text[i])<2 ) or (text[i].isalpha()==False ):
            text.remove(text[i])
    text=' '.join(text)
    return text
def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    dic = {}
    lis=[]
    
    text = fp.read().lower().splitlines()
    for i in range(len(text)):
        text[i]=make_clean(text[i])
        lis.append(text[i].split(' '))
        if '' in lis[i]:
           lis[i].remove('')
        for p in lis[i]:
            if p not in dic:
                dic[p]={i+1}
            else:
                if i+1 in dic[p]:
                    pass
                else:
                    dic[p].add(i+1)
    return dic

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    lis=[]
    Q=list(make_clean(query).split(' '))
    while True:
          try:
            lis.remove("")
          except ValueError:
            break
    for i in range(len(Q)):
        lis.append(D[Q[i]])
    if len(lis)==2 and len(lis[0])==len(lis[0])==1:
        if lis[0]==lis[1]:
            coexistance=lis[0]
        else:
            coexistance='0'
    else:
        for i in range(len(lis)):
            for d in range(len(lis)):
                if lis[i]!=lis[d]:
                   coexistance=list(lis[i].intersection(lis[d]))
                   return coexistance
            coexistance=lis[i]
    return coexistance
def is_in_file(lis):
    '''
    (list)-> bool() or str
    returns True if element in the file, or the element if not.
    '''
    for ch in lis:
        if ch in d:
            pass
        else:
            return ch
    return True
    

##############################
# main
##############################
file=open_file()
d=read_file(file)
l=[]
Flag=True
while Flag==True or Flag==False :
    Flag==True
    query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    a=make_clean(query)
    if query=='q':
       break
    else:
        lis=list(make_clean(query).split(' '))
        if lis==['']:
            if query in string.punctuation or len(query)==0:
               print("Word '' not in the file.")
            else:
               print("Word '"+query+"' not in the file.")
        else:
            while True:
              try:
                lis.remove("")
              except ValueError:
                break
            if is_in_file(lis)==True:
                b=find_coexistance(d,query)
                if find_coexistance(d,query)=='0':
                     print('The one or more words you entered does not coexist in a same line of the file.')
                else:
                    print("The one or more words you entered coexisted in the following lines of the file:")
                    if len(b)==31:
                        print(b[(len(a.split(' '))+1)*2])
                    else:
                        l=[]
                        for ch in find_coexistance(d,query):
                            l.append(ch)
                        l=sorted(l)
                        coex=' '.join(str(x) for x in l)
                        print(coex)
            else:
                print("Word '"+is_in_file(lis)+"' not in the file.")


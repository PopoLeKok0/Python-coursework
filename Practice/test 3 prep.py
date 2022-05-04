def mekong(l1,l2):
    lis=[]
    for i in range(len(l1)-1):
        for d in range(len(l1)):
            for f in range(len(l2)):
                if l1[i]%l2[f]==0 and l1[d]%l2[f]==0:
                    if l1[i]!=l1[d]:
                       lis.append((l1[i],l1[d]))
    lis=list(set([ch for ch in lis]))
    if lis!=[]:
       lis.remove(lis[-1])
    return lis
def split_guesses(l,answer):
    low=[]
    correct=[]
    high=[]
    for i in range(len(l)):
        if l[i]==answer:
            correct.append(l[i])
        elif l[i]<answer:
            low.append(l[i])
        elif l[i]>answer:
            high.append(l[i])
    dic={'low':low,'correct':correct,'high':high}
    if dic['low']==[]:
        del dic['low']
    if dic['correct']==[]:
        del dic['correct']
    if dic['high']==[]:
        del dic['high']
    return dic
def decode(s, dic):
    s2=''
    for ch in s:
        s2+=dic[ch]
    return s2
class Route:
    def __init__(self,start,end,num):
        self.start=start
        self.end=end
        self.num=num
    def modify_num_daily_flights_by(self,new_num):
        self.num+=new_num
    def get(self):
        return self.start
    def __repr__(self):
        return "Route('"+self.start+"', '"+self.end+"',"+str(self.num)+")"
class Airline(Route):
    def __init__(self,name,routes):
        self.name=name
        self.routes=routes
    def multiple_flights(self):
        lis=[]
        for i in range((len(self.routes)-(len(self.routes)//2))):
            for d in range(len(self.routes)):
                if self.routes[i]!=self.routes[d]:
                   if Route.get(self.routes[i])==Route.get(self.routes[d]):
                      lis.append(self.routes[i])
                      lis.append(self.routes[d])
            return lis
                 
#recursive:
def numOnes(n):
     # base case
       if n==0:
          return (0)
       elif n == 1:
          return (1)
     # recursive case
       else:
           return numOnes(n//2)+numOnes(n%2)
def rem(l):
    n=len(l)
    mid=len(l)//2
    if n<=0:
        return []
    elif n=2:
        if l[0]==l[1]:
            return l[0]
    else:
        return rem(1

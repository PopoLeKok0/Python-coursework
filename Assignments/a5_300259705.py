import random
def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    raw_network=[]
    lis=[]
    friends1=[]
    friends.remove(friends[0])
    for i in range(len(friends)):
        a=friends[i].split(' ')
        for s in range(len(a)):
            lis.append(int(a[s]))
    for b in range(len(lis)):
        if lis[b] not in raw_network:
           raw_network.append(lis[b])
    raw_network=sorted(raw_network)
    for n in range(len(raw_network)):
           network.append((raw_network[n],[]))
    for j in range(len(friends)):
        k=friends[j].split(' ')
        friends1.append(k)
    n=len(network)
    n_2=len(friends1)
    for x in range(n):
        w=network[x]
        for c in range(n_2):
            v=friends1[c]
            if v[0]==str(w[0]):
                w[1].append(int(v[1]))
            elif v[1]==str(w[0]):
                w[1].append(int(v[0]))
            else:
                pass
    return network
def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    n=len(network)
    for i in range(n):
        if user1==network[i][0]:
            a=network[i][1]
        if user2==network[i][0]:
            b=network[i][1]
    for i in range(len(a)):
        for d in range(len(b)):
            if a[i]==b[d]:
                common.append(a[i])
            

    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''
    commun_list=[]
    network_list=[]
    n=len(network)
    for i in range(n):
        raw_commun=getCommonFriends(user,network[i][0],network)
        if (network[i][0]!=user) and (user not in network[i][1]):
            commun_list.append(raw_commun)
    commun_list.sort(key=len) #sorts the list by length
    if len(commun_list)==0:
        return None
    if len(commun_list[len(commun_list)-1])>len(commun_list[len(commun_list)-2]):
       commun=commun_list[len(commun_list)-1]
    else:
        commun=commun_list[len(commun_list)-2]
    if len(commun)==0:
        return None
    for i in range(n):
       if network[i][0]!= user and (user not in network[i][1]):
          if all(ch in network[i][1] for ch in commun): #checks if all the elements in commun are in network[i][1]
             return network[i][0]

    
def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    counter=0
    for i in range(len(network)):
        if len(network[i][1])>=k:
            counter+=1
    return counter
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    network_list=[]
    for i in range(len(network)):
        network_list.append(network[i][1])
    network_list.sort(key=len)
    max_len=len(network_list[len(network_list)-1])
    return max_len
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    for i in range(len(network)):
        if len(network[i][1])==maximum_num_friends(network):
            max_friends.append(network[i][0])
    return  max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    counter=0
    for i in range(len(network)):
        counter+=len(network[i][1])
    average=counter/len(network)
    return average
        
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    IDs=[]
    for i in range(len(network)):
        IDs.append(network[i][0])
    IDs.sort()
    for d in range(len(network)):
        network[d][1].append(network[d][0])
        network[d][1].sort()
        if IDs!=network[d][1]:
            pass
        else:
            return True
    return False
            


##### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    network_list=[]
    for i in range(len(network)):
        network_list.append(network[i][0])
        
    flag=True
    while flag==True:
        user_answer=input('Enter an integer for a user ID:').strip()
        try:
            user_answer=int(user_answer)
            flag=False
        except ValueError:
               print('That was not an integer. Please try again.')
               flag=True
        if str(user_answer).isnumeric() or (str(user_answer)[0]=='-'):
            if user_answer in network_list:
               return user_answer
               flag=False
            else:    
                print('That user ID does not exist. Try again.')
                flag=True
        
    
##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    

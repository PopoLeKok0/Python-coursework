# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]
     #gives the length of half the deck
     i=-1
     d=-2
     while i<len(deck)-2 and d<len(deck)-2:
         i+=2
         d+=2
         dealer.append(deck[i])
         other.append(deck[d])
     other.append(deck[len(deck)-1])
     return (dealer,other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]
    no_pairs_no_symboles=[]#for testing
    l=sorted(l)
    i=0
    if len(l)==2:
        if l[0]==l[1]:
            return l[0]
    l+=['place holder']
    while i+1<len(l):
        a=l[i]
        b=l[i+1]
        if a[0]!=b[0]:
            no_pairs.append(a)
            no_pairs_no_symboles.append(a[0])#for testing
            i+=1
        else:
            i+=2
    l.remove('place holder')
    #print(l)
    random.shuffle(no_pairs)
    return no_pairs

    
def print_deck(deck):
    '''
    (list)->None
    Prints elements of a given list deck separated by a space
    '''
    
    for i in range(len(deck)):
        print(deck[i],end=' ')
    print('\n')

    #print_deck(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢']) #test
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     print('I have '+str(n)+' cards. If 1 stands for my first card and '+str(n)+ ' for my last card, which of my cards would you like?')
     flag=True
     while flag==True:
         a=int(input('Give me an integer between 1 and '+str(n)+': '))
         if not(a>=1 and a<=n):
             flag==True
             while flag==True:
                 a=int(input('Invalid number. Please enter integer between 1 and '+str(n)+': '))
                 if a>=1 and a<=n:
                     flag==False
                     return a
                 
         else:
             flag==False
             return a
             
             
         

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)
     print('***********************************************************')
     print('Your turn.\n')
     print('Your current deck of cards is:\n')
     print_deck(human)
     p=get_valid_input(len(dealer))
     if str(p)=='1':
         m='st'
     elif str(p)=='2':
         m='nd'
     elif str(p)=='3':
         m='rd'
     else:
         m='th'
     print('You asked for my '+str(p)+m+' card')
     x=dealer[int(p)-1]
     print('Here it is. It is '+x)
     human.append(x)
     dealer.remove(x)
     print('With '+x+' added, your current deck of cards is:\n')
     print_deck(human)
     print('And after discarding pairs and shufing, your deck is:\n')
     human=remove_pairs(human)
     print_deck(human)
     wait_for_player()
     flag=True
     while len(dealer)>0 and flag==True:
             print('***********************************************************')
             print('My turn.\n')
             v=random.randint(1,len(human))
             if str(v)=='1':
                 ko='st'
             elif str(v)=='2':
                 ko='nd'
             elif str(v)=='3':
                 ko='rd'
             else:
                 ko='th'
             print('I took your ' + str(v)+ko+' card')
             dealer.append(human[v-1])
             dealer=remove_pairs(dealer)
             human.remove(human[v-1])
             wait_for_player()
             if len(human)==0:
                print('***********************************************************')
                print('Ups. You do not have any more cards\nCongratulations! You, Human, win')
                flag=False
             else:
                 print('***********************************************************')
                 print('Your turn.\n')
                 print('Your current deck of cards is:\n')
                 print_deck(human)
                 w=get_valid_input(len(dealer))
                 if str(w)=='1':
                     h='st'
                 elif str(w)=='2':
                     h='nd'
                 elif str(w)=='3':
                     h='rd'
                 else:
                     h='th'
                 print('You asked for my '+str(w)+h+' card')
                 xo=dealer[int(w)-1]
                 print('Here it is. It is '+xo)
                 human.append(xo)
                 dealer.remove(xo)
                 print_deck(human)
                 print('With '+xo+' added, your current deck of cards is:\n')
                 print_deck(human)
                 print('And after discarding pairs and shuffling, your deck is:\n')
                 human=remove_pairs(human)
                 print_deck(human)
                 wait_for_player()
                 if len(dealer)==0:
                    print('***********************************************************')
                    print('Ups. I do not have any more cards\nYou lost! I, Robot, win')
                
            
     
	
	 

# main
play_game()

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
        
# Name: Sami Hassan
# Student Number: 300169285
# ITI 1120 Fall 2021
# Assignment 4 Part 2

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
     
     i = 0
     
     while i < len(deck):
         if i % 2 == 0:
             other.append(deck[i])
             i = i + 1
             

         else:
             dealer.append(deck[i])
             i = i + 1


     return (dealer, other)
 


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

    l.sort()
    i = 0
    while i < len(l):
        
        
        if len(l[i]) == 3:
            
            if i == len(l)-1:
                no_pairs.append(l[i])
                random.shuffle(no_pairs)
                return no_pairs
                
                
            if l[i][0:2] == l[i+1][0:2]:
                l.remove(l[i])
                l.remove(l[i])
                
            else:
                no_pairs.append(l[i])
                i = i + 1

        if len(l[i]) == 2:
            
            if i == len(l)-1:
                no_pairs.append(l[i])
                random.shuffle(no_pairs)
                return no_pairs
                
                
            if l[i][0:1] == l[i+1][0:1]:
                l.remove(l[i])
                l.remove(l[i])
                                   
            else:
                no_pairs.append(l[i])
                i = i + 1

    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    
    
    # get the second part of the tuple
    p = deal_cards(deck)
    print(p[1])
    

    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     print("I have " + str(n)+ " cards. If 1 stands for my first card and")
     print(str(n) + " for my last card. which of my cards would you like?")
     response = int(input("Give me an integer between 1 and " + str(n) + ": "))
     

     while response not in range(1,n+1):
         response = int(input("Invalid number. Please enter integer between 1 and " + str(n) + ": "))
         
        
     return int(response)
     

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
     print(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     
     dealer = remove_pairs(dealer)
     human = remove_pairs(human)

     while len(dealer) > 0 and len(human) > 0:
         # human turn

         print("Your turn.")
         print("Your current deck of cards is: ")
         print(human)
         valid = get_valid_input(len(dealer))
         if valid == 1:
             print("You asked for my " + str(valid)+ "st card.")  
         if valid == 2:
             print("You asked for my " + str(valid)+ "nd card.")
         if valid == 3:
             print("You asked for my " + str(valid)+ "rd card.")
         if valid > 3:
             print("You asked for my " + str(valid)+ "th card.")
         card1 = dealer[valid-1]
         print("Here it is. It is " + str(card1))
         dealer.remove(card1)
         human.append(card1)
         
         print("With " + str(card1)+ " added, your current deck of cards is:")
         print(human)
         print("And after discarding pairs and shuffling, your deck is:")
         human = remove_pairs(human)
         print(human)
         wait_for_player()
         if len(human) == 0:
             print("Ups. You do not have any more cards\nCongratulations! You, Human, win")

         if len(dealer) == 0:
             print("Ups. I do not have any more cards\nYou lost! I, Robot, win")

         # robot turn

         else:
             print("My turn.")
             rob = random.randint(1, len(human))
             if rob == 1:
                 print("I asked for your " + str(rob)+ "st card.")  
             if rob == 2:
                 print("I asked for your " + str(rob)+ "nd card.")
             if rob == 3:
                 print("I asked for your " + str(rob)+ "rd card.")
             if rob > 3:
                 print("I asked for your " + str(rob)+ "th card.")

             card2 = human[rob-1]
             human.remove(card2)
             dealer.append(card2)
             dealer = remove_pairs(dealer)
             wait_for_player()
             
             if len(dealer) == 0:
                 print("Ups. I do not have any more cards\nYou lost! I, Robot, win")

             if len(human) == 0:
                 print("Ups. You do not have any more cards\nCongratulations! You, Human, win")
         
    
     
     
    

# main
play_game()

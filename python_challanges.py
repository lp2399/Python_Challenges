# first python challange
import re

def main():
    game_instruction()
    continue_game()
def game_instruction():
    print("Hello Welcome to Tic Tac Toe")
    print("""RULES: The board consist of horizontal and vertical indexes
To choose the top left square you would choose 1a and so on
To win you must get 3 consecutive X's or O's horizontally, vertically or diagnoly
Here is the board
    """)
    initial_board()
    print("Once Game is over you can choose to play again by input prompt that will ask yes or no to continue")

def continue_game():
    initial_board()
    update_board_results = update_board()
    if(update_board_results==True):
        yes_no_results = yes_no()
        if(yes_no_results=="Y"):
            continue_game()
        else:
            return    
                          
def yes_no():
    choice ='NaEC' # Not an expected char
    within_range = False

    while within_range == False:
        choice = input("Enter Y to continue  or N to quit: ").upper()[0] 
        # regex will check to only allow a,b,c from input at the first index only [0] incase more than 1 chars are entered, lowercased if user types uppercase char
        if not re.match("^[Y,N]", choice):
            print ("Only enter Y to continue or N to quit")
            within_range = False
        else:
            within_range = True
    return (choice)  
        
def initial_board():
    print("""
   a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     
""")

def choose_XO_char():
    choice ='NaEC' # Not an expected char
    within_range = False

    while within_range == False:
        choice = input("Enter X or O: ").upper()[0] 
        # regex will check to only allow x or o from input at the first index only [0] incase more than 1 chars are entered
        if not re.match("^[X,O]", choice):
            print ("Only enter X or O")
            within_range = False
        else:
            within_range = True

    print("You picked: "+choice)
    return (choice)  

def choose_int_index():
    choice ='NaN' # Not a number
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
    
        choice = input("Please enter a number (1,2,3): ") # the program only needs a int from 1,2,3
        
        if choice.isdigit() == False: # bool to check that only an int is entered
            print("Sorry enter a digit")
            
        if choice.isdigit() == True:
            if int(choice) in range(1,4): # once a int is entered this checks for a range of numbers between 1,2,3
                within_range = True
            else:
                within_range

    print("You picked: "+choice)
    return int(choice)

def choose_char_index():
    choice ='NaEC' # Not an expected char
    within_range = False

    while within_range == False:
        choice = input("Enter a, b or c: ").lower()[0] 
        # regex will check to only allow a,b,c from input at the first index only [0] incase more than 1 chars are entered, lowercased if user types uppercase char
        if not re.match("^[a-c]", choice):
            print ("Only enter a, b or c")
            within_range = False
        else:
            within_range = True

    print("You picked: "+choice)
    return (choice)  
        
def update_board():
    gameover = False
    row1 = ["-","-","-"]
    row2 = ["-","-","-"]
    row3 = ["-","-","-"]
    while gameover == False:
        chosen_char = choose_XO_char()
        int_index = choose_int_index()
        char_index = choose_char_index()
        if(int_index==1 and char_index=="a"):
            row1[0] = chosen_char
        elif(int_index==1 and char_index=="b"):
            row1[1] = chosen_char
        elif(int_index==1 and char_index=="c"):
            row1[2] = chosen_char
        elif(int_index == 2 and char_index=="a"): # for now cant think of better way to do this
            row2[0] = chosen_char
        elif(int_index==2 and char_index=="b"):
            row2[1] = chosen_char
        elif(int_index==2 and char_index=="c"):
            row2[2] = chosen_char
        elif(int_index==3 and char_index=="a"):
            row3[0] = chosen_char
        elif(int_index==3 and char_index=="b"):
            row3[1] = chosen_char
        elif(int_index==3 and char_index=="c"):
            row3[2] = chosen_char
        if (all(i == row1[0] for i in row1) and row1[0]!="-") or (all(i == row2[0] for i in row2) and row2[0]!="-") or (all(i == row3[0] for i in row3) and row3[0]!="-"): # dont know better way
            gameover = True
        if((row1[0]==row2[1]) and (row1[0]==row3[2]) and (row1[0]!="-")):
            gameover = True
        if((row1[2]==row2[1]) and (row1[0]==row3[0]) and (row1[2]!="-")):
            gameover = True  
        for i, (x, y, z) in enumerate(zip(row1,row2,row3)):
            if((x==y and x==z) and (i==0) and row1[i]!="-"):
                gameover = True
            elif((x==y and x==z) and (i==1) and row1[i]!="-"):
                gameover = True
            elif((x==y and x==z) and (i==2) and row1[i]!="-"):
                gameover = True
        if "-" not in(row1 and row2 and row3):
            gameover = True
            print("Its a tie")
            return gameover    
        board = f"""
  a     b     c
      |     |     
1  {row1[0]}  |  {row1[1]}  |  {row1[2]}  
 _____|_____|_____
      |     |     
2  {row2[0]}  |  {row2[1]}  |  {row2[2]}  
 _____|_____|_____
      |     |     
3  {row3[0]}  |  {row3[1]}  |  {row3[2]}  
      |     |     
    """
        print(board)
    print("Game over "+chosen_char+ " Wins")
    return gameover


# card templeate https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
# function help https://stackoverflow.com/questions/53578015/need-ascii-playing-cards-to-print-on-one-line
""" 
                                                                                        IMPORTANT
                                                         IN THIS PROGRAM I ADD CARD PRINTING FUNCTIONALITY FROM ALREADY EXISTING CODE
                                                                                I DID NOT WRITE THIS PROGRAM 
                                                                                SOURCE CODE CAN BE FOUND HERE
                                                                                             ↓         
            https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/08-Milestone%20Project%20-%202/03-Milestone%20Project%202%20-%20Complete%20Walkthrough%20Solution.ipynb                               

"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }

HIDDEN_CARD = """
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
""".format().split('\n')  


def print_hand_with_hidden(cards):
    hand = []
    for i in cards:
        if(i[0]>9):
            Card = """
 ┌─────────┐
 │{}       │
 │         │
 │         │
 │   {}     │
 │         │
 │         │
 │       {}│
 └─────────┘""".format(i[0],i[1],i[0]).split('\n')
            hand.append(Card)
        elif(i[0]<9 and i[0]>0):
            Card = """
 ┌─────────┐
 │{}        │
 │         │
 │         │
 │    {}    │
 │         │
 │         │
 │       {} │
 └─────────┘""".format(i[0],i[1],i[0]).split('\n')
            hand.append(Card)         
    hand.append(HIDDEN_CARD)
    for i in zip(*hand):
        print("   ".join(i))

def print_hand(cards):
    hand = []
    for i in cards:
        if(i[0]>9):
            Card = """
 ┌─────────┐
 │{}       │
 │         │
 │         │
 │   {}     │
 │         │
 │         │
 │       {}│
 └─────────┘""".format(i[0],i[1],i[0]).split('\n')
            hand.append(Card)
        elif(i[0]<9 and i[0]>0):
            Card = """
 ┌─────────┐
 │{}        │
 │         │
 │         │
 │    {}    │
 │         │
 │         │
 │       {} │
 └─────────┘""".format(i[0],i[1],i[0]).split('\n')
            hand.append(Card)         
    for i in zip(*hand):
        print("   ".join(i))


class Card:
    def __init__(self,rank,suits):
        self.rank = rank
        self.suits = suits
        self.num_rank= values[rank]       

class Deck:
    
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit)) 

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
        

class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing 
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            print("Player Hits")
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    player_cards = []
    for i in player.cards:
        player_cards.append((i.num_rank,symbol[i.suits]))  
    print("\nDealer's Hand:")
    print_hand_with_hidden([(dealer.cards[1].num_rank,symbol[dealer.cards[1].suits])])
    print("\nPlayers's Hand:")
    print_hand(player_cards)
    print("\nPlayers's Total: "+str(player.value))
        
def show_all(player,dealer):
    player_cards = []
    for i in player.cards:
        player_cards.append((i.num_rank,symbol[i.suits]))
    dealer_cards = []
    for i in dealer.cards:
        dealer_cards.append((i.num_rank,symbol[i.suits]))
    print("\nDealer's Hand:")
    print_hand(dealer_cards)
    print("\nDealer's Total: "+str(dealer.value))
    print("\nPlayers's Hand:")
    print_hand(player_cards)
    print("\nPlayers's Total: "+str(player.value))    
    
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    playing = True
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        
    
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break

""" 
RESULTS FROM ONE TEST I HOPE THERE ARE NO BUGS SEEMS TO WORK 

Welcome to BlackJack! Get as close to 21 as you can without going over!
    Dealer hits until she reaches 17. Aces count as 1 or 11.
How many chips would you like to bet? 50

Dealer's Hand:
   
 ┌─────────┐   ┌─────────┐
 │10       │   │░░░░░░░░░│
 │         │   │░░░░░░░░░│
 │         │   │░░░░░░░░░│
 │   ♥     │   │░░░░░░░░░│
 │         │   │░░░░░░░░░│
 │         │   │░░░░░░░░░│
 │       10│   │░░░░░░░░░│
 └─────────┘   └─────────┘

Players's Hand:
   
 ┌─────────┐    ┌─────────┐
 │10       │    │8        │
 │         │    │         │
 │         │    │         │
 │   ♠     │    │    ♥    │
 │         │    │         │
 │         │    │         │
 │       10│    │       8 │
 └─────────┘    └─────────┘

Players's Total: 18
Would you like to Hit or Stand? Enter 'h' or 's' s
Player stands. Dealer is playing.

Dealer's Hand:
   
 ┌─────────┐   ┌─────────┐       
 │10       │   │░░░░░░░░░│       
 │         │   │░░░░░░░░░│
 │         │   │░░░░░░░░░│
 │   ♥     │   │░░░░░░░░░│
 │         │   │░░░░░░░░░│
 │         │   │░░░░░░░░░│
 │       10│   │░░░░░░░░░│
 └─────────┘   └─────────┘

Players's Hand:
   
 ┌─────────┐    ┌─────────┐
 │10       │    │8        │
 │         │    │         │
 │         │    │         │
 │   ♠     │    │    ♥    │
 │         │    │         │
 │         │    │         │
 │       10│    │       8 │
 └─────────┘    └─────────┘

Players's Total: 18

Dealer's Hand:

 ┌─────────┐    ┌─────────┐    ┌─────────┐
 │2        │    │10       │    │10       │
 │         │    │         │    │         │
 │         │    │         │    │         │
 │    ♥    │    │   ♥     │    │   ♠     │
 │         │    │         │    │         │
 │         │    │         │    │         │
 │       2 │    │       10│    │       10│
 └─────────┘    └─────────┘    └─────────┘

Dealer's Total: 22

Players's Hand:

 ┌─────────┐    ┌─────────┐
 │10       │    │8        │
 │         │    │         │
 │         │    │         │
 │   ♠     │    │    ♥    │
 │         │    │         │
 │         │    │         │
 │       10│    │       8 │
 └─────────┘    └─────────┘

Players's Total: 18
Dealer busts!

Player's winnings stand at 150
Would you like to play another hand? Enter 'y' or 'n' n
Thanks for playing!



ADDED CODE FOR FUNCTIONALITY AGAIN I DID NOT WRITE THIS ONE BLACK JACK PROGRAM ONLY ADDED FUNCTIONALITY

symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }

HIDDEN_CARD = ""
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
"".format().split('\n')  


def print_hand_with_hidden(cards):
    hand = []
    for i in cards:
        if(i[0]>9):
            Card = ""
 ┌─────────┐
 │{}       │
 │         │
 │         │
 │   {}     │
 │         │
 │         │
 │       {}│
 └─────────┘"".format(i[0],i[1],i[0]).split('\n')
            hand.append(Card)
        elif(i[0]<9 and i[0]>0):
            Card = ""
 ┌─────────┐
 │{}        │
 │         │
 │         │
 │    {}    │
 │         │
 │         │
 │       {} │
 └─────────┘"".format(i[0],i[1],i[0]).split('\n')
            hand.append(Card)         
    hand.append(HIDDEN_CARD)
    for i in zip(*hand):
        print("   ".join(i))

def print_hand(cards):
    hand = []
    for i in cards:
        if(i[0]>9):
            Card = ""
 ┌─────────┐
 │{}       │
 │         │
 │         │
 │   {}     │
 │         │
 │         │
 │       {}│
 └─────────┘"".format(i[0],i[1],i[0]).split('\n')
            hand.append(Card)
        elif(i[0]<9 and i[0]>0):
            Card = ""
 ┌─────────┐
 │{}        │
 │         │
 │         │
 │    {}    │
 │         │
 │         │
 │       {} │
 └─────────┘"".format(i[0],i[1],i[0]).split('\n')
            hand.append(Card)         
    for i in zip(*hand):
        print("   ".join(i))

def show_some(player,dealer):
    player_cards = []
    for i in player.cards:
        player_cards.append((i.num_rank,symbol[i.suits]))  
    print("\nDealer's Hand:")
    print_hand_with_hidden([(dealer.cards[1].num_rank,symbol[dealer.cards[1].suits])])
    print("\nPlayers's Hand:")
    print_hand(player_cards)
    print("\nPlayers's Total: "+str(player.value))
    
def show_all(player,dealer):
    player_cards = []
    for i in player.cards:
        player_cards.append((i.num_rank,symbol[i.suits]))
    dealer_cards = []
    for i in dealer.cards:
        dealer_cards.append((i.num_rank,symbol[i.suits]))
    print("\nDealer's Hand:")
    print_hand(dealer_cards)
    print("\nDealer's Total: "+str(dealer.value))
    print("\nPlayers's Hand:")
    print_hand(player_cards)
    print("\nPlayers's Total: "+str(player.value))    
"""










"""
                                                                    PROMPT
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

For example
Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return:
Error: Too many problems.
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
Error: Operator must be '+' or '-'.
Each number (operand) should only contain digits. Otherwise, the function will return:
Error: Numbers must only contain digits.
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
Error: Numbers cannot be more than four digits.
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)                                                                    



"""

                                                                            #CODE
# FAILS TEST AT Repl.it 
def arithmetic_arranger(arithm_list,cond=None): 
   if len(arithm_list) > 5: return "Error: Too many problems." #check len of list 
   problem_list = [] # empty list to append lists 
   for i, problem in enumerate(arithm_list):
     problem_list.append(problem.split()) #appends list to create nested list. example [['23','+','5']['23','-','5']]
   for i in problem_list:
      if([j for j in i if len(j)>4]): # checks if len of digit sequence is > 4
          return "Error: Numbers cannot be more than four digits."
      while True:
         try:
          if(i[1]=="+"): # checks if the second value in i is either - +
             i.append("-----")    
             i.append(int(i[0])+int(i[2])) # if conditon true, try to parse, sum, append to i
          elif(i[1]=="-"):
             i.append("-----")    
             i.append(int(i[0])-int(i[2])) # if conditon true, try to parse, subt, append to i
          else:
            return "Error: Operator must be '+' or '-'."         
         except ValueError: # handles parsing error
            return "Error: Problems must only contain digits."
         else:
             break 
   if(cond==False):
      return 
   elif(cond==None):
      return         
   final_list = []
   for i, characters in enumerate(problem_list):
# for loop iterates problem_list to create a list of formated strings using list indexes   
        problem = """
{0:>10}
{1:>5}{2:>5}
{3:>10}
{4:>10}
      """.format(characters[0], characters[1], characters[2],characters[3],characters[4]).split('\n')
        final_list.append(problem)
   return '\n'.join([''.join(i) for i in zip(*final_list)]) # man i was so happy when got this to work took me alot of trys and reformats
   
ints_list = ["32 + 6911", "2 - 3801", "45 + 43", "123 + 49"]
print(arithmetic_arranger(ints_list,True))



"""
                                                            TERMINAL RESULTS


    32         2        45       123
+ 6911    - 3801    +   43    +   49
 -----     -----     -----     -----
  6943     -3799        88       172                                                            
"""
   




"""
                                                            PROMPT
If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

print( add_time("8:16 PM", "466:02", "tuesday"))
# Returns: 6:18 AM, Monday (20 days later)

print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday
 
print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM
 
print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)
 
print(add_time("11:43 PM", "24:20", "tueSday")) 
# Returns: 12:03 AM, Thursday (2 days later)
 
print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

                                                               PROCESS

add_time("11:59 PM", "24:59", MOnDay) example :challange states no py lib imports we can only assume it will only be case 
insensitive for third param therefore we can use toLowercase or toUpper to compare in our list


first for arg1, replace the : seperator with '' and split into array example --> ["11","59",""PM]
next for arg2, replace the : seperator with '' and split into array example --> ["24","59"]  
then arg1[1] and arg2[1] are parsed to int and added example --> value of arg1[1] = 59, value of arg2[1] = 59, then 59+59  = 118

next 118/60 for obtaining hours and mins
1.96666666667  the (1) is the hour so it needs to carry over to the left hand side for additon with arg1[0] and arg2[0]
for obtaining remainder minutes .96666666667 * 60  = round(58) 58 minutes
if statment must handle values less than 10 for proper format example --> 11:10 and 11:03 correct format, 11:3 will result instead of 11:03 if not properly formated 

next adding the left hand side
arg1[0] and arg2[0] are parsed to int and added example --> value of arg1[0] = 11, value of arg2[0] = 24, 11 +24 (+1 carried over from previous of 1h 58min)  = 36
while loop subtracts a = (a)-12 in this case a is 36 , condition: while a is greater than 12 will subtract 2 times resulting in 12
12:58

round(36/12)  = 3, this checks the amount of times to flip PM:AM only when value is 1 or greater
next to check for AM or PM, a dictionary with {key"AM" val as int "0", key"PM" val as int "1"} to use in if statemnt 
example --> "PM" is initial start time then we take the value of PM from dict and add the value from 36/12 which is 3, then check added numbers, if odd then PM, if even then AM
"""

#                                                               CODE
def add_time(arg_one, arg_two, arg_opti=None):
   day_list = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
   AM_PM_dict = {"AM":0,"PM":1}
   arg_one_contents = arg_one.replace(':',' ').split()
   arg_two_contents = arg_two.replace(':',' ').split()
   hours = int(arg_one_contents[0])+int(arg_two_contents[0])
   minutes = int(arg_one_contents[1])+int(arg_two_contents[1])
   if(minutes>60):
         min_to_hour = minutes/60
         int_hour, remainder_min = divmod(min_to_hour, 1)
         hours = round(hours+int_hour)
         converted_min = round(remainder_min*60)
         minutes =str(converted_min).zfill(2) if converted_min<10 else converted_min
   elapsed_days = round(hours/24)
   AM_PM_Flip = hours//12
   while hours > 12:
          hours = hours-12
   if(AM_PM_Flip>0):
      j = AM_PM_Flip+AM_PM_dict[arg_one_contents[2]]
      AM_PM="AM" if j%2==0 else "PM"
   else:
      AM_PM = arg_one_contents[2]         
   h = AM_PM_Flip-1 # forgot what this does but i think it checks what will be printed
   minutes =str(minutes).zfill(2) if int(minutes)<10 else minutes
   if(arg_opti!=None):
          if(h<0):
            return """{}:{} {}, {}""".format(hours, minutes, AM_PM,arg_opti.lower().capitalize())
          arg_opti_index = day_list.index(arg_opti.lower())
          len_from_end = day_list.index(day_list[-1]) -arg_opti_index
          elap_days = elapsed_days
          while elap_days>7:
             elap_days-=7
          day  = day_list[(elap_days-len_from_end)-1].capitalize()
          if(h==1):
            return """{}:{} {}, {} (next day)""".format(hours, minutes, AM_PM,day)   
          elif(h>1):
            return """{}:{} {}, {} ({} days later)""".format(hours, minutes, AM_PM,day,elapsed_days)
          elif(h<1):
            return """{}:{} {}, {} """.format(hours, minutes, AM_PM,day)  
   if(h==1):
      return """{}:{} {} (next day)""".format(hours, minutes, AM_PM)
   elif(h>1):
      return """{}:{} {} ({} days later)""".format(hours, minutes, AM_PM,elapsed_days)
   elif(h<1 and AM_PM_Flip<1):
          return """{}:{} {}""".format(hours, minutes, AM_PM)     
   elif(h<1 and AM_PM=="AM"):
      return """{}:{} {} (next day)""".format(hours, minutes, AM_PM)    
   else:
      return """{}:{} {}""".format(hours, minutes, AM_PM)                                                                    

"""
                                                               RESULTS AT Repl.it
 python main.py
1:08 AM (next day)
............
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK


                                                               TERMINAL RESULTS
6:18 AM, Monday (20 days later)
5:01 AM
5:42 PM, Monday
6:10 PM
2:02 PM, Tuesday
12:03 PM
1:40 AM (next day)
12:03 AM, Thursday (2 days later)
7:42 AM (9 days later)                                                               

"""

""" 
                                                                            PROMPT
In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

Rectangle class
When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

set_width
set_height
get_area: Returns area (width * height)
get_perimeter: Returns perimeter (2 * width + 2 * height)
get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line 
should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)

Square class
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The __init__ method should store the side 
length in both the width and height attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string, 
it should look like: Square(side=9)

Additionally, the set_width and set_height methods on the Square class should set both the width and height.

"""
                                                                        #CODE
# NOT MUCH TO COMMENT CODE IS SELF EXPLANITORY
# THIS CHALLANGES WAS TOO EASY 
class Rectangle: 
    def __init__(self, width, height): 
        self.width = width
        self.height = height 

    def __str__(self):
        return """Rectangle(width={}, height={})""".format(self.width,self.height)

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self): 
        return self.width*self.height 
    
    def get_perimeter(self): 
        return ((2 * self.width) + (2 * self.height))

    def get_diagonal(self): 
        return (((self.width ** 2) + (self.height ** 2)) ** .5)

    def get_picture(self):
        if(self.height >50 or self.width>50):
            return "Too big for picture."
        shape_list = []
        for i in range(self.height):
            i = ('*'*self.width)
            shape_list.append(i)
        x = "\n".join(shape_list)         
        return """{}\n""".format(x)

    def get_amount_inside(self,shape):
        return  self.get_area()//shape.get_area()   

class Square(Rectangle):
    def __init__(self, side): 
        self.width = side
        self.height = side
        self.side = side

    def __str__(self):
        return """Square(side={})""".format(self.side)

    def set_side(self,side):
        self.side = side
        self.width = side
        self.height = side    

    def set_width(self,width):
        self.width = width
        self.height = width
        self.side = width

    def set_height(self,height):
        self.height = height
        self.width = height
        self.side = height         

'''                                                                                    RESULTS AT Repl.it

 python main.py
50
26
Rectangle(width=3, height=10)
81
5.656854249492381
Square(side=4)
...............
----------------------------------------------------------------------
Ran 15 tests in 0.002s

OK



'''



"""                                                                     PROMPT

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls?
 While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate 
 probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

First, create a Hat class in prob_calculator.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, 
a class object could be created in any of these ways:

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be 
a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat 
is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].

The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return 
those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the
 available quantity, return all the balls.

Next, create an experiment function in prob_calculator.py (not inside the Hat class). This function should accept the following arguments:

hat: A hat object containing balls that should be copied inside the function.
expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and
 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
num_balls_drawn: The number of balls to draw out of the hat in each experiment.
num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
The experiment function should return a probability.

For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball when you draw 5 balls from a hat containing 6 black, 4 red, 
and 3 green. To do this, we perform N experiments, count how many times M we get at least 2 red balls and 1 green ball, and estimate the probability as M/N. Each experiment consists
 of starting with a hat containing the specified balls, drawing a number of balls, and checking if we got the balls we were attempting to draw.

Here is how you would call the experiment function based on the example above with 2000 experiments:

hat = Hat()

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
Since this is based on random draws, the probability will be slightly different each time the code is run.
"""

                                                                                #CODE

import random
import copy
from collections import Counter
class Hat: 
    def __init__(self,**kwargs): # from dict to a list of key*val times. if we pass Hat(blue=3,red=2) we get a list [blue,blue,blue,red,red]
        contents = []
        for i,j in kwargs.items():
            for x in range(j):
                contents += i.split()
        self.contents = contents

    def draw(self,quantity):
        drawn_list = []
        if(quantity>len(self.contents)): # if the len is greater than the len(contents) we just return the list
            return self.contents
        for i in range(quantity): # we do this for the amount needed
            drawn_list.append(self.contents.pop(self.contents.index(random.choice(self.contents)))) 
        return drawn_list
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    drawn_list = []
    M =0 # helps us keep track of the times expected_balls appaears in drawn list
    for i in range(num_experiments):
        hat_obj = copy.deepcopy(hat) # had to look this up since hat_obj = hat wasnt working had me confused
        drawn = hat_obj.draw(num_balls_drawn)# drawing the balls using draw method num_ball_time
        drawn_list.append(drawn) #append what is returned from draw

    #99% of the work was figuring out how to find the expected ball in the drawn list       
    for sub in drawn_list:
        if(len( Counter(expected_balls)-Counter(i for i in sub))==0): # so satisfiyng when you create the answer i found no help online really sucked
            M+=1           
    return M/num_experiments # finally we return our prob
hat = Hat(black=6, red=4, green=3)      
probability = experiment(hat, {"red":2,"green":1},5,2000)
print(probability)


""" THIS ALLOWED ME TO FIND THE SOLUTION
a = Counter(red=2,green=1)
b = Counter(red=3,green=2,blue=5)
print(a-b)
"""

"""
                                                                                        RESULTS AT Repl.it
 python main.py
Probability: 0.176
...
----------------------------------------------------------------------
Ran 3 tests in 0.121s

OK
                                                                                         

"""

"""
                                                                            PROMPT

Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. 
When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also 
contain the following methods:

A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the 
ledger list in the form of {"amount": amount, "description": description}.
A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, 
nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer 
to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer 
from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns 
True otherwise. This method should be used by both the withdraw method and transfer method.
When the budget object is printed it should display:

A title line of 30 characters where the name of the category is centered in a line of * characters.
A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, 
then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
A line displaying the category total.
Here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
Besides the Category class, create a function (ouside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be vertacally below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     


Probably the ugliest graph possible i decided to make a different one hopefully easier on the eyes however will fail Repl.it tests





 """         
                                                                            #CODE
import math
class Category:
    def __init__(self,category):
        self.category = category 
        self.ledger = []

    def __str__(self):
        asterik_quantity = (30-(len(self.category)))//2 # right_side + len(middle)+ left_side = 30 therefore if len(middle)=5 then 30-5 = 25, 25//2 then check is even
        if(len(self.category)%2==0):# Checking if is even for formatting
            formatted_title = """{0}{1}{2}""".format("*"*asterik_quantity,self.category,"*"*asterik_quantity)
        else:
            formatted_title = """{0}{1}{2}""".format("*"*asterik_quantity,self.category,"*"*(asterik_quantity+1))     
        formatted_list = [] # the formatted list that will be returned
        formatted_list.append(formatted_title)# appending out title
        total = 0 # helps us track the total
        description = "" # placeholder
        amount = 0 # used for tracking amount initally 0
        for i in self.ledger: # iterate through the ledger list to obtain info
            for key,val in i.items():
                if(key=="description"):
                    description = val  # getting the val for key'description' 
                if(key=="amount"):
                    amount = val # getting the int val from key'amount'
                    total = val+total  # here we add all values from keys'amount'  
            formatted_amount_description="""
{0:23}{1:7} """.format(description[0:22],amount)# [0:22] helps truncate the len of descrpiton so that it fits consisintly
            formatted_list.append(formatted_amount_description)
        formatted_total = """\nTotal: {}\n""".format(total)
        formatted_list.append(formatted_total)     
        return ''.join([''.join(i) for i in zip(formatted_list)]) #finally we us list comprension and join to return a string

    def deposit(self,amount, description=""):
        return self.ledger.append({"amount":amount,"description":description}) # creating 2 dicts for deposit

    def withdraw(self,amount, description=""):
        if(self.check_funds(amount)): # funds will return true if suffienct funds to make withdrawl
            self.ledger.append({"amount":-amount,"description":description})# the amount is negative for eventual summation
            return True # returns true so we dont have to use else statement since if this conditon fails it will just return false
        return False

    def get_balance(self):
        return sum([i["amount"] for i in self.ledger]) # gets the total sum of values from keys'amount'

    def transfer(self,amount, category):
        if(self.check_funds(amount)): #checks if there are suffiecnt funds to transfer
            self.withdraw(amount, f"Transfer to {category}") # we use the withdraw method
            category.deposit(amount, f"Transfer from {self.category}")# transfers to category obj
            return True        
        return False

    def check_funds(self,amount):
        if(amount>self.get_balance()): # get out balance and compare the amount if amount>balance= true than insuffiecnt funds
            return False
        return True 
        
def create_spend_chart(catergories_list):
    formatted_list = [] # final formatted list used in printing
    withdraws = [] # tracks our withdraws
    total = 0
    title = """Percentage spent by category 100% {0} """.format("|"*100) # helps visualize 100% for comparison to the rest of the graph
    formatted_list.append(title)
    for category in catergories_list:
        withdrawn_amount = 0
        for action in category.ledger:
            if action["amount"] < 0: # we want to get all negative or withdrawls
                withdrawn_amount -= action["amount"]
                categ = category.category # grabbing the name of the category
                categ_withdrawn_amount_dict = {categ: math.ceil(withdrawn_amount * 1000) / 1000} # creating a dictionary with {name:amount_spent}
        withdraws.append(categ_withdrawn_amount_dict)
    total = get_total(withdraws) # this static method helps get the total for the percentage it adds the total from dict {name:amount_spent} amount_spent
    for i in withdraws:
        for key,val in i.items():# now iterate through our dicts
            percentage = val/total # getting the percentage for each obj
            formatted_str = """
{0:29} {1}% {2}""".format(key,int((math.ceil(percentage * 1000) / 1000)*100),'|'*int((math.ceil(percentage * 1000) / 1000)*100)) # some rounding error occurs and we may get 99% instead of 100            
        formatted_list.append(formatted_str)   
    return '\n'.join([''.join(i) for i in zip(formatted_list)])# your probably tired of seeing this but it works

def get_total(withdraws):
    total = 0
    for i in withdraws:
        for key,val in i.items():
            total = val+total
    return total                                                                             
# TEST 
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.check_funds(100))
clothing = Category("Clothing")
food.transfer(50, clothing)
print(clothing.get_balance())
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))

""" 
                                                                            TERMINAL RESULTS


*************Food*************
initial deposit           1000
groceries               -10.15
restaurant and more fo  -15.89
Transfer to **********     -50
Total: 923.96

***********Clothing***********
Transfer from Food          50
                        -25.55
Total: 24.45

*************Auto*************
initial deposit           1000
                           -15
Total: 985

Percentage spent by category 100% ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Food                          65% ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Clothing                      22% ||||||||||||||||||||||

Auto                          12% |||||||||||||
"""


""" 

                                                                 FUN CHALLANGES TRY THEM OUT FOR PRACTICE
                                                                                     ↓
                                        https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/


"""
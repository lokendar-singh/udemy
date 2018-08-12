#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    deck = {}
    p1 = []
    p2 = []
    def __int__(self):
        print('DECK __int__ called')

    def createDeck(self,SUITE,RANKS):
        self.SUITE = SUITE
        self.RANKS = RANKS
        self.ct = 2;
        # print('Fun called to call __int__')
        for s in self.SUITE:
            for r in self.RANKS:
                Deck.deck[s+r] = self.ct
                self.ct = self.ct+1
            self.ct = 2

        # print('Deck created:')
        # print(Deck.deck.items())
        key1 = list(Deck.deck.keys())
        # print((key1))
        shuffle(key1)
        # print(len(key1))
        ind = int(len(key1)/2)
        Deck.p1 = key1[:ind]
        Deck.p2 = key1[ind:]

    def getDeck(self,keyList):
        ind = int(len(keyList)/2)
        Deck.p1 = keyList[:ind]
        Deck.p2 = keyList[ind:]
        # print(len(self.p1))
        # print(len(self.p2))
        # print(self.p1)
        # print(self.p2)
        # k=self.p1.pop()
        # print(k)
        # print(Deck.deck[k])
        # print(Deck.p1)

class Hand(Deck):
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __int__(self):
        print('Hand __int__ called')
    def addCard(self,ply,card):
        print('add card')
        # print(Hand.p1)
        if ply=='p1':
            Hand.p1.append(card)
        else:
            Hand.p2.append(card)

    def remCard(self,ply):
        print('remove card')
        if ply=='p1':
            self.c = Hand.p2.pop(0)
            Hand.addCard(self,'p2',self.c)
            self.c = Hand.p1.pop(0)
            Hand.addCard(self,'p2',self.c)
        else:
            self.c = Hand.p1.pop(0)
            Hand.addCard(self,'p1',self.c)
            self.c = Hand.p2.pop(0)
            Hand.addCard(self,'p1',self.c)





class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """


    def startGame(self):
        self.n1 = input('Enter Player1 name: ')
        self.n2 = input('Enter Player2 name: ')
        print(Player.p1)
        print(Player.p2)
        ctt = 0
        while ctt < 50:
            ctt = ctt+1
            if(len(Player.p1)>0 and len(Player.p2)>0):
                Player.checkCard(self,0)
                print(Player.p1)
                print(Player.p2)
            else:
                if len(Player.p1)<=0:
                    print('Player 1 {} won'.format(self.n1))
                    break;
                else:
                    print('Player 2 {} won'.format(self.n2))
                    break;

    def checkCard(self,ind):
        k1 = Player.p1[ind]
        k2 = Player.p2[ind]
        if Player.deck[k1] > Player.deck[k2]:
            Player.remCard(self,'p2')
        elif Player.deck[k1] == Player.deck[k2]:
            
            for i in range(5):


            k1 = Player.p1[ind]
            k2 = Player.p2[ind]
            if Player.deck[4] > Player.deck[4]:
                Player.remCard(self,'p2')
        else:
            Player.remCard(self,'p1')


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
# d = Deck()
# k = d.createDeck(SUITE,RANKS)
# d.getDeck(k)

p = Player()
p.createDeck(SUITE,RANKS)
p.startGame()
# Use the 3 classes along with some logic to play a game of war!

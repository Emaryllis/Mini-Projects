from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
def createDeck():
    deck = [i+j for j in RANKS for i in SUITE]
    shuffle(deck)
    return deck

class Hand:
    '''
    This is the Hand class. Each player has a Hand, 
    and can add or remove cards from that hand.
    '''
    def __init__(self, cards):
        self.__cards = cards
    def cardList(self):
        return self.__cards
    def add(self, card):
        self.__cards.append(card)
        self.shuffle()
    def remove(self, card):
        self.__cards.remove(card)
    def rank(self,card):
        return RANKS.index(card[1:])
    def __len__(self):
        return len(self.__cards)
    def shuffle(self):
        shuffle(self.__cards)

class Player(Hand):
    """
    This is the Player class, which takes in a name and
    an instance of a Hand class object. The Player can
    then play cards and check if they still have cards.
    """
    def __init__(self, deck, name):
        super().__init__(deck)
        self.__name=name

    def handleWar(self, player2: 'Player', depth=0):
        card1, card2 = self.getCard(depth,player2), player2.getCard(depth,self)

        if self.rank(card1) > player2.rank(card2):
            self.modifyCards(card2, player2)
            print(f"{card1} beats {card2}! Player 1 wins this round!")
        elif self.rank(card1) < player2.rank(card2):
            player2.modifyCards(card1, self)
            print(f"{card2} beats {card1}! Player 2 wins this round!")
        else:
            print(f"Both players have the same card rank ({card1} & {card2}), it's war{'' if depth == 0 else ' again'}!")
            self.handleWar(player2, depth + 1)

    def getCard(self, depth, player):
        try:
            return self.cardList()[depth]
        except IndexError:
            print(f"{self.__name} has run out of cards. {player.__name} wins!")
            exit()

    def modifyCards(self, card, player):
        self.add(card)
        player.remove(card)
        


######################
#### GAME PLAY #######
######################
print("\nWelcome to War, let's begin...")
deck = createDeck()
player1 = Player(deck[:len(deck)//2],"Player 1")
player2 = Player(deck[len(deck)//2:],"Player 2")
print(f"Player 1's deck: {', '.join(player1.cardList())}\nPlayer 2's deck: {', '.join(player2.cardList())}")
while len(player1) !=0 and len(player2) !=0:
    input("\nPress any key to play a card\n")
    player1.handleWar(player2)
print(f"Player {'2' if len(player1)==0 else '1'} wins!")
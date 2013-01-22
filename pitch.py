from functools import total_ordering
from collections import deque
import random

random.seed()

@total_ordering
class Card(object):
    _suitList = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    _rankList = ['skip', 'skip', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self._rankList[self.rank] + ' of ' +
                self._suitList[self.suit])
        
    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

class Deck(object):
    def __init__(self):
        self.reset_deck()

    def reset_deck(self):
        self.unused_cards = []
        for suit in range(4):
            for rank in range(2,15):
                self.unused_cards.append(Card(suit,rank))
        random.shuffle(self.unused_cards)

    def deal_hand(self, n, player):
        """deal n to player"""
        player.hand = [self.unused_cards.pop() for _ in range(n)]
        

class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

    def display_hand(self):
        for card in self.hand:
            print(card)

    def play_card(self):
        c = srandom.choice(self.hand)       

players = [Player('P0'), Player('P1'), Player('P2'), Player('P3')]
deck = Deck()
HAND_SIZE = 6
play = True
while(play):
    deck.reset_deck()
    trump = -1
    lead = -1
    for player in players:
        deck.deal_hand(HAND_SIZE, player)
    for turn in range(HAND_SIZE):
        print('-' * 5 + 'Turn #' + str(turn) + '-' * 5)
        for play, player in enumerate(players):
            random.shuffle(player.hand)
            card = player.hand.pop()
            if (turn == 0 and play == 0):
                trump = card.suit
            if (play == 0):
                lead = card.suit
            print(str(player) + ' played: ' + str(card) +
                  ' {is_trump} {is_lead}'.format(is_trump = '*TRUMP' if card.suit == trump else '',
                                                is_lead = '*LEAD' if card.suit == lead else ''))
            
    answer = input('Play another hand (Y/N)?: ').upper()
    while(answer.upper() != 'Y' and answer.upper() != 'N'):
        answer = input('Incorrect answer, enter Y or N: ')
    play = True if answer == 'Y' else False

"""
    X 4 players (in same order) randomly play 1 card at a time, then re-deal hands
    X Detect trump cards
    X Detect lead suit
    - Check if valid play    
    - Determine winner of each turn
    - Give lead to correct player
    - Determine winner of each round
    - Get user input on card play
    - Take bets
    - Detect gentleman's hand
    
"""
        
    



    
                               
        
        

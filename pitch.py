from functools import total_ordering
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
        return self.rank == other.rank and self.suit == other.suit

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
        self.collected_cards = []

    def __str__(self):
        return self.name

    def display_hand(self):
        for card in self.hand:
            print(card)

    def play_valid_card(self, lead):
        card = self.hand.pop()
        if (self.has_valid_play(lead)):
            while (card.suit != lead):
                self.hand.insert(0, card)
                card = self.hand.pop()
        return card

    def has_valid_play(self, lead):
        for card in self.hand:
            if card.suit == lead:
                return True
        return False
    
def turn_winner(cards, trump, lead):
    winning_card = cards[0]
    for card in cards[1:]:
        if ((winning_card.suit == trump and card.suit == trump and card > winning_card) or
            (winning_card.suit != trump and card.suit == trump) or
            (winning_card.suit == lead and card.suit == lead and card > winning_card) or
            (winning_card.suit != lead and winning_card.suit != trump and card.suit == lead) or
            (winning_card.suit != trump and card.suit != trump and winning_card.suit != lead and card.suit != lead and card > winning_card)):
            winning_card = card
    return winning_card

def make_lead(player):
    i = players.index(player)
    return players[i:] + players[:i]

def game_points(cards):
    card_points = {
        10: 10,# 10
        11: 1, # Jack
        12: 2, # Queen
        13: 3, # King
        14: 4  # Ace
    }    
    num_points = 0
    for card in cards:
        try:
            num_points += card_points[card.rank]
        except KeyError:
            pass
    return num_points




deck = Deck()
HAND_SIZE = 6
play = True
while(play):
    print()
    deck.reset_deck()
    players = [Player('P0'), Player('P1'), Player('P2'), Player('P3')]
    for player in players:
        player.collected_cards = []
    trump = -1
    for player in players:
        deck.deal_hand(HAND_SIZE, player)
    for turn in range(HAND_SIZE):
        lead = -1
        cards_played = []
        print('-' * 5 + 'Turn #' + str(turn) + '-' * 5)
        for play, player in enumerate(players):
            card = player.play_valid_card(lead)
            if (turn == 0 and play == 0):
                trump = card.suit
            if (play == 0):
                lead = card.suit
            cards_played.append(card)
                
            print(str(player) + ' played: ' + str(card) +
                  ' {is_trump} {is_lead}'.format(is_trump = '*TRUMP' if card.suit == trump else '',
                                                is_lead = '*LEAD' if card.suit == lead else ''))
        turn_winning_player = players[cards_played.index(turn_winner(cards_played, trump, lead))]
        print('Winning card is: {winner} {player_name}'.format(winner = str(turn_winner(cards_played, trump, lead)),
                                                              player_name = str(turn_winning_player)))
        players = make_lead(turn_winning_player)
        turn_winning_player.collected_cards += cards_played

    for player in players:
        print(str(player) + ' has ' + str(game_points(player.collected_cards)) + ' points towards game')
        
    answer = input('Play another hand (y/n)?: ').upper()
    while(answer != 'Y' and answer != 'N'):
        answer = input('Incorrect answer, enter Y or N: ').upper()
    play = True if answer == 'Y' else False

"""
    X 4 players (in same order) randomly play 1 card at a time, then re-deal hands
    X Detect trump cards
    X Detect lead suit
    X Check if valid play    
    X Determine winner of each turn
    X Give lead to correct player
    - Determine points awarded to each player for each round
    - Get user input on card play
    - Take bets
    - Detect gentleman's hand
    
"""
        
    



    
                               
        
        

# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user47_Q5NyK3nK42IZuBt.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False  # keeps track of whether the player's hand is still being played
outcome = ""
message = ''
score = 0
player_hand = []
dealer_hand = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print
            "Invalid card: ", suit, rank

    #  __str__ method is called when we want to print out information about a Card object
    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)

    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE,
                          [pos[0] + CARD_BACK_CENTER[0] + 1.5 * CARD_BACK_SIZE[0] - 8,
                           pos[1] + CARD_BACK_CENTER[1] + 1],
                          CARD_BACK_SIZE)


# define hand class
class Hand:
    # represent both the dealer's hand and the player's hand
    def __init__(self):
        # create Hand object, create an empty hand by assigning an empty list to the cards field
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        hand_contain = 'Hand contains '
        for card in self.cards:
            hand_contain = hand_contain + str(card) + ' '
        return hand_contain

    def add_card(self, card):
        #  take the Card object card card and append it to the list in the cards field
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        is_aces = False
        for card in self.cards:
            rank = card.get_rank()
            if rank == 'A': is_aces = True
            hand_value += VALUES[rank]
        if is_aces and hand_value < 11: hand_value += 10
        return hand_value

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0]
            card.draw(canvas, pos)


# define deck class
class Deck:
    def __init__(self):
        # create a Deck object, return a deck containing all 52 cards
        # Remember to use the Card Card initializer to create your cards
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck
        # use random.shuffle()
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()

    def __str__(self):
        # return a string representing the deck
        deck_contain = 'Deck contains '
        for card in self.cards:
            deck_contain = deck_contain + str(card) + ' '
        return deck_contain


# define event handlers for buttons
def deal():
    global outcome, in_play, score, message
    global player_hand, dealer_hand, deck

    # if the "Deal" button is clicked during the middle of a round,
    # the program reports that the player lost the round and updates the score appropriately.
    if in_play:
        in_play = False
        score -= 1
        deal()
    else:
        # shuffle the deck (stored as a global variable), create new player and dealer hands
        player_hand = Hand()
        dealer_hand = Hand()
        deck = Deck()
        deck.shuffle()

        # add two cards to each hand
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        outcome = 'Hit or Stand?'
        message = ''
        in_play = True


def hit():
    global player_hand, dealer_hand, message, in_play, score, outcome
    # if the hand is in play, hit the player
    if in_play:
        if player_hand.get_value() < 21:
            player_hand.add_card(deck.deal_card())
            # if busted, assign a message to outcome, update in_play and score
            if player_hand.get_value() > 21:
                message = "You have busted"
                in_play = False
                score -= 1
                outcome = 'New deal?'


def stand():
    # replace with your code below
    global dealer_hand, player_hand, message, score, in_play, outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())

        if dealer_hand.get_value() > 21:
            message = 'The dealer have busted'
            score += 1


        elif player_hand.get_value() <= dealer_hand.get_value():
            message = 'The dealer wins'
            score -= 1
        else:
            message = 'You win'
            score += 1
        outcome = 'New deal?'
        in_play = False

    # assign a message to outcome, update in_play and score


# draw handler
def draw(canvas):
    canvas.draw_text('Black Jack', (150, 70), 50, 'Maroon')
    canvas.draw_text(outcome, (375, 385), 30, 'white')
    canvas.draw_text(message, (200, 155), 30, 'white')
    canvas.draw_text('Score:' + str(score), (400, 115), 30, "white")
    canvas.draw_text('Dealer', (36, 185), 30, "Black")
    canvas.draw_text('Player', (36, 385), 30, 'Black')
    dealer_hand.draw(canvas, [65, 200])
    player_hand.draw(canvas, [65, 400])
    # If the round is still in play, you should draw an image of the back of a card
    # over the dealer's first (hole) card to hide it.
    if in_play:
        dealer_hand.cards[0].draw_back(canvas, [36, 199])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric

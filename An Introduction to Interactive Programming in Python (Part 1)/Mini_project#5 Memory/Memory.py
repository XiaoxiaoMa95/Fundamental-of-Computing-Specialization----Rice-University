# implementation of card game - Memory
# http://www.codeskulptor.org/#user47_GQQxdirRY0O3nqt.py

import simplegui
import random

# cards are logically 50x100 pixels in size
WIDTH = 50
HEIGHT = 100


# helper function to initialize globals
def new_game():
    global card_deck, exposed, index1, index2, state, turns

    card_deck = [0, 1, 2, 3, 4, 5, 6, 7] * 2
    random.shuffle(card_deck)
    exposed = [False] * 16
    index1, index2 = -1, -1
    state = 0
    turns = 0


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global index1, index2, state, turns, exposed

    position = pos[0] // WIDTH

    # selecting two cards and determining if they match
    if exposed[position] == False:

        # the start of the game
        if state == 0:
            index1 = position
            exposed[index1] = True
            state = 1

        # click on a card
        elif state == 1:
            index2 = position
            exposed[index2] = True
            state = 2
            turns += 1

        # the end of a turn
        elif state == 2:
            '''if you click on an unexposed card, that card is exposed and you switch to state 1
            if all exposed cards are paired, a click on an unexposed card exposes the card that was clicked on 
            and does not flip any other cards.'''
            if card_deck[index1] != card_deck[index2]:
                exposed[index1], exposed[index2] = False, False
                index1, index2 = -1, -1
            index1 = position
            exposed[index1] = True
            state = 1


def draw(canvas):
    for i in range(len(card_deck)):
        if exposed[i]:
            canvas.draw_polygon([[WIDTH * i, 0], [WIDTH * i, HEIGHT],
                                 [WIDTH * (i + 1), HEIGHT], [WIDTH * (i + 1), 0]], 1, 'Black', 'White')
            canvas.draw_text(str(card_deck[i]), [WIDTH * i + 11, 60], 55, 'Red')
        else:
            canvas.draw_polygon([[WIDTH * i, 0], [WIDTH * i, HEIGHT],
                                 [WIDTH * (i + 1), HEIGHT], [WIDTH * (i + 1), 0]], 1, 'Black', 'Green')
    label.set_text('Turns = ' + str(turns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric


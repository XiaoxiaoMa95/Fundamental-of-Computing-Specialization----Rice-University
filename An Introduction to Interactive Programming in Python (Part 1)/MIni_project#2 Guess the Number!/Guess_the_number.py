# python 2.x
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


# http://www.codeskulptor.org/#user47_UFpG34jY9FpQljc_0.py
import simplegui
import random
import math

# initialize global variables used in code
num_range = 100


# helper function to start and restart the game
def new_game():
    global num_range, secret_number, counts
    counts = int(math.ceil(math.log(num_range - 0 + 1, 2)))
    secret_number = random.randrange(0, num_range)
    print "New game. Range is [0," + str(num_range) + ")"
    print "Number of remaining guesses is", counts, "\n"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    new_game()


def input_guess(guess):
    # main game logic goes here
    global counts
    print "Guess was", int(guess)
    counts -= 1
    print "Number of remaining guesses is", counts

    if counts > 0:
        if int(guess) > secret_number:
            print "Lower!\n"
        elif int(guess) < secret_number:
            print "Higher!\n"
        else:
            print "Correct!\n"
            new_game()

    elif counts == 0:
        if int(guess) != secret_number:
            print "You ran out of guesses. The number was", secret_number, "\n"
        else:
            print "Correct!\n"
        new_game()


# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

new_game()

# register event handlers for control elements and start frame
frame.start()

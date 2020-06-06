"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""


# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    scores = [hand.count(item) * item for item in hand]
    # print(max(scores))
    return max(scores)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    scores = []
    num_of_die = list(range(1, num_die_sides + 1))
    sequences = gen_all_sequences(num_of_die, num_free_dice)
    # print('Lens', len(sequences), '\n')
    # print('Possible sequence:', sequences, '\n')
    for item in sequences:
        # print(item)
        # print(held_dice + item)
        scores.append(score(held_dice + item))
        # print(scores,'\n')
    result = sum(scores) / len(sequences)
    # print('----',result)
    return result


# expected_value((2,2), 6, 2)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    hand_holds = [()]
    for item in hand:
        # print('Item is :', item)
        for partial_set in hand_holds:
            # print('Partial Set is:', partial_set)
            hand_holds = hand_holds + [partial_set + (item,)]
            # print('New Hand Hold is:', hand_holds, '\n')

    return set(hand_holds)

#gen_all_holds((1, 2, 3))


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """

    result = (0.0, ())
    current_score = 0
    for item in gen_all_holds(hand):
        # print('ITEM is:',item)
        value = expected_value(item, num_die_sides, len(hand) - len(item))
        # print('Value is:', value)
        if value > current_score:
            current_score = value
            result = (current_score, item)
            # print("Result is:", result,'\n')
    # print('\n', '++++++',result)
    return result


# strategy((1, 2), 6)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    # hand = (1, 2, 3, 3)
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)


run_example()

import poc_holds_testsuite
poc_holds_testsuite.run_suite(gen_all_holds)

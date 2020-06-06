"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 10  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player

EMPTY = 1
PLAYERX = 2
PLAYERO = 3
DRAW = 4


# Add your functions here.

# board = provided.TTTBoard(3)
# print(board)

def switch_player(player):
    """
    Convenience function to switch players.

    Returns other player.
    """
    if player == PLAYERX:
        return PLAYERO
    else:
        return PLAYERX


def mc_trial(board, player):
    '''
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player by making random moves, alternating between players.
    The function should return when the game is over.
    '''
    board_dimension = board.get_dim()
    while board.check_win() == None:
        x_position = random.randrange(board_dimension)
        y_position = random.randrange(board_dimension)
        board.move(x_position, y_position, player)
        player = switch_player(player)


def mc_update_scores(scores, board, player):
    '''
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board,
    a board from a completed game, and which player the machine player is.
    The function should score the completed board and update the scores grid.
    As the function updates the scores grid directly, it does not return anything.
    '''
    winner = board.check_win()
    for dummy_x in range(board.get_dim()):
        for dummy_y in range(board.get_dim()):
            player_constant = board.square(dummy_x, dummy_y)
            if player_constant != EMPTY:
                if winner == player:
                    if player_constant == player:
                        scores[dummy_x][dummy_y] += SCORE_CURRENT
                    # elif player_constant == switch_player(player):
                    else:
                        scores[dummy_x][dummy_y] -= SCORE_OTHER
                elif winner == DRAW:
                    pass
                else:
                    if player_constant == player:
                        scores[dummy_x][dummy_y] -= SCORE_CURRENT
                    # elif player_constant == switch_player(player):
                    else:
                        scores[dummy_x][dummy_y] += SCORE_OTHER


def get_best_move(board, scores):
    '''
    This function takes a current board and a grid of scores.
    The function should find all of the empty squares with the maximum score
    and randomly return one of them as a (row, column) tuple.'''
    empty_square_list = board.get_empty_squares()
    if len(empty_square_list) < 1:
        pass
    else:
        max_value = float('-inf')
        print(max_value)
        max_lst = []
        for square in empty_square_list:
            if scores[square[0]][square[1]] > max_value:
                max_value = scores[square[0]][square[1]]
                max_lst = []
                print(max_value)
                max_lst.append(square)
                print(max_lst)

            elif scores[square[0]][square[1]] == max_value:
                max_lst.append(square)

    choice_empty_square = random.choice(max_lst)
    return choice_empty_square


print(get_best_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]),
                    [[0, 0], [3, 0]]))


def mc_move(board, player, trials):
    '''
    This function takes a current board, which player the machine player is, and the number of trials to run.
    The function should use the Monte Carlo simulation described above to return a move for the machine player
    in the form of a (row, column) tuple'''
    scores = []
    temp_board = board.clone()
    for dummy_i in range(board.get_dim()):
        scores.append([])
        for dummy_j in range(board.get_dim()):
            scores[dummy_i].append(0 * dummy_j)

    for _ in range(trials):
        mc_trial(temp_board, player)
        mc_update_scores(scores, temp_board, player)
        temp_board = board.clone()
    return get_best_move(board, scores)


print(mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY],
                                           [provided.PLAYERO, provided.PLAYERO, provided.EMPTY],
                                           [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX,
              NTRIALS))
# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

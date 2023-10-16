###############################################################################
# This file implements various minimax search agents.
#
# CSC 384 Fall 2023 Assignment 2
# version 1.0
###############################################################################
from mancala_game import Board, play_move
from utils import *

def is_terminal(board):
    top_empty = True
    bott_empty = True
    for pocket in board.pockets[TOP]:
        if pocket != 0:
            top_empty = False

    if top_empty == True:
        return True
    
    for pocket in board.pockets[BOTTOM]:
        if pocket != 0:
            bott_empty = False
    if bott_empty == True:
        return True
    
    return False

def play_index(board, index, player):
    top_pockets = []
    bottom_pockets = []
    for i in range(board.dimension):
        top_pockets[i] = board[TOP][i]
        bottom_pockets[i] = board[BOTTOM][i]
    pockets = []
    pockets[TOP] = top_pockets
    pockets[BOTTOM] = bottom_pockets
    
    mancalas = []
    mancalas[TOP] = board. mancalas[TOP]
    mancalas[BOTTOM] = board.mancalas[BOTTOM]

    new_board = Board(pockets, mancalas)

    stones_in_hand = new_board.pockets[player][index]
    new_board.pockets[player][index] = 0
    index += 1
    curr_top_or_bottom = player
    while(stones_in_hand > 0):
        if(index >= board.dimension):
            new_board.mancalas[curr_top_or_bottom] += 1
            stones_in_hand -= 1
            index = 0
            if curr_top_or_bottom == TOP:
                curr_top_or_bottom = BOTTOM
            else:
                curr_top_or_bottom = TOP
        else:
            if(stones_in_hand == 1 and curr_top_or_bottom == player):
                if player == TOP:
                 captured_stones = new_board.pockets[BOTTOM][board.dimension - 1 - index]
                 new_board.pockets[BOTTOM][board.dimension - 1 - index] = 0
                 new_board.pockets[index] += captured_stones
            new_board.pockets[curr_top_or_bottom][index] += 1
            stones_in_hand -= 1
            index += 1

    return new_board

def resulting_boards(board, player):
    boards = []
    resulting_indices = board.get_possible_moves()
    for index in resulting_indices:
        boards.append(play_index(board, index, player))

    return boards

def max_val(board, player, heuristic_function):
    if is_terminal(board) == True:
        return None, heuristic_function(board, player)

    best_move = None
    best_value = float('-inf')

    for move in resulting_boards(board, player):
        if player == TOP:
            _, value = min_val(move, BOTTOM)
        if player == BOTTOM:
            _, value = min_val(move, TOP)
        if value > best_value:
            best_move = move
            best_value = value
        
    return best_move, best_value


def minimax_max_basic(board, curr_player, heuristic_func):
    """
    Perform Minimax Search for MAX player.
    Return the best move and its minimax value.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the current player
    :param heuristic_func: the heuristic function
    :return the best move and its minimax value according to minimax search.
    """



    raise NotImplementedError


def minimax_min_basic(board, curr_player, heuristic_func):
    """
    Perform Minimax Search for MIN player.
    Return the best move and its minimax value.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the ccurrent player
    :param heuristic_func: the heuristic function
    :return the best move and its minimax value according to minimax search.
    """

    raise NotImplementedError


def minimax_max_limit(board, curr_player, heuristic_func, depth_limit):
    """
    Perform Minimax Search for MAX player up to the given depth limit.
    Return the best move and its estimated minimax value.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the current player
    :param heuristic_func: the heuristic function
    :param depth_limit: the depth limit
    :return the best move and its minimmax value estimated by our heuristic function.
    """

    raise NotImplementedError

def minimax_min_limit(board, curr_player, heuristic_func, depth_limit):
    """
    Perform Minimax Search for MIN player  up to the given depth limit.
    Return the best move and its estimated minimax value.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the ccurrent player
    :param heuristic_func: the heuristic function
    :param depth_limit: the depth limit
    :return the best move and its minimmax value estimated by our heuristic function.
    """

    raise NotImplementedError


def minimax_max_limit_caching(board, curr_player, heuristic_func, depth_limit, cache):
    """
    Perform Minimax Search for MAX player up to the given depth limit with the option of caching states.
    Return the best move and its minimmax value estimated by our heuristic function.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the ccurrent player
    :param heuristic_func: the heuristic function
    :param depth_limit: the depth limit
    :param caching: whether we are caching states.
    :return the best move and its minimmax value estimated by our heuristic function.
    """

    raise NotImplementedError


def minimax_min_limit_caching(board, curr_player, heuristic_func, depth_limit, cache):
    """
    Perform Minimax Search for MIN player up to the given depth limit with the option of caching states.
    Return the best move and its minimmax value estimated by our heuristic function.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the current player
    :param heuristic_func: the heuristic function
    :param depth_limit: the depth limit
    :param caching: whether we are caching states.
    :return the best move and its minimmax value estimated by our heuristic function.
    """

    raise NotImplementedError


###############################################################################
## DO NOT MODIFY THE CODE BELOW.
###############################################################################

def run_ai():
    """
    This function establishes communication with the game manager.
    It first introduces itself and receives its color.
    Then it repeatedly receives the current score and current board state
    until the game is over.
    """
    print("Mancala AI")  # First line is the name of this AI
    arguments = input().split(",")

    player = int(arguments[0])  # Player color
    limit = int(arguments[1])  # Depth limit
    caching = int(arguments[2])  # Caching
    hfunc = int(arguments[3]) # Heuristic Function

    if (caching == 1): 
        caching = True
    else: 
        caching = False

    eprint("Running MINIMAX")


    if limit == -1:
        eprint("Depth Limit is OFF")
    else:
        eprint("Depth Limit is", limit)

    if caching:
        eprint("Caching is ON")
        cache = {}
    else:
        eprint("Caching is OFF")

    if hfunc == 0:
        eprint("Using heuristic_basic")
        heuristic_func = heuristic_basic
    else:
        eprint("Using heuristic_advanced")
        heuristic_func = heuristic_advanced

    while True:  # This is the main loop
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input()
        status, dark_score_s, light_score_s = next_input.strip().split()

        if status == "FINAL":  # Game is over.
            print()
        else:
            pockets = eval(input())  # Read in the input and turn it into an object
            mancalas = eval(input())  # Read in the input and turn it into an object
            board = Board(pockets, mancalas)

            # Select the move and send it to the manager
            if caching:
                move, value = minimax_max_limit_caching(board, player, heuristic_func, limit, cache)
            elif limit >= 0:
                move, value = minimax_max_limit(board, player, heuristic_func, limit)
            else:
                move, value = minimax_max_basic(board, player, heuristic_func)
            print("{}".format(move))


if __name__ == "__main__":
    run_ai()

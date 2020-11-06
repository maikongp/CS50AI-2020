"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    countX = 0
    countO = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1

    if countX <= countO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                available_actions.add((i, j))

    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Make a deep copy of board
    copy_board = copy.deepcopy(board)

    i = list(action)[0]
    j = list(action)[1]

    # The position of action is not empty on board
    if board[i][j] is not EMPTY:
        raise ValueError
    else:
        # Check who is the next player and set on copy board
        copy_board[i][j] = player(board)

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    players = [X, O]

    for p in players:
        # Check the row horizontally
        for i in range(len(board)):
            if board[i] == [p, p, p]:
                return p
        # Check the row vertically
        for i in range(len(board)):
            if [board[0][i], board[1][i], board[2][i]] == [p, p, p]:
                return p
        # Check the row diagonally
        if ([board[0][0], board[1][1], board[2][2]] == [p, p, p]) or ([board[0][2], board[1][1], board[2][0]] == [p, p, p]):
            return p

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    w = winner(board)

    if w is not None:
        return True
    else:
        # Check if game is progress
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == EMPTY:
                    return False

        #The game is over, but without winner
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board):
        w = winner(board)
        if w == X:
            return 1
        elif w == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    p = player(board)

    if p == X:
        score, move_i, move_j = max_value(board)
    else:
        score, move_i, move_j = min_value(board)

    return [move_i, move_j]

def max_value (board):

    if terminal(board):
        return utility(board), None, None

    # Set minus Infinitive
    value = float("-inf")

    # Get all available actions to player
    available_actions = actions(board)

    for act in available_actions:
         bestScore = min_value(result(board, act))[0]
         if bestScore > value:
             value = bestScore
             move_i = act[0]
             move_j = act[1]

    return value, move_i, move_j

def min_value (board):

    if terminal(board):
        return utility(board), None, None

    # Set minus Infinitive
    value = float("inf")

    # Get all available actions to player
    available_actions = actions(board)

    for act in available_actions:
         bestScore = max_value(result(board, act))[0]
         if bestScore < value:
             value = bestScore
             move_i = act[0]
             move_j = act[1]

    return value, move_i, move_j

import chess
import numpy as np
from .minimax import minimax


def get_move(board, depth=4): #Fixed depth of 4
    top_move = None
    depth = 4
    if board.turn == chess.WHITE:
      top_eval = -np.inf
    else:
      top_eval = np.inf

    for move in board.legal_moves: #Iterates through all legal moves
        board.push(move)

        # When black, grab smallest eval
        eval = minimax(board, depth - 1, -np.inf, np.inf, board.turn) #Calling Eval

        board.pop()

        if board.turn == chess.WHITE:
            if eval > top_eval:
                top_move = move
                top_eval = eval
        else:
            if eval < top_eval:
                top_move = move
                top_eval = eval

    print("CHOSEN MOVE: ", top_move, "WITH EVAL: ", top_eval) #Output in terminal
    return top_move

#Vital Imports
from .evaluation import get_evaluation
import numpy as np

#Minimax funct
def minimax(board, depth, alpha, beta, maximizing_player):
  #We need eval 
  if depth == 0 or board.is_game_over():
    return get_evaluation(board)
  # If maximizing_player is True, we are maximizing the score
  if maximizing_player:
    max_eval = -np.inf
    for move in board.legal_moves:
      board.push(move)
      eval = minimax(board, depth - 1, alpha, beta, False)
      board.pop()
      max_eval = max(max_eval, eval)
      alpha = max(alpha, eval)
      if beta <= alpha:
        break
    return max_eval
  # If maximizing_player is False, we are minimizing the score
  else:
    min_eval = np.inf
    for move in board.legal_moves:
      board.push(move)
      eval = minimax(board, depth - 1, alpha, beta, True)
      board.pop()
      min_eval = min(min_eval, eval)
      beta = min(beta, eval)
      if beta <= alpha:
        break
    return min_eval
  

  #Alpha-Beta pruning is used here
  #Check out chessprogramming.org for more info
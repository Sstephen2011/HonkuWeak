#Final evaluation file
#Essential imports
from .material import get_material
import chess
from . import positions

#Main Funct 
def get_evaluation(board):

    # If checkmate
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    # If stalemate
    if board.is_stalemate():
            return 0
    # If draw  
    if board.is_insufficient_material():
            return 0
    #Total Material
    total_material = get_material(board)


    #Table Evals integration
    pawnsq = sum([positions.pawn[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq = pawnsq + sum([-positions.pawn[chess.square_mirror(i)]
                        for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([positions.knight[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-positions.knight[chess.square_mirror(i)]
                            for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq = sum([positions.bishop[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum([-positions.bishop[chess.square_mirror(i)]
                            for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([positions.rook[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rooksq = rooksq + sum([-positions.rook[chess.square_mirror(i)]
                        for i in board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([positions.queen[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queensq = queensq + sum([-positions.queen[chess.square_mirror(i)]
                            for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([positions.king[i] for i in board.pieces(chess.KING, chess.WHITE)])
    kingsq = kingsq + sum([-positions.king[chess.square_mirror(i)]
                        for i in board.pieces(chess.KING, chess.BLACK)])
    #Final Evaluation
    eval = total_material + pawnsq + knightsq + rooksq + queensq + kingsq 
    #Returning the final evaluation
    return eval

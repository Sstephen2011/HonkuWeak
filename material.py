#This whole file is for material calculation

import chess 

def get_material(board):
    # Material values or *weights* 
    # Material weights are relative 
    pw = 100
    kw = 310
    bw = 330
    rw = 500
    qw = 900
    kingw = 20000 #King is inf

#White pieces
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    wk = len(board.pieces(chess.KNIGHT, chess.WHITE))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    wking = len(board.pieces(chess.KING, chess.WHITE))

#Black Pieces
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    bk = len(board.pieces(chess.KNIGHT, chess.BLACK))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    bking = len(board.pieces(chess.KING, chess.BLACK))

#Time to assign the weights into python-chess pieces, and store them in variables
    ## White
    wpw = wp * pw
    wrw = wr * rw
    wkw = wk * kw
    wbw = wb * bw
    wqw = wq * qw
    wkingw = wking * kingw

    ## Black
    bpw = bp * pw
    brw = br * rw
    bkw = bk * kw
    bbw = bb * bw
    bqw = bq * qw
    bkingw = bking * kingw

    white_material = wpw + wrw + wkw + wbw + wqw + wkingw #Total white material
    black_material = bpw + brw + bkw + bbw + bqw + bkingw #Total black material

    total_material = white_material - black_material #Total material

    return total_material #Return material values
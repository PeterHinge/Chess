import pygame


from ChessBoard import ChessBoard
from ChessPieces import *


pygame.init()


def checkmate():
    if in_check():
        pass


def stalemate():
    pass


def in_check():
    pass


def turn(player):
    pass


def is_inside_board(move):
    return 0 <= move <= 7


def check_valid_moves(possible_moves):
    valid_moves = []
    for move in possible_moves:
        if is_inside_board(move):
            valid_moves.append(move)
    return valid_moves


def flip_board(board):
    board['a1'], board['a8'] = board['a8'], board['a1']
    board['a2'], board['a7'] = board['a7'], board['a2']
    board['a3'], board['a6'] = board['a6'], board['a3']
    board['a4'], board['a5'] = board['a5'], board['a4']
    board['a5'], board['a4'] = board['a4'], board['a5']
    board['a6'], board['a3'] = board['a3'], board['a6']
    board['a7'], board['a2'] = board['a2'], board['a7']
    board['a8'], board['a1'] = board['a1'], board['a8']
    return board


def game():
    board = ChessBoard().board
    player_turn = WHITE

    background = pygame.image.load("Board.png")

    screen = pygame.display.set_mode(background)

    exit_game = False
    while not exit_game:
        if checkmate():
            exit_game = True

        if player_turn == WHITE:

            player_turn = BLACK
        elif player_turn == BLACK:
            player_turn = WHITE


chess = ChessGame()
print(chess.board)

#import pygame

from ChessBoard import ChessBoard
from ChessPieces import *



class ChessGame:
    def __init__(self):
        self.player_turn = WHITE
        self.board_layout = ChessBoard().layout
        self.game_board = ChessBoard().empty_board



    def turn(self):
        if self.player_turn == WHITE:
            self.player_turn = BLACK
        else:
            self.player_turn = WHITE

    def check_valid_move(self, start_position, end_position):
        travel = sum(self.board_layout[start_position], self.board_layout[end_position])
        if travel in []:
            pass




chess = ChessGame()
print(chess.game_board)


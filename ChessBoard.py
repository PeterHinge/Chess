from ChessPieces import *


class Square:
    def __init__(self):
        self.piece = None
        self.occupied = False


class ChessBoard:
    def __init__(self):
        self.width = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.height = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.layout = [[letter + number for letter in self.width] for number in self.height]
        self.player_turn = WHITE

        self.board = []
        for lst in self.layout:
            for square in lst:
                self.board.append(square)
        self.board = {square: Square() for square in self.board}

        self.ready_board()

    def __repr__(self):
        print(self.board)

    def ready_board(self):
        # Setting up white:
        self.board['e1'].piece = King(WHITE, [0, 4])
        self.board['d1'].piece = Queen(WHITE, [0, 3])
        self.board['a1'].piece = Rock(WHITE, [0, 0])
        self.board['h1'].piece = Rock(WHITE, [0, 7])
        self.board['b1'].piece = Knight(WHITE, [0, 1])
        self.board['g1'].piece = Knight(WHITE, [0, 6])
        self.board['c1'].piece = Bishop(WHITE, [0, 2])
        self.board['f1'].piece = Bishop(WHITE, [0, 5])
        self.board['a2'].piece = Pawn(WHITE, [1, 0], UP)
        self.board['b2'].piece = Pawn(WHITE, [1, 1], UP)
        self.board['c2'].piece = Pawn(WHITE, [1, 2], UP)
        self.board['d2'].piece = Pawn(WHITE, [1, 3], UP)
        self.board['e2'].piece = Pawn(WHITE, [1, 4], UP)
        self.board['f2'].piece = Pawn(WHITE, [1, 5], UP)
        self.board['g2'].piece = Pawn(WHITE, [1, 6], UP)
        self.board['h2'].piece = Pawn(WHITE, [1, 7], UP)

        # Setting up black:
        self.board['e8'].piece = King(BLACK, [7, 4])
        self.board['d8'].piece = Queen(BLACK, [7, 3])
        self.board['a8'].piece = Rock(BLACK, [7, 0])
        self.board['h8'].piece = Rock(BLACK, [7, 7])
        self.board['b8'].piece = Knight(BLACK, [7, 1])
        self.board['g8'].piece = Knight(BLACK, [7, 6])
        self.board['c8'].piece = Bishop(BLACK, [7, 2])
        self.board['f8'].piece = Bishop(BLACK, [7, 5])
        self.board['a7'].piece = Pawn(BLACK, [6, 0], DOWN)
        self.board['b7'].piece = Pawn(BLACK, [6, 1], DOWN)
        self.board['c7'].piece = Pawn(BLACK, [6, 2], DOWN)
        self.board['d7'].piece = Pawn(BLACK, [6, 3], DOWN)
        self.board['e7'].piece = Pawn(BLACK, [6, 4], DOWN)
        self.board['f7'].piece = Pawn(BLACK, [6, 5], DOWN)
        self.board['g7'].piece = Pawn(BLACK, [6, 6], DOWN)
        self.board['h7'].piece = Pawn(BLACK, [6, 7], DOWN)

        for square in self.board:
            if square.piece:
                square.occupied = True


if __name__ == '__main__':
    board = ChessBoard()
    print(board.layout)
    print(board.board)

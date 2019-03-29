from ChessPieces import *


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
        self.board = {square: None for square in self.board}

        self.ready_board()

    def __repr__(self):
        print(self.board)

    def ready_board(self):
        # Setting up white:
        self.board['e1'] = King(WHITE, [0, 4])
        self.board['d1'] = Queen(WHITE, [0, 3])
        self.board['a1'] = Rock(WHITE, [0, 0])
        self.board['h1'] = Rock(WHITE, [0, 7])
        self.board['b1'] = Knight(WHITE, [0, 1])
        self.board['g1'] = Knight(WHITE, [0, 6])
        self.board['c1'] = Bishop(WHITE, [0, 2])
        self.board['f1'] = Bishop(WHITE, [0, 5])
        self.board['a2'] = Pawn(WHITE, [1, 0], UP)
        self.board['b2'] = Pawn(WHITE, [1, 1], UP)
        self.board['c2'] = Pawn(WHITE, [1, 2], UP)
        self.board['d2'] = Pawn(WHITE, [1, 3], UP)
        self.board['e2'] = Pawn(WHITE, [1, 4], UP)
        self.board['f2'] = Pawn(WHITE, [1, 5], UP)
        self.board['g2'] = Pawn(WHITE, [1, 6], UP)
        self.board['h2'] = Pawn(WHITE, [1, 7], UP)

        # Setting up black:
        self.board['e8'] = King(BLACK, [7, 4])
        self.board['d8'] = Queen(BLACK, [7, 3])
        self.board['a8'] = Rock(BLACK, [7, 0])
        self.board['h8'] = Rock(BLACK, [7, 7])
        self.board['b8'] = Knight(BLACK, [7, 1])
        self.board['g8'] = Knight(BLACK, [7, 6])
        self.board['c8'] = Bishop(BLACK, [7, 2])
        self.board['f8'] = Bishop(BLACK, [7, 5])
        self.board['a7'] = Pawn(BLACK, [6, 0], DOWN)
        self.board['b7'] = Pawn(BLACK, [6, 1], DOWN)
        self.board['c7'] = Pawn(BLACK, [6, 2], DOWN)
        self.board['d7'] = Pawn(BLACK, [6, 3], DOWN)
        self.board['e7'] = Pawn(BLACK, [6, 4], DOWN)
        self.board['f7'] = Pawn(BLACK, [6, 5], DOWN)
        self.board['g7'] = Pawn(BLACK, [6, 6], DOWN)
        self.board['h7'] = Pawn(BLACK, [6, 7], DOWN)


if __name__ == '__main__':
    board = ChessBoard()
    print(board.layout)
    print(board.board)

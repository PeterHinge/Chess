from ChessPieces import *




class ChessBoard:
    def __init__(self):
        self.width = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.height = ['8', '7', '6', '5', '4', '3', '2', '1']
        self.layout = [[letter + number for letter in self.width] for number in self.height]
        self.empty_board = [{letter + number: None for letter in self.width} for number in self.height]

        self.tiles = []
        for lst in self.layout:
            for i in lst:
                self.tiles.append(i)
        self.tiles = {i: None for i in self.tiles}

    def ready_board(self):
        # Setting up white:
        self.tiles['e1'] = King(WHITE)
        self.tiles['d1'] = Queen(WHITE)
        self.tiles['a1'] = Rock(WHITE)
        self.tiles['h1'] = Rock(WHITE)
        self.tiles['b1'] = Knight(WHITE)
        self.tiles['g1'] = Knight(WHITE)
        self.tiles['c1'] = Bishop(WHITE)
        self.tiles['f1'] = Bishop(WHITE)
        self.tiles['a2'] = Pawn(WHITE)
        self.tiles['b2'] = Pawn(WHITE)
        self.tiles['c2'] = Pawn(WHITE)
        self.tiles['d2'] = Pawn(WHITE)
        self.tiles['e2'] = Pawn(WHITE)
        self.tiles['f2'] = Pawn(WHITE)
        self.tiles['g2'] = Pawn(WHITE)
        self.tiles['h2'] = Pawn(WHITE)

        # Setting up black:
        self.tiles['e8'] = King(BLACK)
        self.tiles['d8'] = Queen(BLACK)
        self.tiles['a8'] = Rock(BLACK)
        self.tiles['h8'] = Rock(BLACK)
        self.tiles['b8'] = Knight(BLACK)
        self.tiles['g8'] = Knight(BLACK)
        self.tiles['c8'] = Bishop(BLACK)
        self.tiles['f8'] = Bishop(BLACK)
        self.tiles['a7'] = Pawn(BLACK)
        self.tiles['b7'] = Pawn(BLACK)
        self.tiles['c7'] = Pawn(BLACK)
        self.tiles['d7'] = Pawn(BLACK)
        self.tiles['e7'] = Pawn(BLACK)
        self.tiles['f7'] = Pawn(BLACK)
        self.tiles['g7'] = Pawn(BLACK)
        self.tiles['h7'] = Pawn(BLACK)


if __name__ == '__main__':
    board = ChessBoard()
    print(board.layout)
    print(board.empty_board)
    for i in board.empty_board:
        print(i)
    print(board.empty_board[0]['a8'])
    print(board.tiles)
    board.ready_board()
    print(board.tiles)

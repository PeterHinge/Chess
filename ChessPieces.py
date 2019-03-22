WHITE = "white"
BLACK = "black"


class ChessPiece:
    def __init__(self, color):
        self.color = color
        self.is_alive = True


class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):
        return str(self.color) + ' ♔'


class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):
        return str(self.color) + ' ♕'


class Rock(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):
        return str(self.color) + ' ♖'


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):
        return str(self.color) + ' ♘'


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):
        return str(self.color) + ' ♗'


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):
        return str(self.color) + ' ♙'


if __name__ == '__main__':
    print()

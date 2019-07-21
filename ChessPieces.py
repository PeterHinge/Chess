WHITE = "white"
BLACK = "black"
UP = "up"
DOWN = "down"


class ChessPiece:
    def __init__(self, color, position):
        self.x = position[0]
        self.y = position[1]
        self.color = color
        self.is_alive = True


class King(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.has_moved = False

    def __repr__(self):
        return str(self.color) + ' ♔'

    def get_possible_moves(self):
        possible_moves = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
        for moves in possible_moves:
            moves[0] += self.x
            moves[1] += self.y
        return possible_moves


class Queen(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __repr__(self):
        return str(self.color) + ' ♕'

    def get_possible_moves(self):
        possible_moves = [[0, i-7] for i in range(16) if i != 7] + [[i-7, 0] for i in range(16) if i != 7] + \
                         [[i-7, i-7] for i in range(16) if i != 7] + \
                         [[-i-1, i+1] for i in range(7)] + [[i+1, -i-1] for i in range(7)]
        for moves in possible_moves:
            moves[0] += self.x
            moves[1] += self.y
        return possible_moves


class Rock(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.has_moved = False

    def __repr__(self):
        return str(self.color) + ' ♖'

    def get_possible_moves(self):
        possible_moves = [[0, i-7] for i in range(16) if i != 7] + [[i-7, 0] for i in range(16) if i != 7]
        for moves in possible_moves:
            moves[0] += self.x
            moves[1] += self.y
        return possible_moves


class Knight(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __repr__(self):
        return str(self.color) + ' ♘'

    def get_possible_moves(self):
        possible_moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-2, 1]]
        for moves in possible_moves:
            moves[0] += self.x
            moves[1] += self.y
        return possible_moves


class Bishop(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __repr__(self):
        return str(self.color) + ' ♗'

    def get_possible_moves(self):
        possible_moves = [[i-7, i-7] for i in range(16) if i != 7] + \
                         [[-i-1, i+1] for i in range(7)] + [[i+1, -i-1] for i in range(7)]
        for moves in possible_moves:
            moves[0] += self.x
            moves[1] += self.y
        return possible_moves


class Pawn(ChessPiece):
    def __init__(self, color, position, direction):
        super().__init__(color, position)
        self.direction = direction
        self.has_moved = False
        self.en_passant = False

    def __repr__(self):
        return str(self.color) + ' ♙'

    def get_possible_moves(self):
        possible_moves = [[-1, 1], [0, 1], [1, 1], [1, -1], [0, -1], [-1, -1]]
        for moves in possible_moves:
            moves[0] += self.x
            moves[1] += self.y
            if self.direction is UP:
                return possible_moves[0:3]
            elif self.direction is DOWN:
                return possible_moves[3:6]


if __name__ == '__main__':
    king = King(WHITE, [3, 0])
    queen = Queen(WHITE, [4, 0])
    rock = Rock(WHITE, [0, 0])
    knight = Knight(WHITE, [1, 0])
    bishop = Bishop(WHITE, [2, 0])
    pawn1 = Pawn(WHITE, [0, 1], UP)
    pawn2 = Pawn(WHITE, [0, 6], DOWN)

    print(king.get_possible_moves())
    print(queen.get_possible_moves())
    print(rock.get_possible_moves())
    print(knight.get_possible_moves())
    print(bishop.get_possible_moves())
    print(pawn1.get_possible_moves())
    print(pawn2.get_possible_moves())

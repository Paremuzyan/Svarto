class Piece:

    def __init__(self, color, position, image):
        self.__color = color
        self.__image = image
        self.set_initial_position(position)

    def get_position(self):
        return self.__position

    def move_to(self, row, col):
        self.__position = (row, col)

    def set_initial_position(self, position):
        # check by type and set position
        self.__position = position

class Cell:
    def __init__(self, position, color):
        self.__position = position
        self.__color = color
        self.__occupied = False

    def is_occupied(self):
        return self.__occupied

    def show_cell(self):
        if self.__color == 'black':
            print(chr(11035), end=" ")
        else:
            print(chr(11036), end=" ")

    def occupy_cell(self):
        self.__occupied = True

    def make_free_cell(self):
        self.__occupied = False


class Chessboard:
    def __init__(self):
        self.__size = 8
        self.__board_info = []

    def create(self):
        for row in range(self.__size):
            self.__board_info.append([])
            for col in range(self.__size):
                if (row + col) % 2 == 0:
                    self.__board_info[row].append(Cell((row, col), 'black'))
                else:
                    self.__board_info[row].append(Cell((row, col), 'white'))

    def show_board(self):
        print(' ', ' '.join('abcdefgh'))
        for i in range(self.__size, 0, -1):
            print(i, end=' ')
            for j in range(self.__size):
                self.__board_info[i-1][j].show_cell()
            print(i, end='')
            print()
        print(' ', ' '.join('abcdefgh'))

class Player:
    def __init__(self):
        self.pieces_count = 16
        self.__all_pieces = []

    def get_all_pieces(self):
        return self.__all_pieces

    def remove_piece(self, piece):
        self.__all_pieces.remove(piece)


# զինվոր
class Pawn(Piece):
    def __init__(self, color, position, image):
        super.__init__(color, position, image)

    def set_position(self, row, col):
        self.__position = (row, col)

    def move_to(self, row, col):
        print(f'{self.color} Pawn moving to {row, col}')


# նավակ
class Rook(Piece):
    def __init__(self, color, position, image):
        super.__init__(color, position, image)

    def set_position(self, row, col):
        self.__position = (row, col)

    def move_to(self, row, col):
        print(f'{self.color} Pawn moving to {row, col}')


# ձի
class Knight(Piece):
    def __init__(self, color, position, image):
        super.__init__(color, position, image)

    def set_position(self, row, col):
        self.__position = (row, col)

    def move_to(self, row, col):
        print(f'{self.color} Pawn moving to {row, col}')

# փիղ
class Bishop(Piece):
    def __init__(self, color, position, image):
        super.__init__(color, position, image)

    def set_position(self, row, col):
        self.__position = (row, col)

    def move_to(self, row, col):
        print(f'{self.color} Pawn moving to {row, col}')


class Queen(Piece):
    def __init__(self, color, position, image):
        super.__init__(color, position, image)

    def set_position(self, row, col):
        self.__position = (row, col)

    def move_to(self, row, col):
        print(f'{self.color} Pawn moving to {row, col}')


class King(Piece):
    def __init__(self, color, position, image):
        super.__init__(color, position, image)

    def set_position(self, row, col):
        self.__position = (row, col)

    def move_to(self, row, col):
        print(f'{self.color} Pawn moving to {row, col}')


def main():
    pass
    

chess_board = Chessboard()
chess_board.create()
chess_board.show_board()

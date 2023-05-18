class Piece:

    def __int__(self, color, position):
        self.__color = color

    def move_to(self, row, col):
        self.__position = (row, col)

    def set_position(self, position):
        # check by type and set possition
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


chess_board = Chessboard()
chess_board.create()
chess_board.show_board()

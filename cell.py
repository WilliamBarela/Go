class Cell(object):
    def __init__(self, i, j, board_size):
        self.board_size = board_size
        self.i = i
        self.j = j
        self.color = None
        self.__liberties = self.init_liberties()
        # add liberties

    def isValidBoardSize(self, board_size):
        if not isinstance(board_size, int) or board_size < 0:
            raise ValueError("Board must be a non-negative integer")
        if hasattr(self, "board_size"):
            raise ValueError("Board size cannot be reset")
        else:
            return True

    def isOnBoard(self, iterator):
        if not (iterator >= 0 and iterator < self.board_size):
            raise ValueError("i or j coordinate is invalid.")
        else:
            return True

    def isValidColor(self, color):
        valid_colors = [None, "black", "white"]

        if color not in valid_colors:
            raise ValueError("Color invalid: (choose: None, black, or white)")
        elif hasattr(self, "color") and self.color is not None:
            raise ValueError("Color cannot be changed once set")
        else:
            return True

    @property
    def board_size(self):
        return self.__board_size

    @board_size.setter
    def board_size(self, board_size):
        if self.isValidBoardSize(board_size): self.__board_size = board_size

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, i):
        if self.isOnBoard(i): self.__i = i

    @property
    def j(self):
        return self.__j

    @j.setter
    def j(self, j):
        if self.isOnBoard(j): self.__j = j

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if self.isValidColor(color): self.__color = color

    @property
    def liberties(self):
        return self.__liberties

    def init_liberties(self):
        return {"north"}

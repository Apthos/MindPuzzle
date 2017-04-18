from Graphics.Graphics import *


class Board:
    __x_pixels = -1
    __y_pixels = -1

    __vertical_boxes = -1
    __horizontal_boxes = -1

    __win__ = None

    def __construct_board(self):
        self.__win__ = GraphWin('board', self.__x_pixels, self.__y_pixels)
        self.__win__.setCoords(0.0, 0.0,
                               self.__horizontal_boxes,
                               self.__vertical_boxes)
        self.__win__.setBackground("yellow")

        for x in range(self.__horizontal_boxes):
            for y in range(self.__vertical_boxes):
                self.__win__.plotPixel(x * (self.__x_pixels / self.__horizontal_boxes),
                                       y * (self.__y_pixels / self.__vertical_boxes),
                                       "purple")
        for x in range(self.__horizontal_boxes + 1):
            for y in range(self.__vertical_boxes + 1):
                self.add_rectangle(x, y, "green")
                self.__win__.update()

    def add_rectangle(self, x, y, color):
        self.__win__.update()
        square = Rectangle(Point(x - 1, y - 1), Point(x, y))
        square.draw(self.__win__)
        square.setFill(color)

    def update_board(self):
        self.__win__.update()

    def __init__(self, x_pixels, y_pixels, horizontal_boxes, vertical_boxes):
        self.__x_pixels = x_pixels
        self.__y_pixels = y_pixels
        self.__horizontal_boxes = horizontal_boxes
        self.__vertical_boxes = vertical_boxes

        if x_pixels < 10:
            print("Must have at least 10 pixels!");
            return

        if y_pixels < 10:
            print("Must have at least 10 pixels!");
            return

        if horizontal_boxes < 2:
            print("Must have at least 2 boxes!");
            return

        if x_pixels < 2:
            print("Must have at least 2 boxes!");
            return

        self.__construct_board()

        self.__win__.

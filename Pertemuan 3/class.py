
class GameObject:
    def __init__ (self, symbol, row, col):
        self.symbol = symbol
        self.row = row
        self.col = col

    def printObject(self):
        print(f"object {self.symbol} di {self.row} {self.col}")



class Grid:
    def __init__ (self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = []

        for i in range(rows):

            row = []
            for j in range(cols):
                row.append("-")
            self.board.append(row)

    def display (self):
        for row in self.board:
            print(" ". join(row))

    def place_object(self, object):
        if 0 <= object.row < self.rows and 0 <= object.col < self.cols:
            self.board[object.row][object.col] = object.symbol
        else:
            print("Tidak dapat menaruh di luar arena")

    def move_object(self, object, newRow, NewCol):
        if 0 <= object.row < self.rows and 0 <= object.col < self.cols:
            self.board[object.row][object.col] = "-"
            self.board[newRow][NewCol] = object.symbol
            print(f"simbol {object.symbol} Bergerak ke {newRow} {NewCol}")
        else:
            print("Tidak dapat bergerak ke luar arena")


    

grid = Grid(10, 10)

Zilong = GameObject("Z", 1, 0)
bannet = GameObject("B", 0, 9)
Lanling = GameObject("L", 5, 1)
Ens = GameObject("E", 3, 1)

grid.place_object(Zilong)
grid.place_object(bannet)
grid.place_object(Lanling)
grid.place_object(Ens)

grid.move_object(Zilong, 5, 0)


Grid.display(grid)
Zilong.printObject()
bannet.printObject()
Lanling.printObject()
Ens.printObject()
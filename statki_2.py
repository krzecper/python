from random import randint

board_player = []
for x in range(10):
    board_player.append(["~"]*10)
        
board_computer = []
for x in range(12):
    board_computer.append(["~"]*12)

def print_board(board):
    letters = ["+", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "+"]
    print (" ".join(letters))
    for row in range(10):
        print (row, " ".join(board[row]), row)
    print (" ".join(letters))

def czteromasztowiec():
    if randint(0,1) == 1:
        row_4 = randint(1,10)
        column_4 = randint(1,7)
        board_computer[row_4][column_4] = "1"
        board_computer[row_4][column_4 + 1] = "1"
        board_computer[row_4][column_4 + 2] = "1"
        board_computer[row_4][column_4 + 3] = "1"
        board_computer[row_4][column_4 - 1] = "2"
        board_computer[row_4 - 1][column_4 - 1] = "2"
        board_computer[row_4 + 1][column_4 - 1] = "2"
        board_computer[row_4 - 1][column_4] = "2"
        board_computer[row_4 + 1][column_4] = "2"
        board_computer[row_4 - 1][column_4 + 1] = "2"
        board_computer[row_4 + 1][column_4 + 1] = "2"
        board_computer[row_4 - 1][column_4 + 2] = "2"
        board_computer[row_4 + 1][column_4 + 2] = "2"
        board_computer[row_4 - 1][column_4 + 3] = "2"
        board_computer[row_4 + 1][column_4 + 3] = "2"
        board_computer[row_4][column_4 + 4] = "2"
        board_computer[row_4 - 1][column_4 + 4] = "2"
        board_computer[row_4 + 1][column_4 + 4] = "2"
        return [[row_4 - 1],[column_4 - 1, column_4, column_4 + 1, column_4 + 2], [4]]
    else:
        row_4 = randint(1,7)
        column_4 = randint(1,10)
        board_computer[row_4][column_4] = "1"
        board_computer[row_4 + 1][column_4] = "1"
        board_computer[row_4 + 2][column_4] = "1"
        board_computer[row_4 + 3][column_4] = "1"
        board_computer[row_4 - 1][column_4 - 1] = "2"
        board_computer[row_4 - 1][column_4] = "2"
        board_computer[row_4 - 1][column_4 + 1] = "2"
        board_computer[row_4][column_4 - 1] = "2"
        board_computer[row_4][column_4 + 1] = "2"
        board_computer[row_4 + 1][column_4 - 1] = "2"
        board_computer[row_4 + 1][column_4 + 1] = "2"
        board_computer[row_4 + 2][column_4 - 1] = "2"
        board_computer[row_4 + 2][column_4 + 1] = "2"
        board_computer[row_4 + 3][column_4 - 1] = "2"
        board_computer[row_4 + 3][column_4 + 1] = "2"
        board_computer[row_4 + 4][column_4 - 1] = "2"
        board_computer[row_4 + 4][column_4] = "2"
        board_computer[row_4 + 4][column_4 + 1] = "2"
        return [[row_4 - 1, row_4, row_4 + 1, row_4 + 2], [column_4 - 1], [4]]

def trzymasztowiec():
    i = 1
    while i == 1:
        if randint(0,1) == 1:
            row = randint(1,10)
            column = randint(1,8)
            if board_computer[row][column] != "1" and board_computer[row][column] != "2":
                if board_computer[row][column + 1] != "1" and board_computer[row][column + 1] != "2":
                    if board_computer[row][column + 2] != "1" and board_computer[row][column + 2] != "2":
                        board_computer[row][column] = "1"
                        board_computer[row][column + 1] = "1"
                        board_computer[row][column + 2] = "1"
                        board_computer[row][column - 1] = "2"
                        board_computer[row - 1][column - 1] = "2"
                        board_computer[row + 1][column - 1] = "2"
                        board_computer[row - 1][column] = "2"
                        board_computer[row + 1][column] = "2"
                        board_computer[row - 1][column + 1] = "2"
                        board_computer[row + 1][column + 1] = "2"
                        board_computer[row - 1][column + 2] = "2"
                        board_computer[row + 1][column + 2] = "2"
                        board_computer[row - 1][column + 3] = "2"
                        board_computer[row + 1][column + 3] = "2"
                        board_computer[row][column + 3] = "2"
                        return [[row - 1],[column - 1, column, column + 1], [3]]
                        i = 0
        else:
            row = randint(1,8)
            column = randint(1,10)
            if board_computer[row][column] != "1" and board_computer[row][column] != "2":
                if board_computer[row + 1][column] != "1" and board_computer[row + 1][column] != "2":
                    if board_computer[row + 2][column] != "1" and board_computer[row + 2][column] != "2":                       
                        board_computer[row][column] = "1"
                        board_computer[row + 1][column] = "1"
                        board_computer[row + 2][column] = "1"
                        board_computer[row - 1][column] = "2"                        
                        board_computer[row - 1][column - 1] = "2"
                        board_computer[row - 1][column + 1] = "2"
                        board_computer[row][column - 1] = "2"
                        board_computer[row][column + 1] = "2"
                        board_computer[row + 1][column - 1] = "2"
                        board_computer[row + 1][column + 1] = "2"
                        board_computer[row + 2][column - 1] = "2"
                        board_computer[row + 2][column + 1] = "2"
                        board_computer[row + 3][column - 1] = "2"
                        board_computer[row + 3][column + 1] = "2"
                        board_computer[row + 3][column] = "2"
                        return [[row - 1, row, row + 1], [column - 1], [3]]
                        i = 0

def dwumasztowiec():
    i = 1
    while i == 1:
        if randint(0,1) == 1:
            row = randint(1,10)
            column = randint(1,9)
            if board_computer[row][column] != "1" and board_computer[row][column] != "2":
                if board_computer[row][column + 1] != "1" and board_computer[row][column + 1] != "2":
                    board_computer[row][column] = "1"
                    board_computer[row][column + 1] = "1"
                    board_computer[row][column - 1] = "2"
                    board_computer[row - 1][column - 1] = "2"
                    board_computer[row + 1][column - 1] = "2"
                    board_computer[row - 1][column] = "2"
                    board_computer[row + 1][column] = "2"
                    board_computer[row - 1][column + 1] = "2"
                    board_computer[row + 1][column + 1] = "2"
                    board_computer[row - 1][column + 2] = "2"
                    board_computer[row + 1][column + 2] = "2"
                    board_computer[row][column + 2] = "2"
                    return [[row - 1],[column - 1, column], [2]]
                    i = 0
        else:
            row = randint(1,9)
            column = randint(1,10)
            if board_computer[row][column] != "1" and board_computer[row][column] != "2":
                if board_computer[row + 1][column] != "1" and board_computer[row + 1][column] != "2":                     
                    board_computer[row][column] = "1"
                    board_computer[row + 1][column] = "1"
                    board_computer[row - 1][column] = "2"                        
                    board_computer[row - 1][column - 1] = "2"
                    board_computer[row - 1][column + 1] = "2"
                    board_computer[row][column - 1] = "2"
                    board_computer[row][column + 1] = "2"
                    board_computer[row + 1][column - 1] = "2"
                    board_computer[row + 1][column + 1] = "2"
                    board_computer[row + 2][column - 1] = "2"
                    board_computer[row + 2][column + 1] = "2"
                    board_computer[row + 2][column] = "2"
                    return [[row - 1, row], [column - 1], [2]]
                    i = 0

def jednomasztowiec():
    i = 1
    while i == 1:
        row = randint(1,10)
        column = randint(1,10)
        if board_computer[row][column] != "1" and board_computer[row][column] != "2":
            board_computer[row][column] = "1"
            board_computer[row - 1][column] = "2"
            board_computer[row - 1][column - 1] = "2"
            board_computer[row - 1][column + 1] = "2"
            board_computer[row][column - 1] = "2"
            board_computer[row][column + 1] = "2"
            board_computer[row + 1][column - 1] = "2"
            board_computer[row + 1][column] = "2"
            board_computer[row + 1][column + 1] = "2"
            return [[row - 1],[column - 1], [1]]
            i = 0

czteromasztowiec = czteromasztowiec()    
trzymasztowiec_1 = trzymasztowiec()
trzymasztowiec_2 = trzymasztowiec()
dwumasztowiec_1 = dwumasztowiec()
dwumasztowiec_2 = dwumasztowiec()
dwumasztowiec_3 = dwumasztowiec()
jednomasztowiec_1 = jednomasztowiec()
jednomasztowiec_2 = jednomasztowiec()
jednomasztowiec_3 = jednomasztowiec()
jednomasztowiec_4 = jednomasztowiec()


del board_computer[11]
del board_computer[0]
for row in range(0,10):
    del board_computer[row][11]
for row in range(0,10):
    del board_computer[row][0]

for row in range(10):
    for item in range(10):
        if board_computer[row][item] == "2":
            board_computer[row][item] = "~"

def zliczacz_trafien(statek, row, column):
    if statek[2][0] > 0:
        if row in statek[0]:
            if column in statek[1]:
                statek[2][0] -= 1
                if statek[2][0] == 0:
                    print ("    !!!ZATOPIONY!!!")

dict_for_columns = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8, "J" : 9}
                    
def tura():
    print_board(board_player)
    
    print ("\n")
    
    column = input("Podaj kolumne: ")
    if column == "koniec":
        return 2

    row = input("Podaj rzad: ")
    if row == "koniec":
        return 2

    print ("\n")
    
    row = int(row)
    column = dict_for_columns[column.upper()]

    if row > 9 or column > 9:
        print ("Strzelasz poza mape!!!")
        return 0

    elif board_computer[row][column] == "1":
        print ("    !!!TRAFIONY!!!!")
        board_computer[row][column] = "S"
        board_player[row][column] = "X"
        zliczacz_trafien(czteromasztowiec, row, column)
        zliczacz_trafien(trzymasztowiec_1, row, column)
        zliczacz_trafien(trzymasztowiec_2, row, column)
        zliczacz_trafien(dwumasztowiec_1, row, column)
        zliczacz_trafien(dwumasztowiec_2, row, column)
        zliczacz_trafien(dwumasztowiec_3, row, column)
        zliczacz_trafien(jednomasztowiec_1, row, column)
        zliczacz_trafien(jednomasztowiec_2, row, column)
        zliczacz_trafien(jednomasztowiec_3, row, column)
        zliczacz_trafien(jednomasztowiec_4, row, column)
        return 1

    elif board_computer[row][column] == "~":
        print ("      !!!PUDLO!!!")
        board_computer[row][column] = "S"
        board_player[row][column] = "o"
        return 0

    elif board_computer[row][column] == "S":
        print ("Tu juz strzelales!!!")
        return 0

print ('Witaj w grze w statki!! \nNajpierw podaj litere kolumny (A-J),a nastepnie cyfre rzedu (0-9).\nBy zakonczyc gre w dowolnym momencie napisz "koniec".')
print ('Poszczegolne wpisy zatwierdzaj naciskajac ENTER.')
i = 20
while i > 0:
    a = tura()
    if a == 2:
        print_board(board_computer)
        break
    i -= a    
else:
    print ("!!!!!!!ZWYCIESTWO!!!!!!")
    print_board(board_player)
    
    


         
state = "??????????????????????????rnbqkbnr????pppppppp????........????........????........????........????PPPPPPPP????RNBQKBNR??????????????????????????"
movements = {"n":[-23, -25, -14, -10, 10, 14, 23, 25], "N": [-23, -25, -14, -10, 10, 14, 23, 25],
"b": [-13,-11,13,11], "B": [-13,-11,13,11],
"r":[-12,-1,1,12], "R":[-12,-1,1,12],
"q": [-13,-11,13,11,-12,-1,1,12], "Q":[-13,-11,13,11,-12,-1,1,12],
"k": [-13,-11,13,11,-12,-1,1,12], "K":[-13,-11,13,11,-12,-1,1,12]
 }
eight_x_eight = [26, 27, 28, 29, 30, 31, 32, 33, 38,39,40,41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 56, 57, 62, 63, 64, 65, 66, 67, 68, 69, 74, 75, 76, 77, 78, 79, 80, 81, 86, 87, 88, 89, 90, 91, 92, 93, 98, 99, 100, 101, 102, 103, 104, 105, 110, 111, 112, 113, 114, 115, 116, 117]

def display_board(board):
    display = ""
    length = 0
    for i in eight_x_eight:
        display += board[i]
        length += 1
        if length %8 == 0:
            display += "\n"
    return display

def possible_moves_white(board):
    moves = set()
    for space in eight_x_eight:
        piece = board[space]
        if piece == "." or piece.islower(): continue
        #pawn code
        elif piece == "P":
            if board[space-12] == ".":
                moves.add((space, space-12))
                if space >96 and board[space-24] == ".": moves.add((space, space-24))
            if board[space-11].islower(): moves.add((space, space-11))
            if board[space - 13].islower(): moves.add((space, space-13))
        #knight code

        elif piece == "N":
            for move in movements["N"]:
                if not board[space + move].isupper() and board[space+move] != "?":
                    moves.add((space, space+move))
        elif piece == "K":
            for move in movements["K"]:
                if not board[space + move].isupper() and board[space+move] != "?":
                    moves.add((space,space+move))
        else:
            for direction in movements[piece]:
                new_space = space + direction
                if  piece.isupper():
                    while board[new_space] == ".":
                        moves.add((space, new_space))
                        new_space += direction
                    if board[new_space].islower():
                        moves.add((space, new_space))
    return moves

def possible_moves_black(board):
    moves = set()
    for space in eight_x_eight:
        piece = board[space]
        if piece == "." or piece.isupper: continue
        if piece == "p":
            if board[space+12] == ".":
                moves.add((space, space+12))
                if space < 48 and board[space+24] == ".": moves.add((space, space+24))
            if board[space+11].isupper(): moves.add((space, space+11))
            if board[space + 13].isupper(): moves.add((space, space+13))
        elif piece == "n":
            for move in movements["n"]:
                if not board[space + move].islower() and board[space+move] != "?":
                    moves.add((space, space+move))
        #king move
        elif piece == "k":
            for move in movements["k"]:
                if not board[space + move].islower() and board[space+move] != "?":
                    moves.add((space,space+move))
        else:
            for direction in movements[piece]:
                new_space = space + direction
                if piece.islower():
                    while board[new_space] == ".":
                        moves.add((space, new_space))
                        new_space += direction
                    if board[new_space].isupper():
                        moves.add((space, new_space))
    return moves

def black_check(board):
    king = board.index("k")
    if board[king + 11] == "P" or board[king+13] == "P":
        return True
    for direction in movements["N"]:
        if board[king+direction] == "N":
            return True
    for direction in movements["B"]:
        new_space = king + direction
        while board[new_space] == ".":
            new_space += direction
        if board[new_space] == "B" or board[new_space] == "Q":
            return True
    for direction in movements["R"]:
        new_space = king + direction
        while board[new_space] == ".":
            new_space += direction
        if board[king+direction] == "R" or board[king+direction] == "Q":
            return True
    
def white_check(board):
    king = board.index("K")
    if board[king - 11] == "p" or board[king-13] == "p":
        return True
    for direction in movements["n"]:
        if board[king+direction] == "n":
            return True
    for direction in movements["b"]:
        new_space = king + direction
        while board[new_space] == ".":
            new_space += direction
        if board[new_space] == "b" or board[new_space] == "q":
            return True
    for direction in movements["r"]:
        new_space = king + direction
        while board[new_space] == ".":
            new_space += direction
        if board[king+direction] == "r" or board[king+direction] == "q":
            return True

def move_piece(board, startpos, endpos):
    if endpos > startpos:
        if board[startpos] == "p" and endpos >109:
            new_board =  board[0:startpos] + "." + board[startpos+1:endpos] + "q" + board[endpos+1:]
        else:
            new_board =  board[0:startpos] + "." + board[startpos+1:endpos] + board[startpos] + board[endpos+1:]

    else:
        if board[startpos] == "P" and endpos < 35:
            new_board =  board[0:endpos] + "Q" + board[endpos+1:startpos] + "." + board[startpos+1:]
        else:
            new_board =  board[0:endpos] + board[startpos] + board[endpos+1:startpos] + "." + board[startpos+1:]
    return new_board

print(display_board(state))
print(possible_moves(state))

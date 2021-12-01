def isValidChessBoard(chess_dictionary):
    """Check if a dictionary contains valid chess board. """
    # Count how many kings. If 0 or > 1 kings for either color
    # return False.
    wpieces_counter = 0
    bpieces_counter = 0
    bpawn_counter = 0
    wpawn_counter = 0
    bking_counter = 0
    wking_counter = 0
    for king in chess_dictionary.values():

        if king == "bking":
            bking_counter += 1
        if king == "wking":
            wking_counter += 1

    for piece in chess_dictionary.values():
        color = piece[0]

        # Check that there are no more than 16 pieces per player
      
        if color == "b":
            bpieces_counter += 1
        if color == "w":
            wpieces_counter += 1
        # Check that there are no more than 8 pawns per player
        if piece == 'bpawn':
            bpawn_counter += 1
        if piece == 'wpawn':
            wpawn_counter += 1
    
    # check for a valid location
    board_keys = {'a1':'','a2':'','a3':'','a4':'','a5':'','a6':'','a7':'','a8':'',
                   'b1':'','b2':'','b3':'','b4':'','b5':'','b6':'','b7':'','b8':'',
                   'c1':'','c2':'','c3':'','c4':'','c5':'','c6':'','c7':'','c8':'',
                   'd1':'','d2':'','d3':'','d4':'','d5':'','d6':'','d7':'','d8':'',
                   'e1':'','e2':'','e3':'','e4':'','e5':'','e6':'','e7':'','e8':'',
                   'f1':'','f2':'','f3':'','f4':'','f5':'','f6':'','f7':'','f8':'',
                   'g1':'','g2':'','g3':'','g4':'','g5':'','g6':'','g7':'','g8':'',
                   'h1':'','h2':'','h3':'','h4':'','h5':'','h6':'','h7':'','h8':''}
    
    print("White kings = " + str(wking_counter))
    print("Black kings = " + str(bking_counter))
    print("Black pieces = " + str(bpieces_counter))
    print("White pieces = " + str(wpieces_counter))
    print("Black pawns = " + str(bpawn_counter))
    print("White pawns = " + str(wpawn_counter))

    if 'bking' not in chess_dictionary.values() or 'wking' not in chess_dictionary.values():
        print("Not enough kings")
        return(False)
    if bking_counter > 1 or wking_counter > 1:
        print("Too many kings")
        return(False)
    if bpieces_counter > 16:
        print("Inappropriate number of black pieces")
        return(False)
    if wpieces_counter > 16:
        print("Inappropriate number of white pieces")
        return(False)
    if bpawn_counter > 8:
        print("Inappropriate number of black pawns")
        return(False)
    if wpawn_counter > 8:
        print("Inappropriate number of white pawns")
        return(False)
    # Check that board positions are valid
    for position in chess_dictionary:
        if position not in board_keys:
            print("Invalid position")
            return(False)
    # Check that piece names are valid
    valid_piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    for piece in chess_dictionary.values():
        piece_name = piece[1:]
        if piece_name not in valid_piece_names:
            print("Invalid piece name provided")
            return(False)

 
    
chess_dict = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
isValidChessBoard(chess_dict)

too_many_kings =  {'1h': 'bking', '6c': 'wqueen', '2g': 'wking', '5h': 'bqueen', '3e': 'wking'}
isValidChessBoard(too_many_kings)

print(isValidChessBoard({"h1": "bking", "c6": "wqueen", "g2": "bbishop", "h5": "bqueen", "e3": "wking"}))  # True
print(isValidChessBoard({"a1": "bpawn", "a2": "wking"}))  # False: no bking
print(isValidChessBoard({"a1": "wking", "a2": "wking", "c3": "bbishop"}))  # False: cannot have 2 white kings, no bking
print(isValidChessBoard({"a1": "bking", "z9": "wking"}))  # False: z9 is an invalid position
print(isValidChessBoard({'a1':'bking','a2':'wking','h1':'bpawn','h2':'bpawn','h3':'bpawn','h4':'bpawn','h5':'bpawn','h6':'bpawn','h7':'bpawn','h8':'bpawn','g7':'bpawn','g8':'bpawn'}))#False theres more than 8 pawns
print(isValidChessBoard({"a1": "wking", "a2": "wking", "c3": "bbishop", "c4": "bking"})) # False: cannot have 2 white kings and 1 black king
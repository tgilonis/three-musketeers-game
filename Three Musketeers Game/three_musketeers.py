# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    from copy import deepcopy
    global board
    board = deepcopy(new_board)

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return [[item for item in row] for row in board]

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
    """
    x, y = (int(ord(s[0])-65)), (int(s[1]) -1)
    # x converted from character to grid reference, y altered by 1 to correct index
    if is_legal_location((x, y)) == False:
        raise ValueError('Location outside coordinate limits')
    return((x, y))


def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    x, y = chr(location[0]+65), str(int(location[1])+1)
    # x convertered into character from number, y altered by 1 into correct index
    if is_legal_location(location) == False:
        raise ValueError('Location outside coordinate limits')
    return('{0}{1}'.format(x, y))
    #formatting required here to return location such as A5 and not (A, 5)



def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""

    return board[location[0]][location[1]]
    #board with location as indices


def all_locations():
    """Returns a list of all 25 locations on the board."""
    return [(i, j) for i in range(5) for j in range(5)]

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    temp = list(location)
    if direction == 'up':
        temp[0] -= 1
    elif direction == 'down':
        temp[0] += 1
    elif direction == 'left':
        temp[1] -= 1
    elif direction == 'right':
        temp[1] += 1
    #checks what the direction is, and alters the grid coordinate accordingly
    return (temp[0],temp[1])

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    if at(location) != 'M':
        raise ValueError("The square you have input does not contain a musketeer")
    else:
        #if the new location and direction are within the board and contain R, proceed
        if is_within_board(location, direction):
            if at(adjacent_location(location, direction)) == 'R':
                return True
        return False

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    if at(location) != 'R':
        raise ValueError("The square you have input does not contain an enemy")
    else:
        #if the new location and direction are within the board and contain _, proceed
        if is_within_board(location, direction):
            if at(adjacent_location(location, direction)) == '_':
                return True
        return False

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""

    if at(location) == 'M':
        return is_legal_move_by_musketeer(location, direction)
    elif at(location) == 'R':
        return is_legal_move_by_enemy(location, direction)


def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range.
    You can assume that input will always be in correct range."""
    direction_list = ['up', 'down', 'left', 'right']
    #if any direction is within board and legal, returns true
    for dir in direction_list:
        if is_legal_move(location, dir) and is_within_board(location, dir):
            return True
    return False

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    for i in all_locations():
        #checks if any piece at any location on the board can move, and whether that piece belongs to current user
        if at(i) == who and can_move_piece_at(i):
            return True
    return False


def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    direction_list = ['up', 'down', 'left', 'right']
    #iterates over direction list
    returning_list = ['up', 'down', 'left', 'right']
    #if the move is illegal, the direction is removed from the returning list
    for i in direction_list:
        if is_legal_move(location, i) == False:
            returning_list.remove(i)
    return returning_list

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
        You can assume that input will be a pair of integer numbers."""
    if location[0] in range(0,5) and location[1] in range(0,5):
        #if both coordinates are a number from 0-4, returns true
        return True
    else:
        return False

def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    if is_legal_location(adjacent_location(location, direction)) == True:
        return True
    else:
        return False


def all_possible_moves_for(player):

    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    return [(i, j) for i in all_locations() for j in possible_moves_from(i) if at(i) == player and can_move_piece_at(i)]


def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    board[adjacent_location(location,direction)[0]][adjacent_location(location,direction)[1]] = board[location[0]][location[1]]
    # replace the piece in the adjacent square by the piece in the current square
    board[location[0]][location[1]] = '_'
    #clear the current square of pieces - happens no matter whose move it is

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    from random import randint
    all_poss = all_possible_moves_for(who)
    #choose a random number as the index of the list and use that move
    return all_poss[randint(0,len(all_poss)-1)]

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    #iterates over board indices, using them to count number of M in rows and columns
    #return true if count in either rows or columns == 3
    for i in range(5):
        column_count = 0
        row_count = 0
        for j in range(5):
            if at((i,j)) == 'M':
                #checks count of M in rows
                row_count += 1
            if at((j,i)) == 'M':
                #checks count of M in columns
                column_count += 1
        if column_count == 3 or row_count == 3:
            return True
    return False







#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)

def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()

    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break

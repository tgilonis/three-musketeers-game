import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '_'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, R, M, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board3 =  [ [_, _, _, R, _],
            [_, _, R, R, _],
            [_, M, M, M, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board4 =  [ [R, R, R, R, M],
            [R, R, R, R, R],
            [R, R, M, R, R],
            [M, R, R, R, R],
            [_, R, R, R, R] ]

board5 =  [ [M, R, R, R, R],
            [M, R, R, R, R],
            [M, R, R, R, R],
            [M, R, R, R, R],
            [M, R, R, R, R] ]
board6 =  [ [M, R, _, _, _],
            [_, _, _, _, _],
            [_, _, M, R, _],
            [_, _, _, _, _],
            [_, _, _, _, _] ]

board7 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, R, R, _],
            [_, M, _, _, _],
            [_, _, _, R, _] ]

board8 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, _, _],
            [_, M, _, _, _],
            [_, _, _, R, _] ]

board9 =  [ [M, _, _, _, _],
            [_, _, _, _, _],
            [_, _, M, _, _],
            [_, _, _, _, _],
            [_, _, _, R, _] ]


def test_create_board():
    create_board()
    assert at((0, 0)) == 'R'
    assert at((0, 4)) == 'M'
    assert at((2, 2)) == 'M'
    assert at((3, 4)) == 'R'

def test_set_board():
    set_board(board1)
    assert at((0, 0)) == '_'
    assert at((1, 2)) == 'R'
    assert at((1, 3)) == 'M'
    assert at((0, 4)) == '_'
    set_board(board4)
    assert at((0, 0)) == 'R'
    assert at((1, 2)) == 'R'
    assert at((1, 3)) == 'R'
    assert at((0, 4)) == 'M'

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    set_board(board6)
    assert board6 == get_board()
    set_board(board3)
    assert board3 == get_board()

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == ((0, 0))
    assert string_to_location('B3') == ((1, 2))
    assert string_to_location('E5') == ((4, 4))
    assert string_to_location('C2') == ((2, 1))
    assert string_to_location('D4') == ((3, 3))

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string((0, 5))
    assert location_to_string((0, 0)) == ('A1')
    assert location_to_string((1, 2)) == ('B3')
    assert location_to_string((4, 4)) == ('E5')
    assert location_to_string((2, 1)) == ('C2')
    assert location_to_string((3, 3)) == ('D4')

def test_at():
    set_board(board1)
    assert at((0, 0)) == '_'
    assert at((1, 2)) == 'R'
    assert at((1, 3)) == 'M'
    assert at((4, 1)) == '_'
    assert at((3, 1)) == 'R'


def test_all_locations():
    set_board(board1)
    assert all_locations() == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    set_board(board6)
    assert all_locations() == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

def test_adjacent_location():
    set_board(board1)
    assert adjacent_location((0, 0), 'right') == (0, 1)
    assert adjacent_location((2, 2), 'right') == (2, 3)
    assert adjacent_location((2, 2), 'up') == (1, 2)
    assert adjacent_location((3, 4), 'left') == (3, 3)
    assert adjacent_location((1, 1), 'down') == (2, 1)

def test_is_legal_move_by_musketeer():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0, 0), 'right')
    assert is_legal_move_by_musketeer((2, 2), 'up') == True
    assert is_legal_move_by_musketeer((2, 2), 'right') == True
    set_board(board8)
    assert is_legal_move_by_musketeer((2, 2), 'right') == False
    set_board(board5)
    assert is_legal_move_by_musketeer((0, 0), 'down') == False
    assert is_legal_move_by_musketeer((2, 0), 'right') == True

def test_is_legal_move_by_enemy():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0, 0), 'right')
    assert is_legal_move_by_enemy((3, 1), 'right') == True
    set_board(board4)
    assert is_legal_move_by_enemy((3, 1), 'right') == False
    assert is_legal_move_by_enemy((0, 0), 'down') == False
    assert is_legal_move_by_enemy((2, 0), 'right') == False
    assert is_legal_move_by_enemy((4, 1), 'left') == True

def test_is_legal_move():
    set_board(board1)
    assert is_legal_move((2, 2), 'right') == True
    assert is_legal_move((1, 2), 'up') == True
    assert is_legal_move((1, 2), 'down') == False
    set_board(board5)
    assert is_legal_move((0, 0), 'down') == False
    assert is_legal_move((0, 0), 'left') == False
    set_board(board3)
    assert is_legal_move((2, 1), 'down') == True
    assert is_legal_move((2, 1), 'right') == False
    assert is_legal_move((1, 3), 'left') == False
    assert is_legal_move((1, 2), 'left') == True

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((2, 2)) == True
    assert can_move_piece_at((0, 3)) == False
    assert can_move_piece_at((1, 3)) == True
    set_board(board4)
    assert can_move_piece_at((2, 2)) == True
    assert can_move_piece_at((4, 1)) == True
    assert can_move_piece_at((0, 0)) == False

    # Replace with tests

def test_has_some_legal_move_somewhere():
    set_board(board4)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    set_board(board5)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == False
    set_board(board9)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True

    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    set_board(board6)
    assert possible_moves_from((2, 2)) == ['right']
    assert possible_moves_from((2, 3)) == ['up', 'down', 'right']
    assert possible_moves_from((0, 0)) == ['right']
    set_board(board7)
    assert possible_moves_from((2, 2)) == ['down']
    assert possible_moves_from((1, 3)) == ['down', 'left']
    assert possible_moves_from((0, 3)) == []

def test_is_legal_location():
    assert is_legal_location((0, 1)) == True
    assert is_legal_location((4, -1)) == False
    assert is_legal_location((5, 1)) == False
    assert is_legal_location((4, 2)) == True

def test_is_within_board():
    assert is_within_board((0, 0), 'right') == True
    assert is_within_board((3, 0), 'left') == False
    assert is_within_board((0, 0), 'up') == False
    assert is_within_board((4, 0), 'down') == False
    assert is_within_board((2, 2), 'left') == True
    assert is_within_board((3, 1), 'left') == True

def test_all_possible_moves_for():
    set_board(board5)
    assert all_possible_moves_for('M') == [((0, 0), 'right'), ((1, 0), 'right'), ((2, 0), 'right'), ((3, 0), 'right'), ((4, 0), 'right')]
    assert all_possible_moves_for('R') == []
    set_board(board1)
    assert all_possible_moves_for('M') == [((1, 3), 'down'), ((1, 3), 'left'), ((2, 2), 'up'), ((2, 2), 'left'), ((2, 2), 'right')]
    assert all_possible_moves_for('R') == [((1, 2), 'up'), ((1, 2), 'left'), ((2, 1), 'up'), ((2, 1), 'left'), ((2, 3), 'down'), ((2, 3), 'right'), ((3, 1), 'down'), ((3, 1), 'left'), ((3, 1), 'right'), ((4, 3), 'up'), ((4, 3), 'left'), ((4, 3), 'right')]

def test_make_move():
    set_board(board1)
    #test M
    assert at((2, 2)) == 'M'
    assert at((2, 3)) == 'R'
    make_move((2, 2), 'right')
    assert at((2, 2)) == '_'
    assert at((2, 3)) == 'M'
    #test R
    assert at((2, 1)) == 'R'
    assert at((2, 0)) == '_'
    make_move((2, 1), 'up')
    assert at((1, 1)) == 'R'
    assert at((2, 0)) == '_'
    #new board
    set_board(board2)
    #test M
    assert at((1, 3)) == 'M'
    assert at((1, 2)) == 'R'
    make_move((1, 3), 'left')
    assert at((1, 3)) == '_'
    assert at((1, 2)) == 'M'
    #test R
    assert at((2, 2)) == 'R'
    assert at((3, 2)) == '_'
    make_move((2, 2), 'down')
    assert at((2, 2)) == '_'
    assert at((3, 2)) == 'R'


def test_choose_computer_move():
    set_board(board1)
    assert choose_computer_move('M') in all_possible_moves_for('M')
    assert choose_computer_move('R') in all_possible_moves_for('R')
    # Replace with tests; should work for both 'M' and 'R'

def test_is_enemy_win():
    set_board(board4)
    assert is_enemy_win() == False
    set_board(board3)
    assert is_enemy_win() == True
    set_board(board2)
    assert is_enemy_win() == True
    set_board(board6)
    assert is_enemy_win() == False

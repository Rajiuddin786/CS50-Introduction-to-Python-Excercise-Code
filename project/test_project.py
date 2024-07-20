import pytest
from project import add_grid,check_draw,check_winner,reset_game

def test_add_grid(current_state):
    buttons=[[None for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col]={'text':current_state[row][col]}
    return buttons

def test_check_winner():
    current_state=[['X','X','X'],['','',''],['','','']]
    buttons=test_add_grid(current_state)
    assert check_winner(buttons) == True

    current_state = [['X', '', ''], ['X', '', ''], ['X', '', '']]
    buttons = test_add_grid(current_state)
    assert check_winner(buttons) == True

    current_state = [['X', '', ''], ['', 'X', ''], ['', '', 'X']]
    buttons = test_add_grid(current_state)
    assert check_winner(buttons) == True

    current_state = [['', '', 'X'], ['', 'X', ''], ['X', '', '']]
    buttons = test_add_grid(current_state)
    assert check_winner(buttons) == True

    current_state = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
    buttons = test_add_grid(current_state)
    assert check_winner(buttons) == False

def test_check_draw():
    current_state = [['X', '', ''], ['O', '', ''], ['X', '', '']]
    buttons = test_add_grid(current_state)
    assert check_draw(buttons) == False

    current_state = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
    buttons = test_add_grid(current_state)
    assert check_draw(buttons) == True

def test_reset_game():
    current_state = [['X', 'O', 'X'], ['X', 'O', 'O'], ['X', 'O', 'X']]
    buttons = test_add_grid(current_state)
    reset_game(buttons)
    for row in range(3):
        for col in range(3):
            assert buttons[row][col]['text'] == ''

if __name__ == "__main___":
    pytest.main()    
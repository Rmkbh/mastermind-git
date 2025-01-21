from src.mastermind_game import set_code, mark_guess

def test_set_code_returns_code_correctly():
    test_code = set_code()
    assert len(test_code) == 4
    colours = ['b', 'y', 'r', 'g', 'o', 'p']
    for peg in test_code:
        assert peg in colours

def test_mark_guess_works_for_no_correct_colours():
    test_code = ['g', 'g', 'p', 'p']
    test_guess = 'byro'
    assert mark_guess(test_guess, test_code) == []

def test_mark_guess_works_for_correct_guess():
    test_code = ['g', 'g', 'p', 'p']
    test_guess = 'ggpp'
    test_mark = mark_guess(test_guess, test_code)
    assert test_mark == ['b', 'b', 'b', 'b']

def test_mark_guess_works_for_incorrect_mixed():
    test_code = ['g', 'b', 'r', 'p']
    test_guess = 'byro'
    assert mark_guess(test_guess, test_code) == ['b', 'w']




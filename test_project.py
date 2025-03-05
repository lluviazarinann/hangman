import project

def test_choose_random_word():
    word_list = ["apple", "banana", "cherry"]
    word = project.choose_random_word(word_list)
    assert word in word_list

def test_update_display():
    secret = "hangman"
    # Starting display: hide all letters.
    current_display = "_______"
    # Guess the letter "a" which appears in positions 1 and 5.
    new_display = project.update_display(secret, current_display, "a")
    # Expected: h a n g m a n, but with only "a" revealed: _a___a_
    expected = "_a___a_"
    assert new_display == expected

def test_is_valid_guess():
    used_letters = {"a", "b"}
    # Valid guess: single letter not used already.
    assert project.is_valid_guess("c", used_letters) == True
    # Invalid: more than one character.
    assert project.is_valid_guess("cd", used_letters) == False
    # Invalid: non-alphabetical character.
    assert project.is_valid_guess("1", used_letters) == False
    # Invalid: letter already used.
    assert project.is_valid_guess("a", used_letters) == False

def test_has_won():
    # If there are no underscores, the game is won.
    assert project.has_won("hangman") == True
    # If there is at least one underscore, the game is not yet won.
    assert project.has_won("ha__man") == False

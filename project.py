import streamlit as st
import random

# Word categories
CATEGORIES = {
    "Animals": ["elephant", "tiger", "giraffe", "kangaroo", "zebra"],
    "Food": ["pizza", "burger", "pasta", "sushi", "taco"],
    "Countries": ["canada", "brazil", "germany", "japan", "egypt"]
}

# Hangman visuals as ASCII art
HANGMAN_PICS = [
    """
       +---+
           |
           |
           |
          ===
    """,
    """
       +---+
       O   |
           |
           |
          ===
    """,
    """
       +---+
       O   |
       |   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\  |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\  |
      /    |
          ===
    """,
    """
       +---+
       O   |
      /|\  |
      / \  |
          ===
    """
]

def choose_random_word(category):
    """Selects a random word from the chosen category."""
    return random.choice(CATEGORIES[category])

def update_display(secret_word, current_display, guess):
    """Reveals guessed letters in the word."""
    return "".join([guess if secret_word[i] == guess else current_display[i] for i in range(len(secret_word))])

def is_valid_guess(guess, used_letters):
    """Checks if the guess is a valid, single alphabetical character."""
    return len(guess) == 1 and guess.isalpha() and guess.lower() not in used_letters

def has_won(display_state):
    """Checks if the player has guessed all letters."""
    return "_" not in display_state

def get_hint(secret_word, used_letters):
    """Provides a hint by revealing an unguessed letter."""
    return next((c for c in secret_word if c not in used_letters), "")

def initialize_game(selected_category):
    """Initializes or resets the game based on the selected category."""
    st.session_state.category = selected_category
    st.session_state.secret_word = choose_random_word(selected_category)
    st.session_state.display_state = "_" * len(st.session_state.secret_word)
    st.session_state.used_letters = set()
    st.session_state.strikes = 0
    st.session_state.max_strikes = len(HANGMAN_PICS) - 1
    st.session_state.message = "Welcome! Guess a letter."
    st.session_state.hints_used = 0

def main():
    st.title("Hangman Game")
    
    # Always show selectbox so user can change category any time
    selected_category = st.selectbox("Choose a category:", list(CATEGORIES.keys()))
    
    # (Re)initialize game if category changed or if it hasn't been set
    if "category" not in st.session_state or st.session_state.category != selected_category:
        initialize_game(selected_category)

    # Display Hangman visual with st.code to preserve formatting
    st.code(HANGMAN_PICS[st.session_state.strikes], language="")

    # Display game info
    st.write("Word:", " ".join(st.session_state.display_state))
    st.write("Used Letters:", ", ".join(sorted(st.session_state.used_letters)))
    st.write(f"Strikes: {st.session_state.strikes} / {st.session_state.max_strikes}")
    st.write(st.session_state.message)
    
    # Check win condition
    if has_won(st.session_state.display_state):
        st.success("Congratulations, you've won!")
        if st.button("Play Again"):
            initialize_game(selected_category)
        return
    
    # Check losing condition
    if st.session_state.strikes >= st.session_state.max_strikes:
        st.error(f"Game Over! The word was: {st.session_state.secret_word}")
        if st.button("Play Again"):
            initialize_game(selected_category)
        return
    
    # Form for submitting a guess
    with st.form("guess_form", clear_on_submit=True):
        guess = st.text_input("Enter a letter:")
        submitted = st.form_submit_button("Submit Guess CLICK TWICE")
        if submitted and guess:
            guess = guess.lower()
            if not is_valid_guess(guess, st.session_state.used_letters):
                st.session_state.message = "Invalid guess. Try again."
            else:
                st.session_state.used_letters.add(guess)
                if guess in st.session_state.secret_word:
                    st.session_state.display_state = update_display(
                        st.session_state.secret_word, st.session_state.display_state, guess
                    )
                    st.session_state.message = f"Good guess: '{guess}' is in the word!"
                else:
                    st.session_state.strikes += 1
                    st.session_state.message = f"Wrong guess: '{guess}' is not in the word."
    
    # Button to get a hint (no score deduction now)
    if st.button("Get Hint"):
        hint = get_hint(st.session_state.secret_word, st.session_state.used_letters)
        if hint:
            st.session_state.message = f"Hint: Try guessing '{hint}'"
            st.session_state.hints_used += 1
        else:
            st.session_state.message = "No more hints available."

if __name__ == "__main__":
    main()
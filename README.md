# Hangman Game

#### Video Demo: [<[URL HERE](https://youtu.be/e9Ud751FljA)>]

#### Description:
Hangman Game is an interactive word-guessing game that was created with Python and Streamlit. The game picks a random word from a preloaded list, and the user is required to guess the word letter by letter before he/she uses up all attempts. The UI is updated dynamically to reflect the letters that have been guessed and the number of remaining attempts, respectively. This project illustrates some basic programming ideas like string manipulation, if statements, input validation, and state management with Streamlit session state.

The game provides:
- **A Streamlit-based UI** that allows users to input their guesses and see real-time feedback.
- **A predefined list of words** from which a random word is selected.
- **Tracking of used letters** to prevent duplicate guesses.
- **A win/loss condition** where players either guess the word correctly or run out of attempts.

## File Structure and Contents:

```
HANGMAN [CODESPACES: ...]
├── data/                 # Directory for any additional game data (if needed in future)
├── project.py            # Main script containing game logic and Streamlit interface
├── test_project.py       # Test cases for core functions using pytest
├── requirements.txt      # List of dependencies required to run the project
├── README.md             # This detailed project documentation file
```

## Features

- **Random Word Selection:** Uses `random.choice()` to select a word from a predefined list.
- **Interactive UI with Streamlit:** Provides a user-friendly interface with real-time updates.
- **State Management:** Utilizes `st.session_state` to retain game progress.
- **User Input Validation:** Ensures that guesses are valid single-letter inputs and have not been guessed before.
- **Win/Loss Conditions:** Automatically detects when the player has won or lost and displays an appropriate message.
- **Replay Option:** Allows users to restart the game after a win or loss.
- **Get Hint:** Allows users to get a hint.

## Getting Started

To set up and run this project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd hangman-game
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Game:**
   ```bash
   streamlit run project.py
   ```

5. **Run Tests:**
   ```bash
   pytest test_project.py
   ```

## Design Decisions and Future Improvements

### **Design Choices:**
- **Streamlit for UI:** The game leverages Streamlit's session state to maintain game progress across user interactions.
- **Modular Code Structure:** Functions are used to separate concerns, such as validating input, updating the display, and managing game states.
- **State Persistence:** Using `st.session_state` ensures that game data persists between user interactions.

### **Challenges and Solutions:**
- **Handling State:** Maintaining game progress in a web-based UI was solved using Streamlit’s `session_state`.
- **Form Submission:** Streamlit's form submission requires an extra click, so a message is displayed to remind users to confirm their guess.

### **Future Improvements:**
- **Leaderboard Feature:** Track and display the number of wins/losses.
- **More Word Categories:** Allow users to choose difficulty levels with different word sets.
- **Multiplayer Mode:** Implement a two-player version where one user inputs a word for the other to guess.
- **Graphical Enhancements:** Improve UI with images (e.g., a visual representation of the hangman as the game progresses).

## Conclusion

This Hangman Game project is a cool and engaging method of playing the popular game using a modern web interface. The pairing of a minimalist user interface, well-ordered game flow, and appropriate state management results in an entertaining and learning-based project. The code is modular and extensible, such that there is room for future extension and other features.

Enjoy playing Hangman and feel free to contribute or suggest improvements!

---
**Credits:** Developed by Lluvia Zarinan and Ander Verez.
 *(ChatGPT was used to enhance this assignment.)*
